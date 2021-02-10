import datetime

import database


# enter username
def username():
    name = input('Enter your Name: ')
    database._username_table(name)


# user choice
def user_choice():

    while True:
        print()
        print('Press 1 for enter a new Purchase: ')
        print('Press 2 for show all previous Purchase: ')
        print('Press 0 for Exit: ')
        choice = -1

        if choice < 0 or choice > 2:
            choice = int(input())
            if choice == 1:
                new_purchase()
            elif choice == 2:
                database.show_all_purchases()
            elif choice == 0:
                exit(0)


# input for new purchase
def new_purchase():
    product_name = input('Product name: ')
    time_date = datetime.datetime.now()
    date = str(time_date)[:10]
    amount = float(input('Amount: '))

    database.add_purchase([product_name, date, amount])


if __name__ == '__main__':
    username()
    user_choice()
