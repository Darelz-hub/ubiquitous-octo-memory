import sqlite3

# Соединение с базой данных
conn = sqlite3.connect('coffeeshop.db')
c = conn.cursor()
# Создание таблицы "products"
c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price INTEGER NOT NULL
    )
''')
# Добавление товаров в базу данных
c.execute("INSERT INTO products (name, quantity, price) VALUES ('лате', 200, 200)")
c.execute("INSERT INTO products (name, quantity, price) VALUES ('капучино', 250, 250)")
c.execute("INSERT INTO products (name, quantity, price) VALUES ('круасан', 100, 100)")
c.execute("INSERT INTO products (name, quantity, price) VALUES ('пончик', 150, 150)")

# Добавление нового товара
c.execute("INSERT INTO products (name, quantity, price) VALUES ('эспрессо', 180, 180)")

# Удаление товара по id
product_id = 1
c.execute("DELETE FROM products WHERE id = ?", (product_id,))

# Редактирование имя и количество товара по id
product_id = 2
new_name = "Капучино XL"
new_quantity = 300
c.execute("UPDATE products SET name = ?, quantity = ? WHERE id = ?", (new_name, new_quantity, product_id))
