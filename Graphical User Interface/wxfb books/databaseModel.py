import sqlite3


class SqliteParser:
    """ A parser containing all the models used to intereact with the database """
    def __init__(self, database):
        self.dbName = database
        self.db = sqlite3.connect(database)
        self.cursor = self.db.cursor()

    def close_connection(self, db, cursor):
        """ Close the database connection """
        db.close()

    def get_books(self, order="name"):
        """ Get a list of all books in the database, default sort is name """
        self.cursor.execute(f"SELECT id, name, author, year, pages FROM books ORDER BY {order};")
        result = self.cursor.fetchall()

        return result

    def get_book(self, name):
        self.cursor.execute(f"SELECT id, name, author, year, pages FROM books WHERE name LIKE '%{name}%' ORDER BY name;")
        result = self.cursor.fetchall()

        return result

    def add_book(self, vals):
        self.cursor.execute("INSERT INTO books(name, author, year, pages) VALUES (?,?,?,?)", vals)


