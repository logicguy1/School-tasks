# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-88b0f50)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 621,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_textIn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        bSizer1.Add( self.m_textIn, 0, wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

        self.m_button3 = wx.Button( self, wx.ID_ANY, u"Set Key", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

        self.m_textOut = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,-1 ), 0 )
        bSizer1.Add( self.m_textOut, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.btn_encrypt )
        self.m_button1.Bind( wx.EVT_BUTTON, self.btn_decrypt )
        self.m_button3.Bind( wx.EVT_BUTTON, self.open_dialog )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def btn_encrypt( self, event ):
        event.Skip()

    def btn_decrypt( self, event ):
        event.Skip()

    def open_dialog( self, event ):
        event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer3 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Frfr on god? gib key?", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.key_inp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        bSizer3.Add( self.key_inp, 0, wx.ALL, 5 )

        m_sdbSizer1 = wx.StdDialogButtonSizer()
        self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
        self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
        m_sdbSizer1.Realize();

        bSizer3.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer3 )
        self.Layout()
        bSizer3.Fit( self )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


