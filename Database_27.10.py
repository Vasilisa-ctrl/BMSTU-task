'''import sqlite3
from contextlib import closing

def create_tbl():
    with closing(sqlite3.connect("database.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
            cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, customers_id INTEGER, amount REAL, FOREIGN KEY (customers_id) REFERENCES customers(id) ON DELETE CASCADE)") # каскадно улдаляет строки в связанной таблице по удаляемому id
            print("creating!")                # есть также варианты ВМЕСТО CASCADE: RESTRICT/SET NULL/SET DEFAULT/NO ACTION
def insert_into_table():
    with closing(sqlite3.connect("database.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.execute("INSERT INTO customers (name) VALUES ('Ivan')")
            cursor.execute("INSERT INTO customers (name) VALUES ('Peter')")
            cursor.execute("INSERT INTO customers (name) VALUES ('Kolya')")
            cursor.execute("INSERT INTO customers (name) VALUES ('Serj')")
            cursor.execute("INSERT INTO orders (customers_id, amount) VALUES (3, 100500)")
            cursor.execute("INSERT INTO orders (customers_id, amount) VALUES (1, 100.5)")
            cursor.execute("INSERT INTO orders (customers_id, amount) VALUES (4, 123)")
            cursor.execute("INSERT INTO orders (customers_id, amount) VALUES (2, 246)")
            cursor.execute("INSERT INTO orders (customers_id, amount) VALUES (1, 369.5)")
            #cursor.execute("INSERT INTO orders (customers_id, amount) VALUES (999, 66.6)")
            print("inserting!")

create_tbl()
insert_into_table()
with closing(sqlite3.connect("database.db")) as conn:
    with conn:
        print("opening!")
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE account SET balance=balance-1000 WHERE id=1')
            cursor.execute('UPDATE account SET balance=balance+1000 WHERE id=2')
        except:
            conn.rollback()'''
#----------------------------------------------------------------------------------------------------------------------------------------
#   ORM - Object Relatoinal Mapping

from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, Float, Boolean, insert
)

engine = create_engine('sqlite:///database.db') 

metadata = MetaData()
students_table = Table(
    'students', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('group', String(20)),
    Column('gpa', Float, default=0.0),
    Column('is_active', Boolean, default=True),
)

metadata.create_all(engine)

with engine.begin() as connection:               
    something = insert(students_table).values(
        name='Иванов И.И.',
        group='ИУ10-33',
        gpa=4.5,
    )
    result = connection.execute(something)
    connection.commit()
    print(f"Добавлена строка с id={result.inserted_primary_key[0]}")
'''
smt = insert(student_table)
data = [{'name'='', 'group'='', 'gpa'=''}, {}, {}]
result = connection.execute(smt, data)'''

