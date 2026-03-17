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
        death_date TEXT,
        name_cf TEXT,
        surname_cf TEXT,
        father_name_cf TEXT)
        """)
    conn.commit()
    conn.close()


def add_person(name, surname, birth_date, father_name, gender, death_date):
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO people (name, surname, birth_date, father_name,
        gender, death_date, name_cf, surname_cf,father_name_cf)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, surname, birth_date, father_name, gender, death_date,
          name.casefold(), surname.casefold(), father_name.casefold()))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id


def search_person(query):
    conn = get_db_con()
    cursor = conn.cursor()
    query_norm = query.casefold()
    q = f"%{query_norm}%"
    cursor.execute("""
        SELECT name, surname, birth_date, father_name, gender, death_date, id
        FROM people
        WHERE name_cf LIKE ?
           OR surname_cf LIKE ?
           OR father_name_cf LIKE ?
    """, (q, q, q))
    rows = cursor.fetchall()
    conn.close()
    return [Person(name=row[0], surname=row[1], birth_date=row[2],
               father_name=row[3], gender=row[4], death_date=row[5], id=row[6]) for row in rows]


def get_all_persons():
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, surname, birth_date, father_name, gender, death_date
        FROM people
    """)
    rows = cursor.fetchall()
    conn.close()
    return [Person(name=row[0], surname=row[1], birth_date=row[2],
               father_name=row[3], gender=row[4], death_date=row[5]) for row in rows]

def update_person(person_id, name, surname, birth_date, father_name, gender, death_date):
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE people
        SET name = ?, surname = ?, birth_date = ?, father_name = ?, gender = ?, death_date = ?,
            name_cf = ?, surname_cf = ?, father_name_cf = ?
        WHERE id = ?
    """, (
        name, surname, birth_date, father_name, gender, death_date,
        name.casefold(), surname.casefold(), father_name.casefold(),
        person_id
    ))
    conn.commit()
    conn.close()



def delete_person(person_id):
    with get_db_con() as conn:
        conn.execute("DELETE FROM people WHERE id = ?", (person_id,))


def get_id():
    conn = get_db_con()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM people")
    result = cursor.fetchone()

    return result[0] if result else None
