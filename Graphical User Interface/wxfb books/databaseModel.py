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

    def get_books(self, order="titel"):
        """ Get a list of all books in the database, default sort is name """
        self.cursor.execute(f"SELECT titel, enavn, fnavn, forlag, aar, id FROM books ORDER BY {order};")
        result = self.cursor.fetchall()

        return result

    def search_book(self, name):
        self.cursor.execute(f"SELECT id, titel, enavn, fnavn, forlag, aar FROM books WHERE titel LIKE '%{name}%' ORDER BY titel;")
        result = self.cursor.fetchall()

        return result

    def get_book(self, itemId):
        self.cursor.execute(f"SELECT id, titel, enavn, fnavn, forlag, aar FROM books WHERE id = ?;", (itemId,))
        return self.cursor.fetchone()

    def get_articles(self):
        self.cursor.execute(f"SELECT id, titel, enavn, fnavn, tidsskrift, dato FROM artikler;")
        return self.cursor.fetchall()

    def get_article(self, itemId):
        self.cursor.execute(f"SELECT titel, enavn, fnavn, tidsskrift, dato FROM artikler WHERE id = ?;", (itemId,))
        return self.cursor.fetchone()

    def update_article(self, vals):
        """ Update a book with new items """
        self.cursor.execute("UPDATE artikler SET titel = ?, enavn = ?, fnavn = ?, tidsskrift = ?, dato = ? WHERE id = ?", vals)
        self.db.commit()

    def update_book(self, vals):
        """ Update a book with new items """
        self.cursor.execute("UPDATE books SET titel = ?, enavn = ?, fnavn = ?, aar = ?, forlag = ? WHERE id = ?", vals)
        self.db.commit()

    def add_book(self, vals):
        self.cursor.execute("INSERT INTO books(titel, enavn, fnavn, forlag, aar) VALUES (?,?,?,?,?)", vals)


