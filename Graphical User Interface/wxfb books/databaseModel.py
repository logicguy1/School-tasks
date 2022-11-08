import sqlite3



class SqliteParser:
    """ A parser containing all the models used to intereact with the database """
    def __init__(self, database, pubb):
        self.dbName = database
        self.db = sqlite3.connect(database)
        self.cursor = self.db.cursor()
        self.pubb = pubb


    def active_log(func):
        def wrapper(self, *args, **kwargs):
            self.pubb.sendMessage("MyMainFrame", message = f"{func.__name__} - {args} - {func.__doc__}")
            return func(self, *args, **kwargs)
        return wrapper


    @active_log
    def close_connection(self, db, cursor):
    """ Close the database connection """
        db.close()

    @active_log
    def get_books(self, order="titel"):
        """ Get a list of all books in the database, default sort is name """
        self.cursor.execute(f"SELECT titel, enavn, fnavn, forlag, aar, id FROM books ORDER BY {order};")
        result = self.cursor.fetchall()

        return result

    @active_log
    def search_book(self, name):
        """ Search for a book in the db """
        self.cursor.execute(f"SELECT id, titel, enavn, fnavn, forlag, aar FROM books WHERE titel LIKE '%{name}%' ORDER BY titel;")
        result = self.cursor.fetchall()

        return result

    @active_log
    def get_book(self, itemId):
        """ Get a book from the database """
        self.cursor.execute(f"SELECT id, titel, enavn, fnavn, forlag, aar FROM books WHERE id = ?;", (itemId,))
        return self.cursor.fetchone()

    @active_log
    def get_articles(self):
        """ Get all the articales from the db """
        self.cursor.execute(f"SELECT id, titel, enavn, fnavn, tidsskrift, dato FROM artikler;")
        return self.cursor.fetchall()

    @active_log
    def get_article(self, itemId):
        """ Get all the articales """
        self.cursor.execute(f"SELECT titel, enavn, fnavn, tidsskrift, dato FROM artikler WHERE id = ?;", (itemId,))
        return self.cursor.fetchone()

    @active_log
    def update_article(self, vals):
        """ Update a book with new items """
        self.cursor.execute("UPDATE artikler SET titel = ?, enavn = ?, fnavn = ?, tidsskrift = ?, dato = ? WHERE id = ?", vals)
        self.db.commit()

    @active_log
    def update_book(self, vals):
        """ Update a book with new items """
        self.cursor.execute("UPDATE books SET titel = ?, enavn = ?, fnavn = ?, aar = ?, forlag = ? WHERE id = ?", vals)
        self.db.commit()

    @active_log
    def add_book(self, vals):
        """ Add a book to the database """
        self.cursor.execute("INSERT INTO books(titel, enavn, fnavn, forlag, aar) VALUES (?,?,?,?,?)", vals)


