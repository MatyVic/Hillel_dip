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
        gender_str = "чоловік" if self.gender == "m" else "жінка" if self.gender == "f" else "невідомо"
        age = self.age()
        birth = f"Народився {self.birth_date.strftime('%d.%m.%Y')}" if self.gender == "m" else f"Народилася {self.birth_date.strftime('%d.%m.%Y')}"
        death = f"Помер: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date and self.gender == "m" else f"Вмерла: {self.death_date.strftime('%d.%m.%Y')}" if self.death_date else ""
        return f"{self.name} {self.surname} {self.father_name},{self.doa} {age} років, {gender_str}. {birth}. {death}"


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

    @property
    def doa(self):
        return "dead" if self.death_date else "alive"


p1 = Person('Victor', 'Chupryna', '6.10.91', 'Oleksandrovych', )

print(p1.birth_date)
print(p1.death_date)
print(p1.doa)
print(p1.gender)
print(p1.age())
print(p1)
