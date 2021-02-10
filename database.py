import sqlite3

# connecting as a cursor
conn = sqlite3.connect('material.db')
c = conn.cursor()
user_name = ''


def _username_table(person_name):
    global user_name
    user_name = person_name
    c.execute(
        f'''CREATE TABLE IF NOT EXISTS {person_name}
        (description VARCHAR(255) NOT NULL, date DATE, amount NUMERIC NOT NULL) ''')

    conn.commit()


def add_purchase(new_purchase):
    # inserting new purchase in user table
    c.execute(f'INSERT INTO {user_name} VALUES (?,?,?);', new_purchase)
    conn.commit()


def show_all_purchases():
    # showing all previous purchase from username table
    for description, date, amt in c.execute(f'SELECT description, date, amount from {user_name}'):
        print(f'Description: {description} | Date: {date} | Amount {amt}')
