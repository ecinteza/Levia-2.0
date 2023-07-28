import mysql.connector
import json

async def makemoney(message, bot):
    try:

        f = open('./json/DB.json')
        data = json.load(f)
        myconn = mysql.connector.connect(host = data["endpoint"],
                                        port = data["port"],
                                        user = data["username"],
                                        password = data["password"],
                                        database = data["database"])
        cursor = myconn.cursor()

        cursor.execute(f"SELECT * FROM users WHERE id = {message.author.id}")
        result = cursor.fetchall()
        if (len(result)==0):
            cursor.execute(f"INSERT INTO users (id, coins) VALUES ({message.author.id}, 0)")
        else:
            cursor.execute(f"SELECT coins FROM users WHERE id = {message.author.id}")
            result = cursor.fetchone()
            coin = int(result[0])+1
            cursor.execute(f"UPDATE users SET coins = {coin} WHERE id = {message.author.id}")

        myconn.commit()
        cursor.close()
        myconn.close()
        f.close()
    except:
        await bot.get_channel(565602349679378433).send(f"<@255432828668477441> Database Disconnected.")