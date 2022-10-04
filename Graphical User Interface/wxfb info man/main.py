import wx
import gui

import crypt

class mainFrame(gui.MainFrame): 
    """
    Class to manage the graphical user interface
    
    Attributes:

    Methods: 

        quit: Exit the program
    """

    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
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

    def quit(self, event):
        exit()


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
