from my_diploma_package.People import Person

def main():
    # Запитуємо дані у користувача
    name = input("Введіть ім'я: ").strip()
    surname = input("Введіть прізвище: ").strip()
    father_name = input("Введіть по батькові (необов'язково): ").strip()
    birth_date = input("Введіть дату народження (ДД.ММ.РРРР): ").strip()
    gender = input("Введіть стать (m/f): ").strip().lower()
    death_date = input("Введіть дату смерті (якщо є, інакше залиште порожнім): ").strip()

    # Створюємо об'єкт Person
    person = Person(
        name=name,
        surname=surname,
        birth_date=birth_date,
        father_name=father_name,
        gender=gender,
        death_date=death_date
    )

    # Виводимо результат
    print("\nІнформація про людину:")
    print(person)

if __name__ == "__main__":
    main()
