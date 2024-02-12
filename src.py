import csv
from math import ceil
from typing import List, Dict, Any


class Phonebook:
    headers = ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный']

    def __init__(self, filepath: str) -> None:
        self.filepath: str = filepath
        self.contacts: List[Any] = []
        self.load_contacts_from_file()

    def load_contacts_from_file(self) -> None:
        try:
            with open(self.filepath, encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.contacts.append(row)
        except FileNotFoundError:
            print('Файл не найден')

    def save_contacts_to_file(self) -> None:
        with open(self.filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact)
        print("Данные успешно сохранены в файл.")

    def validate_contact(self, contact_data: Dict[str, str]) -> None:
        """
        Валидация данных нового контакта.

        :param contact_data: Данные нового контакта.
        """
        required_fields: List[str] = self.headers
        for field in required_fields:
            if field not in contact_data or not contact_data[field]:
                raise ValueError(f'Поле \'{field}\' является обязательным и не может быть пустым.')
            if (field == 'Телефон рабочий' or field == 'Телефон личный') and not contact_data[field].isdigit():
                raise ValueError(f'Поле \'{field}\' должно состоять из цифр.')
        for contact in self.contacts:
            if contact == contact_data:
                raise ValueError(f'Контакт с такими данными уже существует.')

    def display_contacts(self, page_number: int, page_size: int) -> None:
        """
        Отображение списка контактов.

        :param page_number: Номер страницы.
        :param page_size: Количество контактов на странице, по умолчанию = 5.
        """
        start_index: int = (page_number - 1) * page_size
        end_index: int = min(start_index + page_size, len(self.contacts))
        for i in range(start_index, end_index):
            print(self.contacts[i])

    def add_contact(self, contact_data: Dict[str, str]) -> None:
        column_mapping = {
            'Фамилия': 'last_name',
            'Имя': 'first_name',
            'Отчество': 'middle_name',
            'Название организации': 'organization',
            'Телефон рабочий': 'work_phone',
            'Телефон личный': 'personal_phone'
        }
        new_contact_data: Dict[str, str] = {header: contact_data[column_mapping[header]] for header in self.headers}
        try:
            self.validate_contact(new_contact_data)
            self.contacts.append(new_contact_data)
            self.save_contacts_to_file()
        except ValueError as e:
            print(f'\n{e}')

    def edit_contact(self, contact_index: int, contact_updates: Dict[str, str]) -> None:
        """
        Редактирование существующего контакта.

        :param contact_index: Индекс контакта в списке.
        :param contact_updates: Новые данные контакта.
        """
        contact = self.contacts[contact_index]

        for key, value in contact_updates.items():
            if value:  # Проверяем, что значение поля не пустое
                contact[key] = value
        print(contact)
        self.contacts[contact_index] = contact
        self.save_contacts_to_file()
        print("Запись успешно отредактирована.")

    def search_contacts(self) -> List[str]:
        """
        Поиск контактов по заданным критериям.
        """
        results = []
        search_criteria: Dict[str, str] = self.get_search_criteria(self.headers)
        for contact in self.contacts:
            is_match = True
            for key, value in search_criteria.items():
                if value and contact.get(key) != value:
                    is_match = False
                    break
            if is_match:
                results.append(contact)
        return results

    @staticmethod
    def get_search_criteria(headers: List[str]):
        search_criteria = {
            key: input(f"Введите {key} для поиска: ")
            for key in headers
        }
        return search_criteria


