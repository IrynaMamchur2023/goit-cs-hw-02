import sqlite3

# Список вебсайтів для перевірки
websites = ["https://google.com", "https://facebook.com", "https://twitter.com"]

# Підключення до бази даних
conn = sqlite3.connect('websites.db')
cursor = conn.cursor()

# Додавання даних у таблицю
for site in websites:
    cursor.execute('''
    INSERT INTO websites (url, status) VALUES (?, 'UNKNOWN')
    ''', (site,))

# Збереження змін і закриття з'єднання
conn.commit()
conn.close()

print("Дані успішно додані до таблиць")