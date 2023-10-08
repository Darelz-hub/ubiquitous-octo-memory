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
        choose_main = input("""Меню смены:
    1 - добавить
    2 - редактировать
    3 - просмотр
    4 - отмена
""")

        #отмена/выход в главное меню
        if choose_main == '4':
            break

        # добавить
        elif choose_main == '1':
            shift = input('смена (дневная/вечерняя): ')
            date = input('дата (ГГГГ-ММ-ДД): ')
            revenue = int(input('выручка: '))
            id_e = int(input('id сотрудника: '))
            cur.execute(f"""
                        INSERT INTO work_shift (shift, date, revenue, id_e) VALUES (
                        '{shift}', {date}, '{revenue}', '{id_e}'
                        );
                        """)

        # посмотреть
        elif choose_main == '2':
            result = cur.execute("SELECT * FROM work_shift;")
            for row in result.fetchall():
                print(row)

        # изменить
        elif choose_main == '3':
            result = cur.execute("SELECT * FROM work_shift;")
            for row in result.fetchall():
                print(row)
            choose_3 = input('''Изменить:
    1 - выручку за смену
    2 - сотрудника на смене
''')
            if choose_3 == '1':
                ids = int(input('какая смена (id): '))
                new_revenue = int(input('ввести выручку: '))
                cur.execute(f"""
                            UPDATE work_shift SET revenue='{new_revenue}' WHERE id={ids};
                            """)
            elif choose_3 == '2':
                ids = int(input('какая смена (id): '))
                new_id_e = int(input('заменить на сотрудника: '))
                cur.execute(f"""
                            UPDATE work_shift SET id_e='{new_id_e}' WHERE id={ids};
                            """)

