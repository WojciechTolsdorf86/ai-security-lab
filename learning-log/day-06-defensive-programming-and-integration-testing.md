Learning Log - 8th November 2026
Defensive Programming, Automated Testing & Integration Testing
Project: AI Security Lab
Application: Ollama Model Inventory
Environment: Python 3.12, Ubuntu 24.04 (WSL2), Ollama, pytest

1. Session objectives

Today's objectives were to:

Improve defensive programming in the Model Inventory application.

Validate API response data and handle unexpected data types.

Refactor repeated validation logic into a reusable helper function.

Expand automated unit test coverage.

Introduce integration testing using pytest markers.

Understand the difference between unit, integration and end-to-end testing.

2. Defensive programming and data validation

Continued improving the build_inventory() function to handle malformed API data.

Previously, optional model metadata fields could contain unexpected values. Using .get() with a default value only handles missing dictionary keys; it does not handle keys containing invalid values.

Implemented additional validation using:

isinstance(value, str)

This ensures that optional metadata fields contain strings before being added to the inventory.

Invalid or missing values are replaced with "Unknown".

Fields validated:

family

parameter_size

quantization_level

3. Code refactoring – DRY principle

Identified repeated validation logic and refactored it into a reusable helper function:

def get_string_or_unknown(details, key):
    value = details.get(key)

    if isinstance(value, str):
        return value

    return "Unknown"

Updated build_inventory() to reuse this function.

Key concept learned:

DRY – Don't Repeat Yourself.

Rather than repeating the same validation logic, a reusable function handles the operation consistently.

This improves readability, maintainability and reduces duplicated code.

4. Automated unit testing

Expanded the existing pytest suite.

Added three dedicated tests for get_string_or_unknown():

test_get_string_or_unknown_valid_value

test_get_string_or_unknown_missing_key

test_get_string_or_unknown_invalid_type

These tests verify that the helper correctly handles valid values, missing dictionary keys and invalid data types.

Unit test results:

21 unit tests passed.

No failures.

5. Integration testing

Introduced the first automated integration test for the Model Inventory application.

Created:

@pytest.mark.integration
def test_ollama_integration():
    models = get_model_inventory()

    assert models is not None
    assert isinstance(models, list)
    assert len(models) > 0

    inventory = build_inventory(models)

    assert len(inventory) > 0

This test communicates with the actual Ollama API rather than using mocked responses.

Successfully verified that:

The Python application can connect to Ollama.

The API returns a valid model inventory.

The returned data can be processed by build_inventory().

The resulting inventory contains at least one model.

Pytest markers

Created and configured pytest.ini to register the integration marker:

[pytest]
markers =
    integration: tests requiring external services such as Ollama

Initially encountered PytestUnknownMarkWarning.

Investigated the problem and discovered that the configuration file was in the wrong directory.

Moved pytest.ini into the project root:

~/ai-security-lab/pytest.ini

Confirmed that pytest correctly loads the configuration and recognises the integration marker.

6. Testing strategy

Learned the differences between three testing approaches:

Test type

Purpose

Unit testing

Tests individual functions independently.

Integration testing

Tests whether different components work together.

End-to-end testing

Tests the complete application workflow from the user's perspective.

Established separate commands for running different test categories:

Integration tests:

python -m pytest -v -m integration

Unit tests:

python -m pytest -v -m "not integration"

This separation allows ordinary unit tests to run without depending on external services such as Ollama.

7. Final test results

<escape> </escape>

Test category

Result

Unit tests

21 passed

Integration tests

1 passed

Total

22 passed

Failures

0

Warnings

0

All tests completed successfully.

8. Key learning outcomes

By the end of this session, I gained practical experience with:

Defensive programming and input validation.

Python conditional expressions and type checking.

Reusable helper functions.

The DRY programming principle.

Writing independent unit tests.

Integration testing against a real API.

Pytest fixtures, markers and configuration.

Diagnosing test discovery and configuration problems.

Separating unit tests from integration tests.

An important lesson was that passing tests are not enough if the test suite does not adequately cover unexpected inputs and failure conditions.

9. Next session – Code review and portfolio preparation

The next session will focus on reviewing the existing Model Inventory application before adding further functionality.

Planned activities:

Review model_inventory.py function by function.

Evaluate code quality, structure and error handling.

Review the existing 22 automated tests and identify potential gaps.

Improve the project documentation.

Create a README explaining the application, architecture, installation and testing procedures.

Prepare the application for its first portfolio milestone on GitHub.

Session status: Completed successfully.

Current milestone: Ollama Model Inventory – functional application with 21 unit tests and 1 automated integration test.
