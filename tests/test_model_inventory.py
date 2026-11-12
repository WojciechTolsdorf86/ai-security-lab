import pytest
import requests
from unittest.mock import patch, Mock
from src.model_inventory import (
    build_inventory, 
    find_model, 
    get_model_inventory,
    get_string_or_unknown,
    get_model_info
)


@pytest.fixture
def sample_inventory():
    return [
        {
            "name": "qwen2.5:3b",
            "family": "qwen",
            "parameters": "3B",
            "quantisation": "Q4"
        }
    ]


def test_build_inventory():
    test_models = [
        {
            "name": "test-qwen",
            "details": {
                "family": "qwen",
                "parameter_size": "3B",
                "quantization_level": "Q4"
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["name"] == "test-qwen"
    assert result[0]["family"] == "qwen"
    assert result[0]["parameters"] == "3B"
    assert result[0]["quantisation"] == "Q4"


def test_build_inventory_skips_incomplete_models():
    test_models = [
        {
            "details": {
                "family": "llama",
                "parameter_size": "7B",
                "quantization_level": "Q4"
            }
        },
        {
            "name": "test-qwen",
            "details": {
                "family": "qwen",
                "parameter_size": "3B",
                "quantization_level": "Q4"
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["name"] == "test-qwen"


def test_build_inventory_handles_missing_optional_fields():
    test_models = [
        {
            "name": "broken-model",
            "details": {
                "family": "qwen"
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["family"] == "qwen"
    assert result[0]["parameters"] == "Unknown"
    assert result[0]["quantisation"] == "Unknown"


def test_find_model(sample_inventory):
    result = find_model(sample_inventory, "qwen2.5:3b")

    assert result is not None
    assert result["name"] == "qwen2.5:3b"


def test_find_model_not_found(sample_inventory):
    result = find_model(sample_inventory, "mistral:7b")

    assert result is None


def test_find_model_case_insensitive(sample_inventory):
    result = find_model(sample_inventory, "QWEN2.5:3B")

    assert result is not None
    assert result["name"] == "qwen2.5:3b"


def test_find_model_empty_inventory():
    result = find_model([], "qwen2.5:3b")

    assert result is None


@patch("src.model_inventory.requests.get")
def test_get_model_inventory_success(mock_get):

    mock_response = Mock()
    mock_response.json.return_value = {
        "models": [
            {
                "name": "qwen2.5:3b",
                "details": {
                    "family": "qwen",
                    "parameter_size": "3B",
                    "quantization_level": "Q4"
                }
            }
        ]
    }


    mock_get.return_value = mock_response

    result = get_model_inventory()

    assert len(result) == 1
    assert result[0]["name"] == "qwen2.5:3b"

    mock_get.assert_called_once_with(
        "http://172.25.48.1:11434/api/tags",
        timeout=5
    )


@patch("src.model_inventory.requests.get")
def test_get_model_inventory_connection_error(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError

    result = get_model_inventory()

    assert result is None


@patch("src.model_inventory.requests.get")
def test_get_model_inventory_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout

    result = get_model_inventory()

    assert result is None


@patch("src.model_inventory.requests.get")
def test_get_model_inventory_http_error(mock_get):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "500 Server Error"
    )

    mock_get.return_value = mock_response
    
    result = get_model_inventory()

    assert result is None

@patch("src.model_inventory.requests.get")
def test_get_model_inventory_missing_models_key(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "unexpected": "data"
    }

    mock_get.return_value = mock_response

    result = get_model_inventory()

    assert result is None


@patch("src.model_inventory.requests.get")
def test_get_model_inventory_invalid_models_type(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "models": "qwen2.5:3b"
    }

    mock_get.return_value = mock_response

    result = get_model_inventory()

    assert result is None


@patch("src.model_inventory.requests.get")
def test_get_model_inventory_invalid_json(mock_get):
    mock_response = Mock()

    mock_response.json.side_effect = requests.exceptions.JSONDecodeError(
        "Invalid JSON",
        "invalid response",
        0
    )

    mock_get.return_value = mock_response

    result = get_model_inventory()

    assert result is None


def test_build_inventory_skips_invalid_model_type():
    test_models = [
        "qwen2.5:3b",
        {
            "name": "llama3",
            "details": {
                "family": "llama",
                "parameter_size": "8B",
                "quantization_level": "Q4"
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["name"] == "llama3"

def test_build_inventory_skips_invalid_details_type():
    test_models = [
        {
            "name": "broken-model",
            "details": "not-a-dictionary"
        },
        {
            "name": "qwen2.5:3b",
            "details": {
                "family": "qwen",
                "parameter_size": "3B",
                "quantization_level": "Q4"
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["name"] == "qwen2.5:3b"


def test_build_inventory_skips_invalid_name_type():
    test_models = [
        {
            "name": 12345,
            "details": {
                "family": "qwen"
            }
        },
        {
            "name": "qwen2.5:3b",
            "details": {
                "family": "qwen",
                "parameter_size": "3B",
                "quantization_level": "Q4"
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["name"] == "qwen2.5:3b"


def test_build_inventory_handles_invalid_optional_field_types():
    test_models = [
        {
            "name": "qwen2.5:3b",
            "details": {
                "family": 12345,
                "parameter_size": None,
                "quantization_level": ["Q4"]
            }
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["family"] == "Unknown"
    assert result[0]["parameters"] == "Unknown"
    assert result[0]["quantisation"] == "Unknown"


def test_get_string_or_unknown_valid_value():
    details = {"family": "qwen"}

    result = get_string_or_unknown(details, "family")

    assert result == "qwen"

def test_get_string_or_unknown_missing_key():
    details = {}

    result = get_string_or_unknown(details, "family")

    assert result == "Unknown"

def test_get_string_or_unknown_invalid_type():
    details = {"family": 12345}

    result = get_string_or_unknown(details, "family")

    assert result == "Unknown"

@pytest.mark.integration
def test_ollama_integration():
    models = get_model_inventory()

    assert models is not None
    assert isinstance(models, list)
    assert len(models) > 0

    inventory = build_inventory(models)

    assert len(inventory) > 0


def test_get_string_or_unknown_invalid_details_type():
    result = get_string_or_unknown(None, "family")

    assert result == "Unknown"

def test_build_inventory_handles_none_input():
    result = build_inventory(None)

    assert result == []

def test_build_inventory_handles_invalid_input_type():
    result = build_inventory("not a list")

    assert result == []

def test_build_inventory_handles_empty_model_name():
    test_models = [
        {
            "name": "",
            "details": {"family": "qwen"}
        }
    ]
    result = build_inventory(test_models)

    assert result == []

def test_build_inventory_handles_white_space_model_name():
    test_models = [
        {
            "name": "     ",
            "details": {"family": "qwen"}
        }
    ]
    
    result = build_inventory(test_models)
    
    assert result == []

def test_build_inventory_strips_model_name_whitespace():
    test_models = [
        {
            "name": "   qwen2.5:3b   ",
            "details": {"family": "qwen"}
        }
    ]

    result = build_inventory(test_models)

    assert len(result) == 1
    assert result[0]["name"] == "qwen2.5:3b"

def test_find_model_ignores_whitespace():
    inventory = [
        {"name": "qwen2.5:3b"},
        {"name": "llama3:8b"}
    ]

    result = find_model(inventory, "  QWEN2.5:3b ")

    assert result is not None
    assert result['name'] == 'qwen2.5:3b'

def test_find_model_handles_none_inventory():
    
    result = find_model(None, "qwen2.5:3b")

    assert result is None

def test_get_model_info_returns_matching_model():
    models = [
        {
            "name": "qwen2.5:3b",
            "details": {
                "family": "qwen2",
                "parameter_size": "3B",
                "quantization_level": "Q4_K_M"
            }
        }
    ]

    result = get_model_info(models, "QWEN2.5:3B")

    assert result is not None
    assert result["name"] == "qwen2.5:3b"
    assert result["family"] == "qwen2"

def test_get_model_info_returns_none_when_model_not_found():
    models = [
        {
            "name": "qwen2.5:3b",
            "details": {
                "family": "qwen2",
                "parameter_size": "3B",
                "quantization_level": "Q4_K_M"
            }
        }
    ]

    result = get_model_info(models, "llama3:8b")

    assert result is None

def test_get_model_info_handles_none_inventory():
    result = get_model_info(None, "qwen2.5:3b")

    assert result is None