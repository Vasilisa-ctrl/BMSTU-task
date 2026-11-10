import json
from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, Float, ForeignKey, insert
)

engine = create_engine('sqlite:///Catalog.db')

metadata = MetaData()

category_table = Table(
    'category', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('description', String),
)

products_table = Table(
    'products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('price', Float)),
)

def create_tbl():
    metadata.create_all(engine)
    print("creating!")


def insert_into_table():
    with engine.begin() as connection:
        with open("catalog.json", "r", encoding="utf-8") as f1:
            data = json.load(f1)

        seem = set()
        for item in data:
            productt = item["product_name"]
            pricee = item["price"]
            connection.execute(
                insert(products_table).values(name=productt, price=pricee)
            )

            categoryy = item["category"]
            if categoryy["name"] in seem:
                continue
            seem.add(categoryy["name"])

            name_c = categoryy["name"]
            description_c = categoryy["description"]
            connection.execute(
                insert(category_table).values(name=name_c, description=description_c)
            )

        print("inserting!")


create_tbl()
insert_into_table()
