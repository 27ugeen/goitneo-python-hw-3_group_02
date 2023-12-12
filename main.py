from address_book import AddressBook, Record, InvalidPhoneError, InvalidDateError, BirthdayExistsError

class NoContactsError(Exception):
    pass

class ContactExistsError(Exception):
    pass

class MissingArgumentsError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except MissingArgumentsError:
            return "Give me please name and birthday"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide a name."
        except ContactExistsError:
            return "Contact already exists."
        except InvalidPhoneError:
            return "Invalid phone number format"
        except InvalidDateError:
            return "Invalid date format. Please use DD.MM.YYYY."
        except BirthdayExistsError:
            return "Birthday already exists for this contact."
        except NoContactsError:
            return "No contacts found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()

    return cmd, *args


def hello():
    return "How can I help you?"

@input_error
def add_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        raise ContactExistsError
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)

    return "Contact added."

@input_error
def change_contact(args, book):
    name, phone = args
    record = book.find(name)
    if record:
        record.edit_phone(phone)

        return "Contact updated."
    else:
        raise KeyError
        
@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record.find_phone()
    else:
        raise KeyError

@input_error
def show_all(book):
    if not book:
        raise NoContactsError
    result = "\n".join([str(record) for record in book.data.values()])
    
    return result
    
@input_error
def add_birthday(args, book):
    if len(args) < 2:
        raise MissingArgumentsError
    
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        raise KeyError
    
@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record:
        return record.birthday if record.birthday else "No birthday entered"
    else:
        raise KeyError

def birthdays(book):
    book.get_birthdays_per_week()
        

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            birthdays(book)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()