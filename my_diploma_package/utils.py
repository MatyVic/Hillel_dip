import re
from datetime import datetime

def validate_date(date_str):

    if not re.match(r'^[0-9.\-\/\s]+$', date_str):
        raise ValueError("Дата може містити лише цифри та роздільники (., -, /, пробіл)")
    if not any(ch.isdigit() for ch in date_str):
        raise ValueError("Дата повинна містити цифри!")

    formats = [
        "%d.%m.%Y", "%d-%m-%Y", "%d/%m/%Y", "%d %m %Y", "%Y-%m-%d",
        "%d.%m.%y", "%d-%m-%y", "%d/%m/%y", "%d %m %y"
    ]

    for fmt in formats:
        try:
            datetime.strptime(date_str, fmt)
            return date_str
        except ValueError:
            continue

    raise ValueError("Дата введена некоректно. Використовуйте формат: "
                     "дд.мм.рррр, дд мм рррр, дд/мм/рррр, дд-мм-рррр або дд.мм.рр")

def print_error(e):
    print("Виникла помилка:", e)
    print('-----' * 50)
