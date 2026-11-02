Learning Log – 2 November 2026

Today's focus

Transitioning from JupyterLab experiments to developing standalone Python applications in VS Code.

1. Python development environment

Connected Visual Studio Code to Ubuntu 24.04 through WSL.

Installed and verified Microsoft's Python and Pylance extensions.

Selected the existing project virtual environment.

Verified Python 3.12.3.

Confirmed interpreter path:
/home/wojtek/ai-security-lab/.venv/bin/python

2. First standalone Python application

Created:

src/model_inventory.py

Successfully implemented and tested:

HTTP communication with the Ollama API.

API response handling using requests.

JSON parsing.

Connection error, timeout and HTTP error handling.

Retrieving installed models from /api/tags.

Successful execution:

Successfully retrieved 1 models.
qwen2.5:3b

3. Application architecture

Started separating functionality into reusable functions.

get_model_inventory() – retrieves models from Ollama.

build_inventory(models) – transforms model metadata into a structured list of dictionaries. Function written, execution test pending.

Previously developed and tested:

find_model()

display_model_info()

check_model()

4. Concepts reinforced

Python functions and modular programming.

Function composition.

Lists of dictionaries.

Nested data structures.

API communication and JSON.

Exception handling.

Separation of concerns.

Python virtual environments.

VS Code and WSL development workflow.

Current progress

Completed: VS Code configuration, interpreter verification and Ollama API integration.

In progress: Standalone AI Model Inventory Checker.

Next session – Planned tasks

Finish implementing and testing build_inventory().

Integrate find_model() into the standalone application.

Add display_model_info() and check_model().

Make the application interactive using input().

Test successful searches, missing models and API failures.

Review the code and prepare the first Git commit.

Longer-term direction

Continue building practical Python skills towards AI security engineering, including automated model testing, prompt injection detection, secure RAG and AI agent security.

Current milestone: First standalone Python application successfully communicates with the local Ollama model environment.
