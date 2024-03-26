import os

from src import Phonebook, display_contacts, add_contact, edit_contact, search_contacts

PHONEBOOK_FILE = 'phonebook.csv'


def main():
    filepath = os.path.join(os.path.dirname(__file__), PHONEBOOK_FILE)
    phonebook = Phonebook(filepath)

    actions = {
        '1': display_contacts,
        '2': add_contact,
        '3': edit_contact,
        '4': search_contacts,
    }

    while True:
        print('\nТелефонный справочник')
        print('1. Вывести записи постранично')
        print('2. Добавить новую запись')
        print('3. Редактировать запись')
        print('4. Поиск записей')
        print('5. Выйти')
        choice = input('Выберите действие: ')

        if choice == '5':
            break

        action = actions.get(choice)
        if action:
            action(phonebook)
        else:
            print('Неверный выбор. Попробуйте снова.')


if __name__ == '__main__':
    main()
