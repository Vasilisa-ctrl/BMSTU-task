import json
import sqlite3
from contextlib import closing

def create_tbl():
    with closing(sqlite3.connect("Catalog.db")) as conn:
        with conn:
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY, name TEXT NOT NULL, description TEXT)")
            cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL, FOREIGN KEY (id) REFERENCES category(name))")
            print("creating!")

def insert_into_table():
    with closing(sqlite3.connect("Catalog.db")) as conn:
        with conn:
            cursor = conn.cursor()
            with open("catalog.json", "r", encoding="utf-8") as f1:
                data = json.load(f1)

            seem = set()
            for item in data:
                productt = item["product_name"]
                pricee = item["price"]
                cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (productt, pricee))
                
                categoryy = item["category"]
                if categoryy["name"] in seem:
                    continue
                seem.add(categoryy["name"])
                name_c = categoryy["name"]
                description_c = categoryy["description"]
                cursor.execute("INSERT INTO category (name, description) VALUES (?, ?)", (name_c, description_c))
                
            print("inserting!")

create_tbl()
insert_into_table()




