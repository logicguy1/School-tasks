# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-88b0f50)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"open dialog", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"open window", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.m_button6, 0, wx.ALL, 5 )


		self.SetSizer( bSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.open_dialog )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btn_open_window )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def open_dialog( self, event ):
		event.Skip()

	def btn_open_window( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 442,466 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Fornavn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_textFname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_textFname, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Efternavn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer6.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_Ename = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_Ename, 0, wx.ALL, 5 )


		bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )

		self.m_calendar = wx.adv.CalendarCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.CAL_SHOW_HOLIDAYS )
		bSizer5.Add( self.m_calendar, 0, wx.ALL, 5 )

		m_radioGenderChoices = [ u"Mand", u"Kvinde" ]
		self.m_radioGender = wx.RadioBox( self, wx.ID_ANY, u"Køn", wx.DefaultPosition, wx.DefaultSize, m_radioGenderChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioGender.SetSelection( 0 )
		bSizer5.Add( self.m_radioGender, 0, wx.ALL, 5 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer5.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MySecondFrame
###########################################################################

class MySecondFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Joe mam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer7.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Load value", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button5, 0, wx.ALL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.btn_load_val )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn_load_val( self, event ):
		event.Skip()


