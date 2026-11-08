Learning Log — 5 November 2026
Defensive Programming & API Response Validation

1. Session objectives

The focus today was improving the reliability of the Python application by validating external API responses and handling unexpected data safely.

We continued developing the Ollama Model Inventory application.

2. What I learned

API response validation

Learned why HTTP 200 does not guarantee valid application data.

Validated that API responses are dictionaries using isinstance().

Used .get() to safely retrieve dictionary values.

Validated that the models field contains a list.

Learned how to handle missing API fields and unexpected data types.

JSON error handling

Learned about requests.exceptions.JSONDecodeError.

Added exception handling for malformed JSON responses.

Used mocking to simulate invalid API responses.

Defensive programming

Validated individual model records before processing them.

Checked that each model entry is a dictionary.

Checked that model names are strings.

Checked that the details field is a dictionary.

Ensured malformed records are skipped rather than crashing the application.

Testing

Continued using pytest and unittest.mock.

Updated tests to verify improved application behaviour.

Tested malformed records alongside valid records.

Reinforced the difference between testing expected exceptions and testing graceful error handling.

3. Application improvements

Updated:

src/model_inventory.py

Added validation for:

Invalid API response structures.

Missing models key.

Incorrect models data type.

Malformed JSON.

Invalid individual model entries.

Invalid details data types.

Invalid model name data types.

4. Automated testing results

<badge color="success">17 tests passing</badge>

Command used:

python -m pytest -v

Test category

Tests

Inventory processing and validation

7

Model searching

4

API integration and error handling

6

Total

17

All 17 tests passed successfully.

5. Important lessons

Never automatically trust data received from external services.

Validate both the structure and data types of API responses.

A field existing does not mean its value is valid.

One malformed record should not necessarily prevent processing valid records.

Good tests verify both successful operations and failure scenarios.

Reviewing application code is just as important as checking whether tests pass.

6. Next session – Planned activities

Continue hardening the Ollama Model Inventory application:

Reject empty and whitespace-only model names.

Test additional malformed model details.

Review input validation in find_model().

Refactor and clean up the application.

Run the complete test suite.

Update the learning log and GitHub repository.

7. Personal reflection

Today I progressed from testing individual Python functions to thinking more like a software developer responsible for application reliability.

I learned how to validate external data at multiple levels and how to use automated tests to identify weaknesses before they become application failures.

These skills are directly relevant to building secure AI applications, particularly applications that consume external APIs, process model outputs and interact with potentially untrusted data.

Next milestone: Complete the hardening of the Ollama Model Inventory application before moving on to practical AI security projects.
