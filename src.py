import csv


class Phonebook:
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

    def save_contacts_to_file(self):
        pass

    def display_contacts(self, page_number: int, page_size: int = 5) -> None:
        pass

    def add_contact(self, contact_data: dict[str, str]) -> None:

        pass

    def edit_contact(self) -> None:
        pass

    def search_contact(self) -> None:
        pass


