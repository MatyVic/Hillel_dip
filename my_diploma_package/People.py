from datetime import datetime

def parse_date(date_str: str):

    if not date_str or date_str.strip() == "":
        return None
    clean = date_str.strip().replace("/", ".").replace("-", ".").replace(" ", ".")
    parts = clean.split(".")
    if len(parts) != 3:
        return None
    try:
        day, month, year = map(int, parts)
        return datetime(year, month, day).date()
    except ValueError:
        return None


class Human:
    def __init__(self, name, surname, date_of_birth, gender, date_of_death = 0):
        self.name = name
        self.surname = surname
        self.date_of_birth = parse_date(date_of_birth)
        self.date_of_death = None if date_of_death == 0 else parse_date(str(date_of_death))
        self.gender = gender
        self.gender = gender
        self.status = "inactive" if date_of_death is None else "active"

    # def __str__(self):
    #     return {
    #         "first_name": self.name,
    #         "last_name": self.surname,
    #         "birth_date": self.date_of_birth,
    #         "death_date": self.date_of_death,
    #         "status": self.status,
    #         "gender": self.gender
    #     }

first = Human('Ivan', 'Petrenko', '8 9 1998', 'm')
print(first.date_of_birth)
print(first.date_of_death)

print(first.__dict__)