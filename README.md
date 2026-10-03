# Security Log Analyzer API

## Overview
This repository contains a RESTful API built with Python and FastAPI, designed to parse server logs, identify potential brute-force attacks (such as failed login attempts), and securely store the threat data into a local SQLite database. Originally a CLI tool, it has been refactored into a fully modular web API.

## Project Goals
This project was developed as a hands-on training exercise to practice foundational software engineering and cybersecurity skills. 

Key learning areas include:
* Python fundamentals and modular architecture (Clean Code).
* API development and routing using **FastAPI**.
* Automated testing and quality assurance using **pytest**.
* Data extraction and pattern matching using Regular Expressions (Regex).
* Relational database creation and manipulation using SQLite3.
* Secure SQL practices (using parameterized queries to prevent SQL Injection).

## Repository Structure
* `api.py`: The main application acting as the gateway for all HTTP routes.
* `main.py`: Contains the logic to read logs, filter malicious events using Regex, and insert them into the database.
* `blocklist_generator.py`: Queries the database to identify top attackers and generates a `firewall_rules.txt` file.
* `viewer.py`: Queries the database and formats the threat reports into structured JSON data.
* `test_api.py`: Automated test suite ensuring the reliability of all API endpoints.
* `server_logs.txt`: A sample log file simulating a web server environment for testing purposes.
* `.gitignore`: Configured to ignore `.db` files, `.pytest_cache`, and `__pycache__` for security and clean version control.

## Requirements
To run this API, you will need to install the following Python libraries:

    pip install fastapi uvicorn pytest httpx

## How to Run
1. Clone this repository to your local machine.
2. Open your terminal in the project folder and install the requirements.
3. Start the API server using Uvicorn:

       uvicorn api:app --reload

4. Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive Swagger UI.
5. Test the routes directly from the browser to analyze logs, generate blocklists, and view attackers.

## How to Run Tests
To execute the automated test suite and verify the API's integrity, ensure the terminal is available and run:

    pytest