async def makemoney(message, cursor):
    cursor.execute(f"SELECT * FROM users WHERE id = {message.author.id}")
    result = cursor.fetchall()
    if (len(result)==0):
        cursor.execute(f"INSERT INTO users (id, coins) VALUES ({message.author.id}, 0)")
    else:
        cursor.execute(f"SELECT coins FROM users WHERE id = {message.author.id}")
        result = cursor.fetchone()
        coin = int(result[0])+1
        cursor.execute(f"UPDATE users SET coins = {coin} WHERE id = {message.author.id}")