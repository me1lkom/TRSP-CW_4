import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()

sql_command = """insert into product (title, price, count) values (?, ?, ?) """

data1 = ('Арбуз', 100, 3)
data2 = ('Клубника', 500, 10)

cursor.execute(sql_command, data1)
cursor.execute(sql_command, data2)

conn.commit()
conn.close()