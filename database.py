import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sujal@123",
    database="soc_project"
)

cursor = connection.cursor()

with open("sample_logs.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        log_time = parts[0] + " " + parts[1]
        status = parts[2]
        username = parts[3].split("=")[1]
        ip = parts[4].split("=")[1]

        query = """
        INSERT INTO logs (log_time, username, ip_address, status)
        VALUES (%s, %s, %s, %s)
        """

        values = (log_time, username, ip, status)

        cursor.execute(query, values)

connection.commit()

print("✅ Logs inserted successfully!")

cursor.close()
connection.close()