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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 555,379 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataView_books = wx.dataview.DataViewListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), 0 )
		self.m_dataView_books.SetMinSize( wx.Size( 1000,200 ) )

		self.m_dataViewListColumn17 = self.m_dataView_books.AppendTextColumn( u"ID", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn1 = self.m_dataView_books.AppendTextColumn( u"Book name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn2 = self.m_dataView_books.AppendTextColumn( u"Author", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn15 = self.m_dataView_books.AppendTextColumn( wx.EmptyString, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn16 = self.m_dataView_books.AppendTextColumn( u"Year", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn3 = self.m_dataView_books.AppendTextColumn( u"Publisher", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer5.Add( self.m_dataView_books, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"Books", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_dataView_articles = wx.dataview.DataViewListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), 0 )
		self.m_dataView_articles.SetMinSize( wx.Size( 1000,200 ) )

		self.m_dataViewListColumn11 = self.m_dataView_articles.AppendTextColumn( u"ID", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn21 = self.m_dataView_articles.AppendTextColumn( u"Name", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn31 = self.m_dataView_articles.AppendTextColumn( u"Author", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn18 = self.m_dataView_articles.AppendTextColumn( wx.EmptyString, wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn19 = self.m_dataView_articles.AppendTextColumn( u"Journal", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		self.m_dataViewListColumn20 = self.m_dataView_articles.AppendTextColumn( u"Date", wx.dataview.DATAVIEW_CELL_INERT, -1, wx.ALIGN_LEFT, wx.dataview.DATAVIEW_COL_RESIZABLE )
		bSizer51.Add( self.m_dataView_articles, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer51 )
		self.m_panel2.Layout()
		bSizer51.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Articles", True )

		bSizer8.Add( self.m_notebook1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Add New Record", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button3, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Print List", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Delete record", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_dataView_books.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.activate, id = wx.ID_ANY )
		self.m_dataView_articles.Bind( wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED, self.activate, id = wx.ID_ANY )
		self.m_button3.Bind( wx.EVT_BUTTON, self.btn_add_book )
		self.m_button5.Bind( wx.EVT_BUTTON, self.get_output )
		self.m_button4.Bind( wx.EVT_BUTTON, self.btn_delete_record )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def activate( self, event ):
		event.Skip()


	def btn_add_book( self, event ):
		event.Skip()

	def get_output( self, event ):
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 336,315 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer6.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.m_text_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_name.SetMinSize( wx.Size( 310,-1 ) )

		bSizer6.Add( self.m_text_name, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		bSizer6.Add( self.m_staticText8, 0, wx.ALL, 5 )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_text_auth1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_auth1.SetMinSize( wx.Size( 150,-1 ) )

		bSizer9.Add( self.m_text_auth1, 0, wx.ALL, 5 )

		self.m_text_auth2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_auth2.SetMinSize( wx.Size( 150,-1 ) )

		bSizer9.Add( self.m_text_auth2, 0, wx.ALL, 5 )


		bSizer6.Add( bSizer9, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer10.SetMinSize( wx.Size( -1,90 ) )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Year", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer11.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_text_year = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_year.SetMinSize( wx.Size( 150,-1 ) )

		bSizer11.Add( self.m_text_year, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 0, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Publisher", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer12.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_text_pub = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_text_pub.SetMinSize( wx.Size( 150,-1 ) )

		bSizer12.Add( self.m_text_pub, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer12, 0, wx.EXPAND, 5 )


		bSizer6.Add( bSizer10, 0, wx.EXPAND, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1Save = wx.Button( self, wx.ID_SAVE )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Save )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer6.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class PrintDialog
###########################################################################

class PrintDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		self.m_sdbSizer2Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer2.AddButton( self.m_sdbSizer2Cancel )
		m_sdbSizer2.Realize();

		bSizer11.Add( m_sdbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()
		bSizer11.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


