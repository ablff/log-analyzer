# Security Log Analyzer

## Overview
This repository contains a Python-based security tool designed to parse server logs, identify potential brute-force attacks (such as failed login attempts), and securely store the threat data into a local SQLite database.

## Project Goals
This project was developed as a hands-on training exercise. The primary objective is to practice and consolidate foundational software engineering and cybersecurity skills. 

Key learning areas include:
* Python fundamentals and file handling operations.
* Data extraction and pattern matching using Regular Expressions (Regex).
* Relational database creation and manipulation using SQLite3.
* Secure SQL practices (using parameterized queries to prevent SQL Injection).
* SQL data filtering and aggregation.

## Repository Structure
* `main.py`: The core script that reads the log file, filters "LOGIN_FAILED" events using Regex, and inserts the malicious events into the database.
* `viewer.py`: A reporting script that queries the database to display specific alerts and generate statistical summaries (e.g., top attackers).
* `server_logs.txt`: A sample log file simulating a web server environment for testing purposes.
* `.gitignore`: Configured to ignore `.db` files, ensuring that the actual database is not uploaded to the repository for security reasons.

## How to Run
1. Clone this repository to your local machine.
2. Ensure you have Python installed. No external libraries are required (both `sqlite3` and `re` are native to Python).
3. Open your terminal in the project folder and run `python main.py` to process the logs and generate the database.
4. Run `python viewer.py` to query the database and visualize the threat reports.