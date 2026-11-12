Python Code Review, Refactoring & Application Completion

Date: 12 November 2026
Project: AI Security Lab – Ollama Model Inventory

1. Session objectives

Complete the code review of the Ollama Model Inventory application, improve defensive programming, refactor application logic, validate the complete workflow and prepare the project for future development.

2. Topics covered

Defensive programming – find_model()

Reviewed and improved the find_model() function.

Key improvements:

Validated that the inventory is a list.

Validated that the search term is a string.

Handled None, empty strings and whitespace-only input.

Implemented case-insensitive searching.

Used .strip() and .lower() to normalise search input.

Ensured unsuccessful searches return None.

Learned why placing return None inside a loop can cause premature termination.

Function refactoring – get_model_info()

Refactored display_model_info() into get_model_info().

Key improvements:

Removed direct terminal output from the function.

Removed interactive user input from the function.

Passed the search term as a function argument.

Returned the matching model dictionary or None.

Used early returns to simplify control flow.

Relied on build_inventory() for inventory validation rather than duplicating validation logic.

Key concept: Separation of concerns. Functions should have clearly defined responsibilities.

Application entry point

Refactored the if __name__ == "__main__": section.

The application now:

Retrieves the Ollama model inventory.

Checks whether the inventory is available.

Collects the user's search term.

Calls get_model_info().

Displays the matching model information.

Handles unsuccessful searches and unavailable inventory.

Also identified and fixed a NameError caused by referencing result outside the conditional branch where it was assigned.

Automated testing

Expanded the pytest suite to cover the refactored application.

New tests covered:

Searching with leading and trailing whitespace.

Handling None inventory.

Returning None when a model is not found.

Successfully returning matching model information.

Handling unavailable inventory in get_model_info().

Practised the Red-Green-Refactor workflow:

Red: Write a test that exposes a problem.

Green: Modify the implementation to pass.

Refactor: Improve the implementation while preserving behaviour.

3. Testing results

Final automated test result: 33 passed in 0.16 seconds.

32 unit tests.

1 live Ollama integration test.

0 failures.

Manual application testing

Successfully verified:

Scenario

Result

Search for qwen2.5:3b

Passed

Search for nonexistent model

Passed

Search with different capitalisation

Passed

Search with leading/trailing spaces

Passed

Ollama unavailable

Passed

Application handles unavailable inventory without crashing

Passed

The application successfully retrieved:

Name: qwen2.5:3b

Family: qwen2

Parameters: 3.1B

Quantisation: Q4_K_M

4. Git and GitHub

Reviewed Git repository management.

Practised:

Checking the current working directory.

Using git status.

Understanding tracked versus untracked files.

Reviewing .gitignore.

Selectively staging application files, tests and configuration.

Verifying repository synchronisation with origin/main.

The application files, test suite and pytest.ini were included in the Git workflow. Jupyter notebooks were deliberately left untracked for later review.

5. Important concepts learned

Python exception handling and defensive programming.

Input validation and data normalisation.

Function parameters and return values.

Early returns and conditional execution.

Separation of concerns.

Avoiding duplicated validation.

Unit testing versus integration testing.

Red-Green-Refactor.

Debugging NameError and TypeError.

Git staging, commits and repository synchronisation.

6. Current project status

The Ollama Model Inventory application is operational and has passed all 33 automated tests.

The application can communicate with the local Ollama API, process model metadata, search the inventory and handle unavailable services gracefully.

7. Next session – Configuration Management & Application Quality

Planned activities:

Move the hardcoded Ollama API address into a .env configuration file.

Use python-dotenv to load environment variables.

Implement configuration validation and sensible defaults.

Introduce Python's logging module instead of relying entirely on print().

Review the overall project structure.

Update and test the application.

Review the GitHub repository and documentation.

Longer-term objective: Prepare the application architecture for more advanced AI security projects, including LLM security testing, RAG security and AI agent security.
