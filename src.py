import csv


class Phonebook:
    headers = ['Фамилия', 'Имя', 'Отчество', 'Название организации', 'Телефон рабочий', 'Телефон личный']

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.contacts = []
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

    def validate_contact(self, contact_data):
        """
        Валидация данных нового контакта.

        :param contact_data: Данные нового контакта.
        """
        required_fields = self.headers
        for field in required_fields:
            if field not in contact_data or not contact_data[field]:
                raise ValueError(f'Поле \'{field}\' является обязательным и не может быть пустым.')
            if (field == 'Телефон рабочий' or field == 'Телефон личный') and not contact_data[field].isdigit():
                raise ValueError(f'Поле \'{field}\' должно состоять из цифр.')

    def display_contacts(self, page_number: int, page_size: int = 5) -> None:
        """
        Отображение списка контактов.

        :param page_number: Номер страницы.
        :param page_size: Количество контактов на странице, по умолчанию = 5.
        """
        start_index = (page_number - 1) * page_size
        end_index = min(start_index + page_size, len(self.contacts))
        for i in range(start_index, end_index):
            print(self.contacts[i])

    def add_contact(self, contact_data: dict[str, str]) -> None:
        column_mapping = {
            'Фамилия': 'last_name',
            'Имя': 'first_name',
            'Отчество': 'middle_name',
            'Название организации': 'organization',
            'Телефон рабочий': 'work_phone',
            'Телефон личный': 'personal_phone'
        }
        new_contact_data = {header: contact_data[column_mapping[header]] for header in self.headers}
        self.validate_contact(new_contact_data)
        self.contacts.append(new_contact_data)
        self.save_contacts_to_file()

    def edit_contact(self) -> None:
        pass

    def search_contact(self) -> None:
        pass


