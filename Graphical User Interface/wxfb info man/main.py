import wx
import gui

class MySecondFrame(gui.MySecondFrame):
    def __init__(self, parent):
        gui.MySecondFrame.__init__(self, parent)

    def btn_load_val(self, event):
        MySecondFrame.Hide(self)

class mainFrame(gui.MainFrame): 
    """
    Class to manage the graphical user interface
    
    Attributes:
        fnavn: First name
        enavn: Last name
        gender: Gender
        birth: Birthday
        MySecondFrame: The second frame in the program

    Methods: 
        open_dialog: Open a dialog box
        quit: Exit the program
    """

    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.MySecondFrame = MySecondFrame(self)

        self.fnavn = ""
        self.enavn = ""
        self.gender = ""
        self.birth = ""

    def open_dialog(self, event):
        dlg = gui.MyDialog2(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            self.fnavn = dlg.m_textFname.GetValue() 
            self.enavn = dlg.m_Ename.GetValue() 

            self.birth = dlg.m_calendar.GetDate() 
            self.gender = ("Male", "Female")[dlg.m_radioGender.GetSelection()]

            print("name:", self.fnavn, self.enavn)
            print("birth:", self.birth)
            print("gender:", self.gender)

    def btn_open_window(self, event):
        print("btn")
        self.MySecondFrame.Show(True)

    def quit(self, event):
        exit()


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
