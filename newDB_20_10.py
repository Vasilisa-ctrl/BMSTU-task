'''Принцип ACID
A = Атомарность: транзакция не может быть выполнена частично - всё или ничего
C = Согласованность: после выполнения транзакции все данные должны быть согласованы
I = Изолированность: параллельные транзакции не должны мешать друг другу, каждая транзакция должна "думать", что она единственная в системе
D = Долговечность: до коммита данные хранятся в журнале, а после - записываются в Базу Данных'''

#---------------------------------------------------------------------------------------------------------------------------------------------

'''import sqlite3
from contextlib import closing
#import sys

#sys.sleep(3)

def create_tbl():
    with closing(sqlite3.connect("accounts.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY, name TEXT NOT NULL, balance INTEGER)")
            print("creating!")
def insert_into_table():
    with closing(sqlite3.connect("accounts.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO account (name, balance) VALUES ('Kolya', 1500)")
            cursor.execute("INSERT INTO account (name, balance) VALUES ('Petya', 2500)")
            print("inserting!")

create_tbl()
insert_into_table()
with closing(sqlite3.connect("accounts.db")) as conn:
    with conn:
        print("opening!")
        cursor = conn.cursor()
        try:
            cursor.execute('UPDATE account SET balance=balance-1000 WHERE id=1')
            cursor.execute('UPDATE account SET balance=balance+1000 WHERE id=2')
        except:
            conn.rollback()'''

#-----------------------------------------------------------------------------------------------------------
'''
import sqlite3
from contextlib import closing
         
def create_tbl():
    with closing(sqlite3.connect("Table.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE games (id INTEGER PRIMARY KEY, user_id INTEGER, score INTEGER)")
            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER)")
            print("creating!")
def insert_into_table():
    with closing(sqlite3.connect("Table.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO games (user_id, score) VALUES (4, 100500)") 
            cursor.execute("INSERT INTO games (user_id, score) VALUES (2, 1000)")
            cursor.execute("INSERT INTO games (user_id, score) VALUES (5, 5000)")
            cursor.execute("INSERT INTO games (user_id, score) VALUES (3, 10000)")
            cursor.execute("INSERT INTO users (name, age) VALUES ('Kolya', 20)")
            cursor.execute("INSERT INTO users (name, age) VALUES ('Petya', 21)")
            cursor.execute("INSERT INTO users (name, age) VALUES ('Ivan', 20)")
            cursor.execute("INSERT INTO users (name, age) VALUES ('Nikolai', 22)")
            cursor.execute("INSERT INTO users (name, age) VALUES ('Sergey', 19)")
            print("inserting!")

create_tbl()
insert_into_table()
with closing(sqlite3.connect("Table.db")) as conn:
    with conn:
        print("opening!")
        cursor = conn.cursor()
        #cursor.execute("DELETE FROM users WHERE id=4")
        
DELETE FROM users WHERE id=4;
SELECT user_id, name, age, score FROM games LEFT JOIN users ON games.user_id = users.id;
INSERT INTO games (user_id, score) VALUES (3, 1000);
INSERT INTO games (user_id, score) VALUES (3, 2000);
INSERT INTO games (user_id, score) VALUES (3, 3000);

SELECT user_id, name, age, SUM(score) FROM games LEFT JOIN users ON games.user_id = users.id GROUP BY games.user_id
SELECT user_id, name, age, SUM(score) as sum_score FROM games LEFT JOIN users ON games.user_id = users.id ORDER BY sum_score DESC
'''
