import handlers
from address_book import *


def parse_input(user_input):
    """
    Parse the input from the user. If there is no input - set default command to "help"
    :param user_input:
    :return:
    """
    if user_input == "":
        return "help", []

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")

    # Each handler must accept two arguments: args and contacts dictionary and return tuple with the output
    # and the termination flag if program should exit
    command_to_handler = {
        "close": handlers.exit,
        "exit": handlers.exit,
        "hello": handlers.hello,
        "add": handlers.add_contact,
        "change": handlers.set_contact_phone,
        "phone": handlers.get_contact_phone,
        "add-birthday": handlers.add_birthday,
        "show-birthday": handlers.show_birthday,
        "birthdays": handlers.birthdays,
        "all": handlers.get_contacts_list,
    }

    book = AddressBook()

    r1 = Record("test1")
    book.add_record(r1)

    r2 = Record("test2")
    r2.add_birthday(Birthday("30.07.1992"))
    book.add_record(r2)

    r3 = Record("test3")
    r3.add_birthday(Birthday("30.09.1992"))
    book.add_record(r3)

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "help":
            print(handlers.render_help(command_to_handler))
            continue

        if command not in command_to_handler:
            print("Invalid command!")
            print(handlers.render_help(command_to_handler))
            continue

        output, should_terminate = command_to_handler[command](args, book)
        print(output)

        if should_terminate:
            break


if __name__ == "__main__":
    main()
