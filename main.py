from my_diploma_package import db
from my_diploma_package.menu import menu_variants

def main():
    while True:
        db.init_db()
        print('Вас вітає довідник мешканців країни, будь ласка оберіть пункт меню')
        print('1-Додати\n2-Завантажити з файлу\n3-Зберегти у файл\n4-Пошук\n5-Оновити запис\n6-Видалити запис\n0-Вихід\n')
        ans = input('Введіть пункт меню ').strip()
        if ans in menu_variants:
            menu_variants[ans]()
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
