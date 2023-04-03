import json
import mysql.connector

myconn = None
with open('DB.json') as f:
        data = json.load(f)
        myconn = mysql.connector.connect(host = data["endpoint"],
                                         port = data["port"],
                                         user = data["username"],
                                         password = data["password"],
                                         database = data["database"])
        cursor = myconn.cursor()
        #cursor.execute("CREATE TABLE users (id INT PRIMARY KEY NOT NULL, coins INT NOT NULL)")
        #cursor.execute("CREATE TABLE users (id VARCHAR(255) PRIMARY KEY NOT NULL, coins INT NOT NULL)")
        cursor.execute(f"UPDATE users SET coins = 250 WHERE id = '301978946508161025'")
        myconn.commit()