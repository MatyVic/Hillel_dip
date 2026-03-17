from datetime import datetime, date


class Person:
    def __init__(self, name, surname, birth_date, father_name="",
                 gender="", death_date="", id=None):
        if not name:
            raise ValueError("Ім'я обов'язкове")
        if not surname:
            raise ValueError("Прізвище обов'язкове")
        self.id = id
        self.name = name.strip()
        self.surname = surname.strip()
        self.birth_date = self.parse_date(birth_date)

        if self.birth_date and self.birth_date > date.today():
            raise ValueError("Дата народження не може бути у майбутньому")

        self.death_date = self.parse_date(death_date)

        if (self.birth_date and self.death_date
                and self.death_date < self.birth_date):
            raise ValueError("Дата смерті не може бути раніше дати народження")

        if self.death_date and self.death_date > date.today():
            raise ValueError("Дата смерті не може бути у майбутньому")

        self.father_name = father_name.strip()

        gender_str = gender.strip().lower().casefold()
        gender_map = {
            'м': 'm', 'm': 'm', 'man': 'm', 'чоловік': 'm',
            'ж': 'w', 'w': 'w', 'woman': 'w', 'жінка': 'w'
        }
        if not gender_str:
            self.gender = 'non binary'
        elif gender_str in gender_map:
            self.gender = gender_map[gender_str]
        else:
            raise ValueError("Стать має бути 'м', 'ж', 'm', 'w', "
                             "'man', 'woman', 'чоловік', 'жінка'")

    def __str__(self):
        gender_str = "чоловік" if self.gender == "m" \
            else "жінка" if self.gender == "w" else "не визначена"

        birth_word = {"m": "Народився", "w": "Народилася"}.get(self.gender, "Дата народження")
        birth = f"{birth_word} {self.birth_date.strftime('%d.%m.%Y')}" if self.birth_date else "Дата народження невідома"

        age = self.age()
        death_str = ""
        if self.death_date:
            death_word = "Помер" if self.gender == "m" else "Померла" if self.gender == "w" else "Помер(ла)"
            death_str = f"{death_word} {self.death_date.strftime('%d.%m.%Y')}"

        return (f"ФІО: {self.surname} {self.name} {self.father_name}, "
                f"Стать: {gender_str}. "
                f"Статус людини: {self.doa}. "
                f"{birth} - {death_str} "
                f"Вік: {age} {self.get_age_str(age)}. ")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "birth_date": str(self.birth_date),
            "father_name": self.father_name,
            "gender": self.gender,
            "death_date": "" if self.death_date is None else str(self.death_date),
        }

    def age(self):
        if not self.birth_date:
            return None
        end_date = self.death_date if self.death_date else date.today()
        years = end_date.year - self.birth_date.year
        if ((end_date.month, end_date.day) <
                (self.birth_date.month, self.birth_date.day)):
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
            if len(parts[0]) == 4:
                year, month, day = map(int, parts)
            else:
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
        return "мертва" if self.death_date else "жива"
