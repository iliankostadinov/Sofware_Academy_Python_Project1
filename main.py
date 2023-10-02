import clients_data


def validate_user_name(username):
    for indx, client in enumerate(clients_data.clients_data):
        if client['name'] == username:
            return indx
    return "Not exist"


def validate_pin_code(user_indx):

    number_of_tries = 3
    while number_of_tries > 0:
        while True:
            try:
                pin_code = int(input("Please enter your pin code: "))
                break
            except ValueError:
                print("Your pin code should contain only numbers!!!")
        if pin_code == clients_data.clients_data[user_indx]['pin']:
            print(f"Your balance is\
                  {clients_data.clients_data[user_indx]['balance']}")
            return True
        else:
            number_of_tries -= 1
    print("Your card is blocked!")
    return False


def ask_for_operation(user_indx):
    operation = input("What you want to do, pull, push or view balance? ")
    match operation:
        case "pull":
            pull(user_indx)
        case "push":
            push(user_indx)
        case "balance":
            balance(user_indx)
        case _:
            print("Operation which you requested is not valid!")


def pull(user_indx):
    while True:
        try:
            sum_to_pull = float(input("Please enter what amount you want to pull: "))
        except ValueError:
            print("You should enter valid sum, please use only numbers")
        if sum_to_pull > clients_data.clients_data[user_indx]['balance']:
            print("You don't have enough money, please enter lower value! ")
        else:
            break
    new_balance = clients_data.clients_data[user_indx]['balance'] - sum_to_pull
    clients_data.clients_data[user_indx]['balance'] = new_balance
    print(f"Your new balance is {clients_data.clients_data[user_indx]['balance']}")
    quit(0)


def push(user_indx):
    while True:
        try:
            sum_to_push = float(input("Please enter with what amount you want to feed your bill: "))
            break
        except ValueError:
            print("You should enter valid sum, please use only numbers")
    new_balance = clients_data.clients_data[user_indx]['balance'] + sum_to_push
    clients_data.clients_data[user_indx]['balance'] = new_balance
    print(f"Your new balance is {clients_data.clients_data[user_indx]['balance']}")
    quit(0)


def balance(user_indx):
    print(f"Your balance is {clients_data.clients_data[user_indx]['balance']}")
    quit(0)


def main():
    while True:

        userName = input("Please enter your name or write quit to exit: ")
        if userName == "quit":
            quit(0)
        valid_user_indx = validate_user_name(userName)
        if valid_user_indx != "Not exist":
            if validate_pin_code(valid_user_indx):
                ask_for_operation(valid_user_indx)
        else:
            print(f"{userName} is not our client")


if __name__ == "__main__":
    main()
