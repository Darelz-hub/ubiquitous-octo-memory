import sqlite3
def add_product(c):
    name = input("Введите наименование товара: ")
    quantity = int(input("Введите количество товара: "))
    price = int(input("Введите стоимость одной единицы товара: "))
    # conn = sqlite3.connect('coffeeshop.db')
    # c = conn.cursor()
    c.execute('''
        INSERT INTO products (name, quantity, price)
        VALUES (?, ?, ?)
    ''', (name, quantity, price))
    print("Товар успешно добавлен!")

# Редактирование товаров
def edit_product(c):
    product_id = int(input("Введите id товара для редактирования: "))
    name = input("Введите новое наименование товара: ")
    quantity = int(input("Введите новое количество товара: "))
    price = float(input("Введите новую стоимость одной единицы товара: "))
    # conn = sqlite3.connect('coffeeshop.db')
    # c = conn.cursor()
    c.execute('''
        UPDATE products
        SET name = ?, quantity = ?, price = ?
        WHERE id = ?
    ''', (name, quantity, price, product_id))
    print("Товар успешно отредактирован!")

# Удаление товаров
def delete_product(c):
    product_id = int(input("Введите id товара для удаления: "))
    # conn = sqlite3.connect('coffeeshop.db')
    # c = conn.cursor()
    c.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id))
    print("Товар удален!")

# Просмотр товаров
def view_products(c):
    # conn = sqlite3.connect('coffeeshop.db')
    # c = conn.cursor()
    result = c.execute('''
        SELECT * FROM products
    ''')
    print("Список товаров:")
    for row in result.fetchall():
        print (row)
# Соединение с базой данных

# # Добавление товаров в базу данных
# c.execute("INSERT INTO products (name, quantity, price) VALUES ('лате', 200, 200)")
# c.execute("INSERT INTO products (name, quantity, price) VALUES ('капучино', 250, 250)")
# c.execute("INSERT INTO products (name, quantity, price) VALUES ('круасан', 100, 100)")
# c.execute("INSERT INTO products (name, quantity, price) VALUES ('пончик', 150, 150)")

# # Добавление нового товара
# c.execute("INSERT INTO products (name, quantity, price) VALUES ('эспрессо', 180, 180)")

# # Удаление товара по id
# product_id = 1
# c.execute("DELETE FROM products WHERE id = ?", (product_id,))

# # Редактирование имя и количество товара по id
# product_id = 2
# new_name = "Капучино XL"
# new_quantity = 300
# c.execute("UPDATE products SET name = ?, quantity = ? WHERE id = ?", (new_name, new_quantity, product_id))

# Выбор функции
    
def choice_f():
    with sqlite3.connect("coffee_house.db") as conn:
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
        while True:
            print("""Доступные действия: 
            1. Добавить товар
            2. Редактировать товар
            3. Удалить товар
            4. Просмотреть все товары
            5. Выйти
                """)
            choice = input("Выберите номер функции: ")
            if choice == '1':
                add_product(c)
            elif choice == '2':
                edit_product(c)
            elif choice == '3':
                delete_product(c)
            elif choice == '4':
                view_products(c)
            elif choice == '5':
                break
            else:
                print("Неверный выбор функции")

# Добавление товара


