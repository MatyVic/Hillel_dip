from datetime import datetime


def parse_date(date_str: str):
    if not date_str or date_str.strip() == "":
        return None
    clean = (date_str.strip().replace("/", ".")
             .replace("-", ".").replace(" ", "."))
    parts = clean.split(".")
    if len(parts) != 3:
        return None
    try:
        day, month, year = map(int, parts)
        return datetime(year, month, day).date()
    except ValueError:
        return None


class Person:
    def __init__(self, name, surname, birth_date, father_name="",
                 gender="", death_date=""):
        if not name:
            raise ValueError("Ім'я обов'язкове")
        if not surname:
            raise ValueError("Призвіще обов'язкове")

        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.birth_date = parse_date(birth_date)
        self.gender = gender
        self.death_date = parse_date(death_date)

        if self.death_date is None:
            self.doa = 'alive'
        else:
            self.doa = 'dead'


p1 = Person('Victor', 'Chupryna', '6.10.1991', 'Oleksandrovych', 'm')

print(p1.birth_date)
print(p1.death_date)
print(p1.doa)
