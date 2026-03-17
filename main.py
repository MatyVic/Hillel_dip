import sys

from my_diploma_package.People import Person
from my_diploma_package import db


def add_new():

    name = input("Введіть ім'я: ").strip()
    surname = input("Введіть прізвище: ").strip()
    birth_date = input("Введіть дату народження: ").strip()
    father_name = input("Введіть по батькові (необов'язково): ").strip()
    gender = input("Введіть стать (м/ж) (необов'язково): ").strip().lower()
    death_date = input("Введіть дату смерті (якщо є, інакше залиште порожнім): ").strip()
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

def update_person():
    print("Функція оновлення ще не реалізована.")

def save_to_file():
    print("Функція збереження у файл ще не реалізована.")


def exit_program():
    print('Завершення роботи')
    sys.exit()

menu_variants = {"1": add_new, "2": update_person, "3": find_person, "4": save_to_file, "5": exit_program}

def main():
    while True:
        db.init_db()

        print(f'Вас вітає довідник мешканців країни будь ласка оберіть пункт меню')
        print(f'1-Додати\n2-Оновити\n3-Пошук\n4-Зберегти у файл\n5-Вихід\n')
        ans = input('Введіть пункт меню ').strip()

        menu_variants.get(ans)()


if __name__ == "__main__":
    main()
