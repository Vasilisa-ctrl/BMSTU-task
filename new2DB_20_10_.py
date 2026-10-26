import sqlite3
from contextlib import closing

create_tbl()
insert_into_table()
conn = sqlite3.connect ('accounts.db')
cursor = conn.cursor()
try:
    cursor.execute('UPDATE account SET balance=balance - 1000 WHERE id=1')
    #raise Exeption ('Power Failute')
    cursor.execute('UPDATE account SET balance=balance + 1000 WHERE id=2')
    conn.commit()
except:
    conn.rollback()

