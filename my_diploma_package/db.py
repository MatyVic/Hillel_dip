import sqlite3

from my_diploma_package.People import Person

db_name = 'people.db'


def get_db_con():
    return sqlite3.connect(db_name)


def init_db():
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        birth_date TEXT,
        father_name TEXT,
        gender TEXT,
        death_date TEXT
    )
    """)
    conn.commit()
    conn.close()


def add_person(name, surname, birth_date, father_name, gender, death_date):
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO people (name, surname, birth_date, father_name, gender, death_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, surname, birth_date, father_name, gender, death_date))
    conn.commit()
    conn.close()


def search_person(query):
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, surname, birth_date, father_name, gender, death_date
        FROM people
        WHERE lower(name) LIKE ? OR lower(surname) LIKE ? OR lower(father_name) LIKE ?
    """, (f"%{query.lower()}%", f"%{query.lower()}%", f"%{query.lower()}%"))
    rows = cursor.fetchall()
    conn.close()
    return [Person(*row) for row in rows]
