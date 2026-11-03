AI Security Learning Log — 3 November 2026

Session focus

Python application development, API data validation, exception handling and modular programming.

1. Model inventory application

Continued development of src/model_inventory.py, building on the previous session's Ollama API integration.

Implemented and tested four functions:

get_model_inventory() — retrieves model information from the Ollama API.

build_inventory() — transforms raw API responses into simplified dictionaries.

find_model() — searches installed models by name.

display_model_info() — handles user input and displays model information.

2. Python concepts practised

Case-insensitive searching

Used .lower() to normalise user input and stored model names.

Tested uppercase and lowercase model searches.

Exception handling

Implemented handling for:

requests.exceptions.ConnectionError

requests.exceptions.Timeout

requests.exceptions.HTTPError

Added explicit return None statements for failed API requests.

Successfully tested application behaviour with Ollama unavailable.

Dictionary handling and defensive programming

Learned how KeyError occurs when accessing missing dictionary keys.

Practised the dictionary .get() method with default values.

Used the in operator to check whether dictionary keys exist.

Distinguished between required and optional data fields.

Loop control

Introduced continue to skip incomplete model entries without terminating the entire function.

Python modules and imports

Learned the difference between executing a Python script and importing a function.

Discovered that importing a module executes its top-level statements.

Learned about the special __name__ variable and the __main__ convention.

3. Practical testing

Created an artificial dataset containing three model entries:

Complete model (model-one).

Incomplete model (missing name).

Complete model (model-three).

Successfully verified that:

The first model was processed.

The incomplete model was skipped.

Processing continued and the third model was included.

4. Current project status

model_inventory.py successfully retrieves, transforms, searches and displays Ollama model information.

The application handles connection failures and several forms of incomplete data.

5. Next session — planned activities

Implement and test if __name__ == "__main__":.

Verify that importing functions no longer starts the application.

Improve validation of required nested dictionary fields.

Introduce more structured error handling.

Review the complete application and refactor where appropriate.

Run regression tests.

Commit the updated project to GitHub.

Key takeaway

Today's focus was moving beyond basic Python syntax towards writing modular, reusable and defensive applications.

These skills will form the foundation for future AI security projects involving API integrations, RAG systems, security testing and automated detection tools.
