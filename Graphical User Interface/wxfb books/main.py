import wx
import gui
import datetime
from pubsub import pub as pubb

import databaseModel as model


class LogFrame(gui.LogFrame):
    def __init__(self, parent):
        gui.LogFrame.__init__(self, parent)
        pubb.subscribe(self.listener, "MyMainFrame")


    def listener(self, message):
        msg = datetime.datetime.now().strftime("%H:%M:%S %m/%d/%Y  | ")
        msg += message + "\n"

        self.m_listBox1.InsertItems([msg,], 0)


    def quit(self, event):
        self.Show(False)


class BookPreview(gui.BookPreview):
    def __init__(self, parent):
        gui.BookPreview.__init__(self, parent)


    def btn_done(self, event):
        """ Hide the frame """
        BookPreview.Hide(self)


class mainFrame(gui.MainFrame): 
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.BookPreview = BookPreview(self)
        self.LogFrame = LogFrame(self)

        self.db = model.SqliteParser("litteratur.db", pubb)

        # Update the table on boot
        self.btn_update_table(None)


    def get_row(self):
        """ Get the selected row in the active listview """
        selection = self.m_notebook1.GetSelection()
        if selection == 0:
            row = self.m_dataView_books.GetSelectedRow()
            book = self.m_dataView_books.GetTextValue(row, 0)

            return book, row, selection 
        elif selection == 1:
            row = self.m_dataView_articles.GetSelectedRow()
            article = self.m_dataView_articles.GetTextValue(row, 0)

            return article, row, selection      
        else:
            return -1


    def btn_update_table(self, event):
        """ Update the table with new values from the database """
        self.m_dataView_books.DeleteAllItems()
        books = self.db.get_books()

        for i in books:
            row = (str(i[5]), i[0], i[2], i[1], str(i[4]), i[3],) 
            self.m_dataView_books.AppendItem(row)

        self.m_dataView_articles.DeleteAllItems()
        articles = self.db.get_articles()
        for i in articles:
            row = (str(i[0]), i[1], i[3], i[2], i[4], i[5]) 
            self.m_dataView_articles.AppendItem(row)


    def open_record(self, itemId, selection):
        """ Open a popup with the active record to allow for editing """

        if selection == 0:
            # We are a book
            book = self.db.get_book(itemId)

            dlg = gui.NewBookDialoge(self)

            dlg.m_text_name.write(book[1])
            dlg.m_text_auth1.write(book[3])
            dlg.m_text_auth2.write(book[2])
            dlg.m_text_year.write(str(book[5]))
            dlg.m_text_pub.write(book[4])

            result = dlg.ShowModal()

            if result == wx.ID_OK:
                name = dlg.m_text_name.GetValue()
                author = dlg.m_text_auth1.GetValue()
                author2 = dlg.m_text_auth2.GetValue()
                year = dlg.m_text_year.GetValue()
                pub = dlg.m_text_pub.GetValue()

                self.db.update_book((name, author2, author, year, pub, itemId))
                self.btn_update_table(None)

        elif selection == 1:
            # We are an article
            article = self.db.get_article(itemId)

            dlg = gui.NewBookDialoge(self)

            dlg.m_text_name.write(article[0])
            dlg.m_text_auth1.write(article[2])
            dlg.m_text_auth2.write(article[1])
            dlg.m_text_year.write(str(article[4]))
            dlg.m_text_pub.write(article[3])

            result = dlg.ShowModal()

            if result == wx.ID_OK:
                name = dlg.m_text_name.GetValue()
                author = dlg.m_text_auth1.GetValue()
                author2 = dlg.m_text_auth2.GetValue()
                year = dlg.m_text_year.GetValue()
                pub = dlg.m_text_pub.GetValue()

                self.db.update_article((name, author2, author, pub, year, itemId))
                self.btn_update_table(None)

        self.btn_update_table(None)


    def activate(self, event):
        """ Triggers when we click on one of the list boxes"""
        itemId, row, selection = self.get_row()
        print(itemId, row, selection)

        self.open_record(itemId, selection)


    def btn_lookup(self, event):
        """ Get the selected row in the table """
        # Get selected row
        row = self.m_dataView_books.GetSelectedRow()
        # If there is no row selected
        if row == -1:
            return -1
        # Book name
        book = self.m_dataView_books.GetTextValue(row, 0)
        bookData = [str(i) for i in self.db.get_book(book)[0]]
        print(bookData)

        # Show dialoge
        self.BookPreview.Show(True)
        self.BookPreview.m_dataView_bookIndevidual.DeleteAllItems()
        self.BookPreview.m_dataView_bookIndevidual.AppendItem(bookData)


    def get_output(self, event):
        dlg = gui.PrintDialog(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            books = self.db.get_books()
            articles = self.db.get_articles()

            out = ""
            for i in books:
                out += ", ".join(map(str, i[:-1])) + "\n"
            for i in articles:
                out += ", ".join(map(str, i[1:])) + "\n"

            with open("liste.txt", "w") as file:
                file.write(out)


    def btn_add_book(self, event):
        dlg = gui.NewBookDialoge(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            name = dlg.m_text_name.GetValue()
            author = dlg.m_text_auth.GetValue()
            year = dlg.m_text_year.GetValue()
            pages = dlg.m_text_pages.GetValue()

            self.db.add_book((name, author, year, pages))
            self.btn_update_table(None)


    def btn_delete_record(self, event):
        # Get selected row
        row = self.m_dataView_books.GetSelectedRow()
        # If there is no row selected
        if row == -1:
            return -1
        # Book name
        book = self.m_dataView_books.GetTextValue(row, 0)

    
    def open_log(self, event):
        self.LogFrame.Show(True)


    def quit(self, event):
        exit()

app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
