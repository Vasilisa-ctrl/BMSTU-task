'''import json

with open("users.json", "r", encoding="utf-8") as f1:
    lines = json.load(f1)          #список объектов

result = lines * 10000

with open("new.json", "w", encoding="utf-8") as f2:
    json.dump(result, f2, ensure_ascii=False, indent=2)

print("########################################")

with open("new.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(len(data))'''
    
'''#----------------------------------------------------------
# База данных

#Student
#  id  |     name  |    mark  |  age  |'''
'''CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)
INSERT INTO students (name, mark, age) VALUES ("Иванов", 41, 19)
SELECT * FROM students WHERE age>18
UPDATE students SET age=20 WHERE name="Иванов"
DELETE FROM students WHERE id=1'''

import sqlite3

def create_tbl():
    conn = sqlite3.connect ('unvercity.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, mark REAL, age INTEGER)")
    conn.commit()
    conn.close()
def insert_into_table():
    conn = sqlite3.connect ('unvercity.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, mark, age) VALUES ('Демиденко', 4.5, 19)")
    conn.commit()
    conn.close()
def update_info():
    conn = sqlite3.connect ('unvercity.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age=25 WHERE id=1")
    conn.commit()
    conn.close()
def show_data():
    conn = sqlite3.connect ('unvercity.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id,name FROM students WHERE age>18")
    rows = cursor.fetchall()
    users = []
    for row in rows:
        users.append(row[1])
    print(users)      
create_tbl()
insert_into_table()
update_info()
show_data()



