import wx
import gui

import databaseModel as model


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

        self.db = model.SqliteParser("base.db")

        # Update the table on boot
        self.btn_update_table(None)

    def btn_update_table(self, event):
        """ Update the table with new values from the database """
        self.m_dataView_books.DeleteAllItems()
        books = self.db.get_books()

        for i in books:
            row = (i[1],i[2],str(i[3]))
            self.m_dataView_books.AppendItem(row)

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


    def quit(self, event):
        exit()

app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
