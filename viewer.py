import sqlite3

connection = sqlite3.connect("security_logs.db")
cursor = connection.cursor()

cursor.execute('''
    SELECT source_ip, COUNT (*) as total_attacks
    FROM incidents
    WHERE severity = "HIGH"
    GROUP BY source_ip
    ORDER BY total_attacks DESC
''')
records = cursor.fetchall()

print("\n--- TOP ATTACKERS SUMMARY ---\n")

for record in records:
    ip_address = record[0]
    attack_count = record[1]
    print(f"\nMalicious IP: {ip_address} | Total Failed Logins: {attack_count}\n")

connection.close()