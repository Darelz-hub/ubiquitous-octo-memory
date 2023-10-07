
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
                        name TEXT NOT NULL,
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
    