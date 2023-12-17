import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '02032002',
    'database': 'PROJECT'
}


conn = mysql.connector.connect(**db_config)


cursor = conn.cursor()


query = "SELECT * FROM ANIME"
cursor.execute(query)


results = cursor.fetchall()


for row in results:
    print("\n")
    print(row)
print("\n")

cursor.close()
conn.close()
