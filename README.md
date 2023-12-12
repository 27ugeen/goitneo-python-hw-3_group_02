# Project "Assistant Bot"

  This is a console assistant bot capable of interacting with the user and executing various commands.  
  The bot responds to various commands, such as adding, changing, and displaying contacts, as well as saying hello and exiting.

### Bot Commands:

1. `hello`: Outputs the message "How can I help you?".
2. `add [name] [phone number]`: Adds a new contact with the specified name and phone number.
3. `change [name] [new phone number]`: Changes the phone number for an existing contact.
4. `phone [name]`: Outputs the phone number for the specified contact.
5. `all`: Outputs all saved contacts with phone numbers.
6. `add-birthday [name] [birthday]`: Adds a birthday for the specified contact.
7. `show-birthday [name]`: Shows the birthday for the specified contact.
8. `birthdays`: Shows the birthdays that will occur within the next week.
9. `close` or `exit`: Exits the bot.

### How to Use:

1. Enter a command in the console.
2. Follow the prompts to add, change, view, or display all contacts.
3. To exit, enter `close` or `exit`.

### Running the Program:

1. Open the terminal or command prompt.
2. Navigate to the project directory.
3. Use the command `python your_script_name.py`, where `your_script_name.py` is the name of your code file.

### Example Usage:

```bash
$ python your_script_name.py
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.
Enter a command: add Jane 9876543210
Contact added.
Enter a command: change John 5555555555
Contact updated.
Enter a command: phone John
5555555555
Enter a command: all
John: 5555555555
Jane: 9876543210
Enter a command: add-birthday John 01.01.1990
Birthday added for John.
Enter a command: show-birthday John
01.01.1990
Enter a command: birthdays
Monday: John
Enter a command: exit
Good bye!
```