import sqlite3

conn = sqlite3.connect('websites.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM websites')
rows = cursor.fetchall()
print("Всі записи з таблиці websites:")
for row in rows:
    print(row)

cursor.execute('UPDATE websites SET status = "UP" WHERE url = "https://google.com"')
print(f"Оновлено {cursor.rowcount} запис(ів)")

cursor.execute('DELETE FROM websites WHERE url = "https://twitter.com"')
print(f"Видалено {cursor.rowcount} запис(ів)")

conn.commit()
conn.close()