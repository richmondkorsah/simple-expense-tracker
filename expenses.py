import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS expenses(
    item TEXT NOT NULL,
    category TEXT NOT NULL,
    date DATE NOT NULL,
    amount REAL NOT NULL
)''')


def add_expenses(item, category, date, amount):
    c.execute("INSERT INTO expenses VALUES (?, ?, ?, ?)", (item, category, date, amount))
    conn.commit()


def get_expenses():
    c.execute("SELECT * FROM expenses")
    return c.fetchall()


add_expenses(item=input("Enter Item: "),
             category=input("Enter Category: "),
             date=input("Enter Date: "),
             amount=float(input("Enter Amount: "))
             )
