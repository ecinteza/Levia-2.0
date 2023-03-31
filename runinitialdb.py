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
cursor.execute("CREATE TABLE users (id INT PRIMARY KEY NOT NULL, coins INT NOT NULL)")