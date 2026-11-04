Learning Log — 4 November 2026

Session focus

Python testing, pytest fixtures, mocking and API error handling

1. What I learned

Pytest fixtures

Used @pytest.fixture to create reusable test data.

Learned how pytest automatically injects fixtures into test functions.

Reduced duplicated data across tests.

Mocking

Introduced unittest.mock.

Learned how Mock() creates simulated objects.

Learned how @patch() temporarily replaces real functions during testing.

Used return_value to simulate successful API responses.

Used side_effect to simulate exceptions.

API testing

Tested get_model_inventory() without requiring a real Ollama connection.

Verified that the correct API endpoint is called exactly once.

Verified that the request uses a five-second timeout.

Learned the difference between a successful HTTP response and valid application data.

Exception handling
Practised testing four API scenarios:

Successful API response.

Connection error.

Request timeout.

HTTP error (simulated HTTP 500).

Python concepts

assert result is None versus assert result == [].

pytest.raises() for testing expected exceptions.

mock_get.assert_called_once_with() for verifying function calls.

Difference between return_value and side_effect.

2. Current project status

Project: ai-security-lab

Application: src/model_inventory.py

Test file: tests/test_model_inventory.py

Test results: 11 PASSED

Test category

Tests

Model inventory processing

3

Model searching

4

Ollama API integration

4

Total

11

All tests passed successfully using:

python -m pytest -v

3. Important lessons

A successful HTTP status does not guarantee valid application data.

An empty list and None represent different application states.

Mocking allows external dependencies to be tested without actually contacting them.

Good tests should verify both returned results and expected application behaviour.

External API data should be validated rather than automatically trusted.

4. Next session

Continue testing the Ollama API integration.

Planned tasks:

Test malformed API responses, including a missing models key.

Review how the application handles unexpected JSON.

Improve defensive handling of malformed responses.

Add further tests for API response validation.

Review and refactor the application where appropriate.

5. Personal reflection

Today I moved beyond testing simple Python functions and started testing an application that communicates with an external API.

I now have a better understanding of how mocking works and how to simulate both successful responses and failures.

This is an important foundation for developing reliable AI security tools and applications that interact with external services.

Next milestone: Build a more robust, fully tested Ollama model inventory application.
