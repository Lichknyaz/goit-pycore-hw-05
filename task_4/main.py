from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error_change(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone from the database to change please."
        except KeyError:
            return "No such name in the database, give me valid name please"
        
    return inner

@input_error_change
def change_contact(args, contacts):
    # if len (args) == 2:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Phone number updated."
        else:
            raise KeyError
    # else:
        # return "Not correct entry"
    
def input_error_add(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone please."

    return inner

@input_error_add
def add_contact(args, contacts):
    # if len (args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added"
    # else:
        # return "Not correct entry"

def input_error_show(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Give me name and phone from the database to change please."
        except IndexError:
            return "Give me name please."
        except KeyError:
            return "Give me name from database please."
    return inner

@input_error_show
def show_phone (args: list, contacts: dict):
    # if len (args) == 1:
        # phone = contacts.get(args[0])
        phone = contacts[args[0]]
        # if phone == None:
            # return "No such name" 
        return phone
    # else:
        return "Not correct entry"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(contacts)
        elif command == "phone":
                print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
