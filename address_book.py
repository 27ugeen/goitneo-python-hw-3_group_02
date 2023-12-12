from collections import UserDict
from datetime import datetime
from user_helpers import get_birthdays_per_week

class InvalidPhoneError(Exception):
    pass

class InvalidDateError(Exception):
    pass

class BirthdayExistsError(Exception):
    pass

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (isinstance(value, str) and value.isdigit() and len(value) == 10):
            raise InvalidPhoneError
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise InvalidDateError
        super().__init__(value)

    def __str__(self):
        return str(self.value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = None
        self.birthday = None

    def add_phone(self, phone):
        self.phone = Phone(phone)

    def edit_phone(self, new_phone):
        if self.phone is not None:
            self.phone = Phone(new_phone)

    def remove_phone(self):
        self.phone = None

    def find_phone(self):
        return self.phone.value if self.phone else None

    def add_birthday(self, birthday):
        if self.birthday is not None:
            raise BirthdayExistsError
        self.birthday = Birthday(birthday)

    def __str__(self):
        phone_info = f"{self.phone.value}" if self.phone else "No phone"
        if self.birthday is not None:
            return f"name: {self.name.value}, phone: {phone_info}, birthday: {self.birthday}"
        else:
            return f"name: {self.name.value}, phone: {phone_info}"
    
class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_birthdays_per_week(self):
        return get_birthdays_per_week(self.values())