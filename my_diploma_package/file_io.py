import json
import glob
from my_diploma_package.People import Person
from my_diploma_package.db_new import Database


class FileStorage:
    def __init__(self, db: Database):
        self.db = db

    def upload_person(self):
        file_list = glob.glob("*.json")
        file_menu = {}
        print('Cписок існуючих файлів:')
        for idx, filename in enumerate(file_list, start=1):
            file_menu[str(idx)] = filename
            print(idx, '-', filename)

        print('-----' * 50)
        ans = input('Оберіть файл ')

        if ans and ans in file_menu:
            file_name = file_menu[ans]
        else:
            file_name = input('Введіть шлях до файла ')

        with open(file_name, "r", encoding="utf-8") as f:
            people = json.load(f)

        for p in people:
            try:
                person = Person(
                    name=p.get("name", ""),
                    surname=p.get("surname", ""),
                    birth_date=p.get("birth_date", ""),
                    father_name=p.get("father_name", ""),
                    gender=p.get("gender", ""),
                    death_date=p.get("death_date", "")
                )
                new_id = self.db.add_person(
                    person.name,
                    person.surname,
                    person.birth_date,
                    person.father_name,
                    person.gender,
                    person.death_date
                )
                person.id = new_id
                print("Додано:", person)
            except ValueError as e:
                print("Помилка у даних:", e)

        print('-----' * 50)

    def save_to_file(self):
        filename = input('Введіть назву файлу для збереження ') + '.json'
        result = self.db.get_all_persons()
        people_list = [person.to_dict() for person in result]

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(people_list, f, ensure_ascii=False, indent=4)

        print(f"Дані збережено у файл {filename}")
