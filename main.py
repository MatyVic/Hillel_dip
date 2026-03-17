import sys
import json
import glob

from my_diploma_package.People import Person
from my_diploma_package import db


def add_new():

    name = input("Введіть ім'я: ").strip()
    surname = input("Введіть прізвище: ").strip()
    birth_date = input("Введіть дату народження: ").strip()
    father_name = input("Введіть по батькові (необов'язково): ").strip()
    gender = input("Введіть стать (м/ж) (необов'язково): ").strip().lower()
    death_date = input("Введіть дату смерті (необов'язково): ").strip()
    try:
        person = Person(
            name=name,
            surname=surname,
            birth_date=birth_date,
            father_name=father_name,
            gender=gender,
            death_date=death_date
        )
    except ValueError as e:
        print("Виникла помилка: ", e)
        print('-----' * 50)
        return  # вихід із функції без запису в базу

    db.add_person(name, surname, birth_date, father_name, gender, death_date)
    print('Було додано нову людину у довідник - ', person)
    print('-----' * 50)


def find_person():
    search_str = input('Введіть строку пошуку ')
    result = db.search_person(search_str)
    print('Результати пошуку:')
    for person in result:
        print(person)
    print('-----' * 50)


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
            db.add_person(
                person.name,
                person.surname,
                person.birth_date,
                person.father_name,
                person.gender,
                person.death_date
            )
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


def exit_program():
    print('Завершення роботи')
    sys.exit()


menu_variants = {"1": add_new, "2": upload_person,
                 "3": find_person, "4": save_to_file, "5": exit_program}


def main():
    while True:
        db.init_db()

        print('Вас вітає довідник мешканців країни '
              'будь ласка оберіть пункт меню')

        print('1-Додати\n2-Завантажити з файлу\n3-Пошук'
              '\n4-Зберегти у файл\n5-Вихід\n')
        ans = input('Введіть пункт меню ').strip()

        menu_variants.get(ans)()


if __name__ == "__main__":
    main()
