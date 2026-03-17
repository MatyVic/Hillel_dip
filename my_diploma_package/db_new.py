import sqlite3
from my_diploma_package.People import Person


class Database:
    def __init__(self, db_name: str = "people.db"):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def init_db(self):
        self.connect()
        self.cursor.execute("""
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
                father_name_cf TEXT
            )
        """)
        self.connection.commit()
        self.close()

    def add_person(self, name, surname, birth_date, father_name, gender, death_date):
        self.connect()
        self.cursor.execute("""
            INSERT INTO people (name, surname, birth_date, father_name,
            gender, death_date, name_cf, surname_cf, father_name_cf)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, surname, birth_date, father_name, gender, death_date,
            name.casefold(), surname.casefold(), father_name.casefold()
        ))
        self.connection.commit()
        new_id = self.cursor.lastrowid
        self.close()
        return new_id

    def search_person(self, query):
        self.connect()
        query_norm = query.casefold()
        q = f"%{query_norm}%"
        self.cursor.execute("""
            SELECT name, surname, birth_date, father_name, gender, death_date, id
            FROM people
            WHERE name_cf LIKE ?
               OR surname_cf LIKE ?
               OR father_name_cf LIKE ?
        """, (q, q, q))
        rows = self.cursor.fetchall()
        self.close()
        return [
            Person(name=row[0], surname=row[1], birth_date=row[2],
                   father_name=row[3], gender=row[4], death_date=row[5], id=row[6])
            for row in rows
        ]

    def get_all_persons(self):
        self.connect()
        self.cursor.execute("""
            SELECT name, surname, birth_date, father_name, gender, death_date, id
            FROM people
        """)
        rows = self.cursor.fetchall()
        self.close()
        return [
            Person(name=row[0], surname=row[1], birth_date=row[2],
                   father_name=row[3], gender=row[4], death_date=row[5], id=row[6])
            for row in rows
        ]

    def update_person(self, person_id, name, surname, birth_date, father_name, gender, death_date):
        self.connect()
        self.cursor.execute("""
            UPDATE people
            SET name = ?, surname = ?, birth_date = ?, father_name = ?, gender = ?, death_date = ?,
                name_cf = ?, surname_cf = ?, father_name_cf = ?
            WHERE id = ?
        """, (
            name, surname, birth_date, father_name, gender, death_date,
            name.casefold(), surname.casefold(), father_name.casefold(),
            person_id
        ))
        self.connection.commit()
        self.close()

    def delete_person(self, person_id):
        self.connect()
        self.cursor.execute("DELETE FROM people WHERE id = ?", (person_id,))
        self.connection.commit()
        self.close()

    def get_last_id(self):
        self.connect()
        self.cursor.execute("SELECT MAX(id) FROM people")
        result = self.cursor.fetchone()
        self.close()
        return result[0] if result else None
