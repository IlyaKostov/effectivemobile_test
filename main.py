import os
from math import ceil

from src import Phonebook, get_contact_info

PHONEBOOK_FILE = 'phonebook.csv'


def main():
    filepath = os.path.join(os.path.dirname(__file__), PHONEBOOK_FILE)

    phonebook = Phonebook(filepath)
    while True:
        print('\nТелефонный справочник')
        print('1. Вывести записи постранично')
        print('2. Добавить новую запись')
        print('3. Редактировать запись')
        print('4. Поиск записей')
        print('5. Выйти')
        choice = input('Выберите действие: ')

        if choice == '1':
            page_size = 5
            print(f'Всего страниц: {ceil(len(phonebook.contacts) / page_size)}')
            try:
                page_number = int(input('Введите номер страницы: '))
                phonebook.display_contacts(page_number, page_size)
            except ValueError:
                print('Нужно вводить число')

        elif choice == '2':
            contact = get_contact_info()
            phonebook.add_contact(contact)

        elif choice == '3':
            print('Оставьте поле пустым, если у вас нет информации для поиска')
            results = phonebook.search_contacts()
            if not results:
                print('Запись не найдена.')
            else:
                print('Найденные записи:')
                for i, result in enumerate(results):
                    print(f'{i + 1}. {result}')
                try:
                    selection = int(input('Выберите номер записи для редактирования: '))
                    if 1 <= selection <= len(results):
                        contact = results[selection - 1]
                        contact_updates = get_contact_info()
                        phonebook.edit_contact(contact, contact_updates)
                    else:
                        print('Неверный выбор.')
                except ValueError as e:
                    print(e)
                    print('Нужно вводить число')

        elif choice == '4':
            print('Оставьте поле пустым, если у вас нет информации для поиска')
            results = phonebook.search_contacts()
            print('Результаты поиска:')
            if results:
                for result in results:
                    print(result)
            else:
                print('Ничего не найдено по заданным критериям.')

        elif choice == '5':
            break
        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
