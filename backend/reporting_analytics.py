```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')       
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    if conn:
        return conn
    return None

def player_performance_report(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Players")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def contract_outcomes_report(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Contracts")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"C:\sqlite\db\pythonsqlite.db"

    conn = create_connection(database)

    with conn: 
        print("Player Performance Report:")
        player_performance_report(conn)

        print("Contract Outcomes Report:")
        contract_outcomes_report(conn)

if __name__ == '__main__':
    main()
```