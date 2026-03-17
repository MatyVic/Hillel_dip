import json
import glob
from my_diploma_package import db
from my_diploma_package.People import Person

def upload_person():

    file_list = glob.glob("*.json")
    file_menu = {}
    print('Cписок існуючих файлів:')
    for _, filename in enumerate(file_list, start=1):
        file_menu[f"{_}"] = filename
        print(_, '-',  filename)

    print('-----' * 50)
    ans = input('Оберіть файл ')

    if not ans == '':
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
            new_id = db.add_person(
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

def save_to_file():
    filename = input('Введіть назву файлу для збереження ') + '.json'
    result = db.get_all_persons()
    people_list = []
    for person in result:
        person_dict = {
            "name": person.name,
            "surname": person.surname,
            "birth_date": str(person.birth_date),
            "father_name": person.father_name,
            "gender": person.gender,
            "death_date": (
                "" if person.death_date is None else str(person.death_date)
                ),
        }
        people_list.append(person_dict)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(people_list, f, ensure_ascii=False, indent=4)