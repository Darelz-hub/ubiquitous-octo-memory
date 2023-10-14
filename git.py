import sqlite3
def add_shit(cur):
    shift = input('смена (дневная/вечерняя): ')
    date_year, date_month, date_day = input('год: '), input(' месяц: '), input('  день: ')
    revenue = int(input('выручка: '))
    id_e = int(input('id сотрудника: '))
    cur.execute(f"""
                INSERT INTO work_shift (shift, date_year, date_month, date_day, revenue, id_e) VALUES (
                '{shift}', {date_year}, {date_month}, {date_day}, '{revenue}', '{id_e}'
                );
                """)

def show_shift(cur):
    result = cur.execute("SELECT * FROM work_shift;")
    for row in result.fetchall():
        print(f"{row[0]}) {row[1]} ({row[2]}-{row[3]}-{row[4]}), $: {row[5]}, id: {row[6]}")

def change_shift(cur):
    result = cur.execute("SELECT * FROM work_shift;")
    for row in result.fetchall():
        print(row)
    choose_3 = input('''    Изменить:
    1 - выручку за смену
    2 - сотрудника на смене
>> ''')
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
def menu():
        
        
    with sqlite3.connect("coffee_house.db") as conn:
        cur = conn.cursor()
        cur.executescript("""
            CREATE TABLE IF NOT EXISTS work_shift (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            shift TEXT, /*смена: дневная, вечерняя*/
            date_year TEXT, /*YYYY*/
            date_month TEXT, /*MM*/
            date_day TEXT, /*DD*/
            revenue INTEGER, /*выручка*/
            id_e INTEGER,
            FOREIGN KEY (id_e) REFERENCES employees(id)
            );
        """)


        while True:
                choose_main = input("""\nМеню смены:
        1 - добавить
        2 - просмотр
        3 - редактировать
        4 - отмена
    >> """)

                #отмена/выход в главное меню
                if choose_main == '4':
                    break

                # добавить
                elif choose_main == '1':
                    add_shit(cur)

                # посмотреть
                elif choose_main == '2':
                    show_shift(cur)

                # изменить
                elif choose_main == '3':
                    change_shift(cur)




