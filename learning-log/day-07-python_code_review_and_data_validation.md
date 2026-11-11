Session 14 – Python Code Review, Defensive Programming & Data Validation

Date: 11 November 2026
Project: AI Security Lab
Application: Ollama Model Inventory
Environment: Python 3.12, Ubuntu 24.04 (WSL2), VS Code, Ollama, pytest

1. Session objectives

Today's objectives were to:

Conduct a structured code review of the Model Inventory application.

Understand API communication and exception handling.

Improve defensive programming.

Identify and handle invalid input types.

Introduce semantic validation and data normalisation.

Expand automated test coverage.

2. Reviewing API communication and exception handling

Reviewed the get_model_inventory() function.

Revisited the following concepts:

HTTP GET requests using the Requests library.

Request timeouts and why they are important.

HTTP response status codes.

response.raise_for_status().

JSON parsing and response validation.

Handling connection failures, timeouts and HTTP errors.

Studied the difference between:

Exception

Meaning

ConnectionError

Unable to establish a connection.

Timeout

A connection or response operation takes too long.

HTTPError

The server returns an unsuccessful HTTP status.

RequestException

Base exception for Requests-related errors.

Added a general RequestException handler after the more specific exception handlers.

Key concept learned: Exception inheritance.

Python evaluates exception handlers from top to bottom. Specific exceptions should be handled before their parent exception classes.

3. Separation of concerns

Discussed whether get_model_inventory() should print error messages directly or return error information to the calling application.

Identified that returning error information is generally preferable for reusable application components.

Different applications may need different error-handling behaviour:

CLI applications can print error messages.

Web dashboards can display notifications.

APIs can return appropriate HTTP error responses.

Key concept learned: Separation of concerns.

A function should focus on its primary responsibility rather than controlling how another application presents information.

This is particularly relevant when developing reusable cybersecurity tools.

4. Defensive programming – get_string_or_unknown()

Identified a potential weakness in the helper function.

The original implementation could raise an AttributeError if details was None.

Improved the function by validating the input type before calling .get().

Updated implementation:

def get_string_or_unknown(details, key):
    if isinstance(details, dict):
        value = details.get(key)
    else:
        return "Unknown"

    if isinstance(value, str):
        return value

    return "Unknown"

Added a new test:

test_get_string_or_unknown_invalid_details_type

Key concepts learned:

Type validation using isinstance().

Early returns.

Preventing unexpected runtime exceptions.

Negative testing.

5. Defensive programming – build_inventory()

Identified that passing None or another non-list object to build_inventory() would raise a TypeError when Python attempted to iterate over the input.

Added input validation to ensure that models is a list.

Invalid inputs now return an empty list:

def build_inventory(models):
    if not isinstance(models, list):
        return []

    inventory = []
    # Remaining processing logic

Added two tests:

test_build_inventory_handles_none_input

test_build_inventory_handles_invalid_input_type

Key concept learned: Type consistency.

Functions are easier to use and maintain when they return predictable data types.

For this function, returning an empty list is more appropriate than returning a string or None, because its purpose is to produce an inventory list.

6. Semantic validation

Identified another weakness in model validation.

Previously, the application checked whether the model name was a string, but an empty string or whitespace-only string would still pass.

Strengthened validation using:

isinstance(model.get("name"), str) and model.get("name").strip()

Added two tests:

test_build_inventory_handles_empty_model_name

test_build_inventory_handles_white_space_model_name

Key concept learned: Semantic validation.

Correct data types do not necessarily mean that data is meaningful or usable.

For example, an empty model name is technically a string but is not a valid model identifier for our inventory.

7. Data normalisation

Improved the inventory transformation logic to remove leading and trailing whitespace from model names.

Updated the stored name:

"name": model['name'].strip()

Added:

test_build_inventory_strips_model_name_whitespace

Verified that "   qwen2.5:3b   " is stored as "qwen2.5:3b".

Key concept learned: Data normalisation.

External data should be validated and cleaned before being stored or processed.

This is especially relevant when working with security telemetry, API responses and data from multiple sources.

8. Automated testing results

Expanded the existing pytest suite from 22 to 28 tests.

Test category

Result

Unit tests

27 passed

Integration tests

1 passed

Total

28 passed

Failures

0

All tests completed successfully.

9. Key learning outcomes

Practical experience gained today:

HTTP communication and exception handling.

Python exception inheritance.

Separation of concerns.

Defensive programming.

Input type validation.

Early returns.

Semantic validation.

Data normalisation.

Negative test cases.

Expanding automated test coverage.

An important takeaway was that an application can work correctly with normal API responses while still containing weaknesses when unexpected data is received.

Systematically identifying and testing these edge cases makes applications more reliable.

10. Next session – Completing the code review

The next session will continue with the find_model() function.

Planned activities:

Review find_model() and its input validation.

Test invalid search inputs, including None.

Review display_model_info() and user interaction.

Examine the overall application structure.

Review the complete test suite for additional gaps.

Identify final improvements before preparing the portfolio milestone.

Session status: Completed successfully.

Current milestone: Ollama Model Inventory – 28 passing automated tests, including one integration test.
