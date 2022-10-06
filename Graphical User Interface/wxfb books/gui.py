# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-88b0f50)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataView_books = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), 0 )
		self.m_dataView_books.SetMinSize( wx.Size( 1000,200 ) )

		self.m_dataViewListColumn1 = self.m_dataView_books.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn2 = self.m_dataView_books.AppendTextColumn( u"Author", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn3 = self.m_dataView_books.AppendTextColumn( u"Year", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer8.Add( self.m_dataView_books, 0, wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btn_lookup = wx.Button( self, wx.ID_ANY, u"Lookup Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_btn_lookup, 0, wx.ALL, 5 )

		self.m_btn_update = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_btn_update, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Add New Record", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Delete record", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_btn_lookup.Bind( wx.EVT_BUTTON, self.btn_lookup )
		self.m_btn_update.Bind( wx.EVT_BUTTON, self.btn_update_table )
		self.m_button3.Bind( wx.EVT_BUTTON, self.btn_add_book )
		self.m_button4.Bind( wx.EVT_BUTTON, self.btn_delete_record )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn_lookup( self, event ):
		event.Skip()

	def btn_update_table( self, event ):
		event.Skip()

	def btn_add_book( self, event ):
		event.Skip()

	def btn_delete_record( self, event ):
		event.Skip()


###########################################################################
## Class BookPreview
###########################################################################

class BookPreview ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataView_bookIndevidual = wx.dataview.DataViewListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_dataView_bookIndevidual.SetMinSize( wx.Size( 600,70 ) )

		self.m_dataViewListColumn4 = self.m_dataView_bookIndevidual.AppendTextColumn( u"Id", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn5 = self.m_dataView_bookIndevidual.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn6 = self.m_dataView_bookIndevidual.AppendTextColumn( u"Author", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn7 = self.m_dataView_bookIndevidual.AppendTextColumn( u"Year", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn8 = self.m_dataView_bookIndevidual.AppendTextColumn( u"Pages", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer10.Add( self.m_dataView_bookIndevidual, 0, wx.ALL, 5 )

		self.m_btn_done = wx.ToggleButton( self, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_btn_done, 0, wx.ALL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_btn_done.Bind( wx.EVT_TOGGLEBUTTON, self.btn_done )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def btn_done( self, event ):
		event.Skip()


###########################################################################
## Class NewBookDialoge
###########################################################################

class NewBookDialoge ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 336,242 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		gSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_name.SetMinSize( wx.Size( 150,-1 ) )

		gSizer3.Add( self.m_text_name, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.m_text_auth = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_auth.SetMinSize( wx.Size( 150,-1 ) )

		gSizer3.Add( self.m_text_auth, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer3.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_text_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_year.SetMinSize( wx.Size( 150,-1 ) )

		gSizer3.Add( self.m_text_year, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Pages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_text_pages = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_pages.SetMinSize( wx.Size( 150,-1 ) )

		gSizer3.Add( self.m_text_pages, 0, wx.ALL, 5 )


		bSizer6.Add( gSizer3, 1, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer6.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


