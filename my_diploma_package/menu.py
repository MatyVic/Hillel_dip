from my_diploma_package.db_new import Database
from my_diploma_package.file_io import upload_person, save_to_file
from my_diploma_package.People import Person
from my_diploma_package.utils import validate_date, print_error
import sys

db = Database("people.db")
db.init_db()

def add_new():
    name = input("Введіть ім'я: ").strip()
    surname = input("Введіть прізвище: ").strip()
    birth_date_input = input("Введіть дату народження: ").strip()
    try:
        birth_date = validate_date(birth_date_input)
    except ValueError as e:
        print_error(e)
        return

    father_name = input("Введіть по батькові (необов'язково): ").strip()
    gender = input("Введіть стать (м/ж): ").strip().lower()
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
        print_error(e)
        return

    new_id = db.add_person(name, surname, birth_date, father_name, gender, death_date)
    person.id = new_id
    print('Було додано нову людину у довідник - ', person)
    print('-----' * 50)


def find_person():
    search_str = input('Введіть строку пошуку ')
    result = db.search_person(search_str)
    print('Результати пошуку:')
    if len(result) == 0:
        print('Немає записів за вашим запитом')
    for person in result:
        print(person)
    print('-----' * 50)


def exit_program():
    print('Завершення роботи')
    sys.exit()


def edit_person():
    search_str = input("Введіть строку пошуку для редагування: ").strip()
    result = db.search_person(search_str)
    if not result:
        print("Немає записів за вашим запитом")
        return

    for idx, person in enumerate(result, start=1):
        print(f"{idx}. {person}")

    choice = input("Оберіть номер для редагування: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(result):
        print("Невірний вибір")
        return

    person_to_edit = result[int(choice) - 1]

    new_name = input(f"Нове ім'я ({person_to_edit.name}): ").strip() or person_to_edit.name
    new_surname = input(f"Нове прізвище ({person_to_edit.surname}): ").strip() or person_to_edit.surname
    new_birth_date = input(f"Нова дата народження ({person_to_edit.birth_date}): ").strip() or person_to_edit.birth_date
    new_father_name = input(f"Нове по батькові ({person_to_edit.father_name}): ").strip() or person_to_edit.father_name
    new_gender = input(f"Нова стать ({person_to_edit.gender}): ").strip() or person_to_edit.gender
    new_death_date = input(f"Нова дата смерті ({person_to_edit.death_date}): ").strip() or person_to_edit.death_date

    db.update_person(person_to_edit.id, new_name, new_surname, new_birth_date, new_father_name, new_gender, new_death_date)
    print("Запис оновлено")
    print('-----' * 50)


def del_person():
    search_str = input("Введіть строку пошуку для видалення: ").strip()
    result = db.search_person(search_str)
    if not result:
        print("Немає записів за вашим запитом")
        return

    for idx, person in enumerate(result, start=1):
        print(f"{idx}. {person}")

    choice = input("Оберіть номер для видалення: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(result):
        print("Невірний вибір")
        return

    person_to_delete = result[int(choice) - 1]
    db.delete_person(person_to_delete.id)
    print("Запис ", person_to_delete, "видалено")
    print('-----' * 50)


menu_variants = {
    "1": add_new,
    "2": upload_person,
    "3": save_to_file,
    "4": find_person,
    "5": edit_person,
    "6": del_person,
    "0": exit_program
}