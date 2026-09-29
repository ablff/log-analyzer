import sqlite3

connection = sqlite3.connect("security_logs.db")
cursor = connection.cursor()

target_ip = '45.33.22.11'

cursor.execute('''
    SELECT timestamp, event_detail
    FROM incidents
    WHERE source_ip = ?
''', (target_ip,))
records = cursor.fetchall()

print(f"\n--- THREAT REPORT FOR IP: {target_ip} ---\n")

for record in records:
    event_time = record[0]
    event_desc = record[1]
    print(f"[{event_time}] -> Alert: {event_desc}")

connection.close()