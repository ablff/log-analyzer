import sqlite3
import re

connection = sqlite3.connect('security_logs.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        source_ip TEXT,
        event_detail TEXT,
        severity TEXT
        )
        ''')
connection.commit()

Log_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - IP: ([\d\.]+) - (.*)"
with open("server_logs.txt", "r") as file:
    for line in file:
        match = re.search(Log_pattern, line)
        if match:
            timestamp = match.group(1)
            source_ip = match.group(2)
            event_detail = match.group(3)
            severity = "HIGH" if "LOGIN_FAILED" in event_detail else "LOW"
            if severity == "HIGH":
                cursor.execute('''
                    INSERT INTO incidents (timestamp, source_ip, event_detail, severity)
                    VALUES (?, ?, ?, ?)
                    ''', (timestamp, source_ip, event_detail, severity))

connection.commit()
connection.close()

print("Analysis complete! High severity incidents saved to the database.")
