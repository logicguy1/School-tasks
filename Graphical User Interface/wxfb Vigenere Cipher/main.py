import wx
import gui

import crypt

class mainFrame(gui.MainFrame): 
    """
    Class to manage the graphical user interface
    
    Attributes:
        key: The key to use for encryption

    Methods: 

        btn_encrypt: Encrypt the text
        btn_decrypt: Decrypt the text
        quit: Exit the program
    """

    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.key = "AA"

    def btn_encrypt(self, event):
        text = crypt.Crypt(self.key).encrypt(self.m_textIn.GetValue())
        self.m_textOut.SetValue(text)

    def btn_decrypt(self, event):
        text = crypt.Crypt(self.key).decrypt(self.m_textIn.GetValue())
        self.m_textOut.SetValue(text)

    def open_dialog(self, event):
        dlg = gui.MyDialog1(self)
        result = dlg.ShowModal()

        if result == wx.ID_OK:
            self.key = dlg.key_inp.GetValue() 
            print("newKey:", self.key)

    def quit(self, event):
        exit()


app = wx.App(False)
frame = mainFrame(None)
frame.Show(True)
app.MainLoop()
