from json import dump
from os import path
from time import sleep
def create_database(db_name):
    from sqlite3 import connect
    conn = connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS combinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        length INTEGER NOT NULL,
        symbol BOOLEAN NOT NULL,
        space BOOLEAN NOT NULL,
        sha256 TEXT NOT NULL
    )''')
    c.close()
    sleep(2)
    print("Database file created.")

    return True


def create_config(db_name, max_length):
    default_config = {
        "lower_letters": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "upper_letters": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        "digits": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "symbols": ["!", "#", "$", "%", "&", "(", ")", "*", "+", "-", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"],
        "symbol": True,
        "digit": True,
        "space": True,
        "length": max_length,
        "db_name": db_name
    }
    while True:
        config_file = "config.json"
        if not path.isfile(config_file):
            with open(config_file, 'w') as file:
                dump(default_config, file)
            print("Config file created.")
            sleep(2)
            break
        else:
            print("Config file already exists.")
            sleep(2)
# run this func if you want to create a new database
db_name = input("Enter database name: ")
max_length = int(input("Enter max length of password combinations: "))
db_name += ".db"
try:
    sleep(2)
    create_config(db_name, max_length)
    create_database(db_name)
except Exception as e:
    print(e)

