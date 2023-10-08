import sqlite3

with sqlite3.connect("coffee.db") as con:
    cur = con.cursor()
    cur.executescript("""
        CREATE TABLE IF NOT EXISTS work_shift (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        shift NVARCHAR, /*смена: дневная, вечерняя*/
        date DATE, /*YYYY-MM-DD*/
        revenue INTEGER, /*выручка*/
        id_e INTEGER,
        FOREIGN KEY (id_e) REFERENCES employees(id)
        );
    """)

    while True:
        choose = input("""Меню смены:
    1 - добавить
    2 - редактировать
    3 - просмотр
    4 - отмена
""")
        # добавить
        if choose == '1':
            shift = input('смена (дневная/вечерняя): ')
            date = input('дата (ГГГГ-ММ-ДД): ')
            revenue = int(input('выручка: '))
            id_e = int(input('id сотрудника: '))
            cur.execute(f"""
                        INSERT INTO Poisons (name, price, items_to_create) VALUES (
                        '{}', {}, '{}'
                        );
                        """)
        # посмотреть
        result = cur.execute("SELECT * FROM Poisons;")
        for row in result.fetchall():
            print(row)



        # изменить
        cur.execute(f"""
                    UPDATE Poisons SET items_to_create='{new_items_to_create}' WHERE id={id_change};
                    """)