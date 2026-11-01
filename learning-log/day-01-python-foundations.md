Day 01 – Python Foundations and API Connectivity

Date: 1 November 2026
Project: AI Security Lab
Environment: Ubuntu 24.04 on WSL2, Python 3, JupyterLab

1. Learning objectives

The objective of this session was to establish Python fundamentals and begin using Python to interact with locally hosted AI services.

2. Python concepts covered

During this session, I worked with:

Variables and data types – storing and working with different types of information.

Dictionaries and lists – organising and accessing structured data.

Conditional statements – making decisions using if, elif and else.

Loops – iterating through collections of data.

Functions – organising reusable code using parameters and return values.

User input – accepting information from a user.

F-strings – formatting output dynamically.

Exception handling – handling errors using try and except.

3. Working with HTTP requests and APIs

I moved beyond basic Python exercises and started interacting with external services.

Using the Python requests library, I explored how to:

Send HTTP requests.

Connect to a local service.

Check whether a service is accessible.

Retrieve information from an API.

4. Connecting Python to Ollama

I started investigating how Python can communicate with my locally hosted Ollama instance.

I tested connectivity using different ports:

Port 11435 – connection unsuccessful.

Port 11434 – successful connection.

This helped demonstrate the importance of checking service configuration and understanding which port an application is listening on.

5. Working with JSON responses

The next step was to retrieve and inspect the JSON response from Ollama.

Endpoint:

http://172.25.48.1:11434/api/tags

Python request:

import requests

response = requests.get(
    "http://172.25.48.1:11434/api/tags"
)

data = response.json()

print(data)

The purpose of this exercise is to understand the structure of an API response and extract information programmatically.

6. What I learned

This session helped connect basic Python programming with practical applications.

Rather than only writing isolated scripts, I started using Python to communicate with an actual service running in my AI lab.

This is an important foundation for future work involving:

AI model integration.

API security.

Automated security analysis.

LLM applications.

AI security testing.

7. Next steps

The next session will focus on:

Inspecting the JSON response returned by Ollama.

Identifying the main dictionary key.

Understanding the models collection and its structure.

Extracting model names programmatically.

Using this information to build a simple Python model inventory.

Current stopping point: Understanding the JSON structure returned by Ollama's /api/tags endpoint.

This learning log records practical work completed during the AI Security Lab learning journey. Code and exercises will be expanded as the project develops.
