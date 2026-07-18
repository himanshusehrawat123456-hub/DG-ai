# DG AI Database System

import sqlite3


def connect_db():

    connection = sqlite3.connect("dgai.db")

    return connection



def create_table():

    db = connect_db()

    cursor = db.cursor()


    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY,
        name TEXT,
        data TEXT

    )

    """)


    db.commit()

    db.close()

    print("Database ready")



def add_data(name, data):

    db = connect_db()

    cursor = db.cursor()


    cursor.execute(

        "INSERT INTO users(name, data) VALUES(?,?)",

        (name, data)

    )


    db.commit()

    db.close()


    print("Data saved")



def show_data():

    db = connect_db()

    cursor = db.cursor()


    cursor.execute("SELECT * FROM users")


    rows = cursor.fetchall()


    for row in rows:

        print(row)


    db.close()
