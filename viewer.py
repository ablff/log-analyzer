import sqlite3

def viewer_web():
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

    connection.close()
    
    formatted_data = []

    for record in records:
        attacker_info = {
            "ip_address": record[0],
            "attack_count": record[1]
        }
        formatted_data.append(attacker_info)
    return {"status" : "success","message": formatted_data}


if __name__ == "__main__":
    result = viewer_web()
    print(result)