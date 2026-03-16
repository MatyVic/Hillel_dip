from datetime import datetime, date


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
        self.birth_date = self.parse_date(birth_date)

        if gender == '':
            self.gender = 'undefined'
        else:
            self.gender = gender.lower()

        self.death_date = self.parse_date(death_date)

    def __str__(self):
        gender_str = "чоловік" if self.gender == "m" \
            else "жінка" if self.gender == "f" else "невідомо"

        birth = f"Народився {self.birth_date.strftime('%d.%m.%Y')}" if self.gender == "m" else f"Народилася {self.birth_date.strftime('%d.%m.%Y')}"
        age = self.age()
        death_str = ''
        if self.doa == "dead":
            death_str = "Помер" if self.gender == "m" else "Вмерла" if self.gender == "f" else "Помер(ла)"
            death_str += f' {self.death_date.strftime('%d.%m.%Y')}'

        return f"{self.name} {self.surname} {self.father_name},{age} {self.get_age_str(age)}, {gender_str}. {birth}. {death_str}"

    def age(self):
        if not self.birth_date:
            return None
        end_date = self.death_date if self.death_date else date.today()
        years = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return years

    @staticmethod
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
            if year < 100:
                year += 2000 if year < 30 else 1900
            return datetime(year, month, day).date()
        except ValueError:
            return None

    @staticmethod
    def get_age_str(age):
        if 11 <= age % 100 <= 14 or age % 10 == 0 or age % 10 >= 5:
            return "років"
        elif age % 10 in (2, 3, 4):
            return "роки"
        elif age % 10 == 1:
            return "рік"
        return 'Шоо'

    @property
    def doa(self):
        return "dead" if self.death_date else "alive"
