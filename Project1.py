
'''
Для каждого проекта команда должна создать удаленный репозиторий. На репозитории главная ветка должна оставаться пустой, каждый участник команды должен создать отдельную ветку


Приложение Кофейня:
●	хранить данные в БД 
1. Создать Бд
 	Таблица 1 Сотрудники:
Id
Имя Фамилия
Таблица 2 Учёт рабочего времени
Id – id смены
Выручка default null. (дальше update)
Смена (Дневная с 9 – 15. Вечерняя с 15 – 22)
Id_e (сотрудника) – employee
Дата работы
Foreign key (id_e) связан с id сотрудника из 1 таблицы
Таблица 3 Товары
	Id id -товара
Наименование товара
Количество
Стоимость
	Таблица 4 Учёт продаж
		Id_s (shift)-смена
		Id_p product –продукт
		Foreign key (id_s) referenses (id) 4 таблица связана со 2 таблицей
		Foreig key (id_p) references (id) 4 таблица связана с 3 таблицей

'''
#----------------------------------------------------Функции----------------------------------------

def show_table_employees():
    result = cur.execute('''
                select * from employees
                ''')
    for row in result.fetchall():
        print(row)

def add_people_on_table_employees():
    listEmployess = [input('Введите имя сотрудника '), input('Введите Фамилию сотрудника ')]
    cur.execute(f'insert into employees(name,cname) values ("{listEmployess[0]}","{listEmployess[1]}"); ')
    result = cur.execute(f"""
            SELECT name, cname FROM employees WHERE name = '{listEmployess[0]}' and cname = ' {listEmployess[1]}'
                """)
    print(result.fetchone())

def update_people_on_table_employees():
    print('''Что вы хотите изменить?
          1. Имя
          2. Фамилия
          3. Имя и Фамилия
          4. Выход
          ''')
    people_choice = int(input('Ваш выбор '))
    
    if people_choice == 1:
        show_table_employees()
        id = int(input('Введите id сотрудника, которому хотите изменить имя '))
        name = input('Введите новое имя ')
        cur.execute(f'''
                    update employees set name =  "{name}"  where id = "{id}";         
                    ''')
        result = cur.execute(f'select * from employees where id = "{id}" ')
        print(result.fetchone())
    elif people_choice == 2:
        show_table_employees()
        id = int(input('Введите id сотрудника, которому хотите изменить фамилию'))
        сname = input('Введите новую фамилию ')
        cur.execute(f'''
                    update employees set cname = \' {сname} \' where employees.id = "{id}"         
                    ''')
        result = cur.execute('select * from employees where id = "{id}" ')
        print(result.fetchone())
    elif people_choice == 3:
        show_table_employees()
        id = int(input('Введите id сотрудника, которому хотите изменить фамилию'))
        name, сname = input('Введите новое имя '), input('Введите новую фамилию ')
        cur.execute(f'''
                    update employees set cname = \' {сname} \' , name = \' {name} \' where employees.id = "{id}"         
                    ''')
        result = cur.execute('select * from employees where id = "{id}" ')
        print(result.fetchone())
    elif people_choice == 4:
        return False
    
def delete_people_on_table_employees():
    show_table_employees()
    id = int(input('Введите id сотрудника, которого хотите удалить '))
    cur.execute(f'delete from employees where employees.id == "{id}" ')
    show_table_employees()
    
def show_table_sales_accounting():
    result = cur.execute('select * from sales_accounting, work_shift, products where sales_accounting.id_s = work_shift.id and sales_accounting.id_p = product.id')
    for row in result.fetchall():
        print(row)

def add_id_s_and_id_p_in_table_sales_accounting():
    id_product = int(input('Введите id продукта, который хотите добавить '))
    id_shift = int(input('Введите id смены, которую хотите добавить '))
    cur.execute('insert into  sales_accounting(id_p, id_s) values(?,?)', (id_product, id_shift))
#-------------------------------------------------------------------
import sqlite3 as sq
with sq.connect('coffee_house.db') as con:
    cur = con.cursor()
    cur.executescript('''
                      
                    Create table if not exists employees(
                        id integer not null primary key autoincrement ,
                        name text,
                        cname text
                    );
                    
                    CREATE TABLE IF NOT EXISTS work_shift (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
                        shift text, 
                        date DATE, /* */
                        revenue INTEGER default 0, 
                        id_e INTEGER,
                        FOREIGN KEY (id_e) REFERENCES employees(id)
                    );
                    
                    CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT ,
                        name TEXT NOT NULL Unique,
                        quantity INTEGER NOT NULL,
                        price INTEGER NOT NULL
                    );
                    
                    Create table if not exists sales_accounting(
                        id_s integer not null,
                        id_p integer not null,
                        foreign key (id_s) references work_shift(id),
                        foreign key (id_p) references products(id) 
                    );
                      ''')
    

    while True:
        print(''' В какую таблицу вы хотите попасть?
            1. Сотрудники
            2. Учёт рабочего времени
            3. Товары
            4. Учёт продаж
            5. Выход          
            ''')
        people_choice = int(input('Введите ваш выбор: '))
        if people_choice == 1: # Максим
            while True:
                print('''Ваши действия с таблицей Сотрудники:
                    1. Просмотреть
                    2. Добавить
                    3. Изменить
                    4. Удалить
                    5. Выйти
                    ''')
                people_choice2 = int(input('Ваш выбор: '))
                if people_choice2 == 1:
                    show_table_employees()
                elif people_choice2 == 2:
                    add_people_on_table_employees()
                elif people_choice2 == 3:
                    update_people_on_table_employees()
                elif people_choice2 == 4:
                    delete_people_on_table_employees()
                elif people_choice2 == 5:
                    print('Конец работы с таблицей Сотрудники')
                    break
        
        
        elif people_choice == 2: # Дима
            pass
        elif people_choice == 3: # Вадим
            pass
        elif people_choice == 4: # Максим
            while True:
                print('''Ваши действия с таблицей Сотрудники:
                    1. Просмотреть
                    2. Добавить
                    3. Выйти
                    ''')
                people_choice2 = int(input('Ваш выбор: '))
                if people_choice2 == 1:
                    show_table_sales_accounting()
                elif people_choice2 == 2:
                    add_id_s_and_id_p_in_table_sales_accounting()
                elif people_choice2 == 3:
                    print('Конец работы с таблицей Учёт продаж')
                    break
        elif people_choice == 5:
            print('Конец работы ')
            break