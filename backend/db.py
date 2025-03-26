import sqlite3

con = sqlite3.connect("jarvis.db") 
cursor = con.cursor()

#for system commands and path
query = "CREATE TABLE IF NOT EXISTS sys_command(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'pychamp', 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3.1\\bin\\pycharm64.exe')"
cursor.execute(query)
con.commit()

#for web commands and links
query = "CREATE TABLE IF NOT EXISTS web_command(id INTEGER PRIMARY KEY AUTOINCREMENT,name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command (name, url) VALUES ('binance', 'https://www.binance.com/en/my/dashboard')"
# cursor.execute(query)
# con.commit()

#delete specific row
# query = "DELETE FROM web_command WHERE name = 'gmail'"
# cursor.execute(query)
# con.commit()

#delete all rows
# query = "DELETE FROM web_command"
# cursor.execute(query)
# con.commit()
 
