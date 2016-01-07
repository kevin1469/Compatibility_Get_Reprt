# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################
class MyFrame1 ( wx.Frame ):

  def __init__( self, parent ):
    wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "Compatibility Report Tool", pos = wx.DefaultPosition, size = wx.Size( 1450,925 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
    
    self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
    
    bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
    
    self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
    bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
    
    fgSizer212 = wx.FlexGridSizer( 5, 1, 0, 0 )
    fgSizer212.SetFlexibleDirection( wx.BOTH )
    fgSizer212.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
    
    fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
    fgSizer3.SetFlexibleDirection( wx.BOTH )
    fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
    
    self.account_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Account：", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.account_staticText.Wrap( -1 )
    fgSizer3.Add( self.account_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
    
    self.account_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
    fgSizer3.Add( self.account_textCtrl, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )
    
    self.password_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Password：", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
    self.password_staticText.Wrap( -1 )
    fgSizer3.Add( self.password_staticText, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.password_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_PASSWORD )
    fgSizer3.Add( self.password_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
    
    self.model_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Model：", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.model_staticText.Wrap( -1 )
    fgSizer3.Add( self.model_staticText, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
    
    bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
    
    self.model_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
    bSizer32.Add( self.model_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.version_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.version_staticText.Wrap( -1 )
    bSizer32.Add( self.version_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.brand_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
    bSizer32.Add( self.brand_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.version_staticText1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.version_staticText1.Wrap( -1 )
    bSizer32.Add( self.version_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.version_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
    bSizer32.Add( self.version_textCtrl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    
    fgSizer3.Add( bSizer32, 1, wx.EXPAND, 5 )
    
    self.testrail_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"TestRail ID：", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.testrail_staticText.Wrap( -1 )
    fgSizer3.Add( self.testrail_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.testrail_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
    self.testrail_textCtrl.SetMinSize( wx.Size( 250,-1 ) )
    
    fgSizer3.Add( self.testrail_textCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
    
    self.project_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Project ID：", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.project_staticText.Wrap( -1 )
    fgSizer3.Add( self.project_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.project_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
    self.project_textCtrl.SetMinSize( wx.Size( 250,-1 ) )
    
    fgSizer3.Add( self.project_textCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
    
    self.common_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Common ID：", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.common_staticText.Wrap( -1 )
    fgSizer3.Add( self.common_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    self.common_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
    fgSizer3.Add( self.common_textCtrl, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
    
    
    fgSizer212.Add( fgSizer3, 0, wx.TOP|wx.BOTTOM, 5 )
    
    bSizer14 = wx.BoxSizer( wx.VERTICAL )
    
    self.m_staticline12 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer14.Add( self.m_staticline12, 1, wx.EXPAND |wx.ALL, 5 )
    
    
    fgSizer212.Add( bSizer14, 1, wx.EXPAND, 5 )
    
    fgSizer13 = wx.FlexGridSizer( 3, 1, 0, 0 )
    fgSizer13.SetFlexibleDirection( wx.BOTH )
    fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
    
    bSizer41 = wx.BoxSizer( wx.VERTICAL )
    
    self.type_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Test Type：", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.type_staticText.Wrap( -1 )
    bSizer41.Add( self.type_staticText, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    type_checkListChoices = [u"All", u"VAST", u"ONVIF", u"ND8321", u"ND8322P", u"Milestone", u"Shepherd", u"Genetec-Omnicast", u"Genetec-Security center"]
    self.type_checkList = wx.CheckListBox( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,200 ), type_checkListChoices, wx.LB_ALWAYS_SB|wx.LB_MULTIPLE|wx.LB_SORT )
    bSizer41.Add( self.type_checkList, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
    
    self.m_staticline131 = wx.StaticLine( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer41.Add( self.m_staticline131, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 17 )
    
    self.ps_staticText = wx.StaticText( self.m_panel3, wx.ID_ANY, u"PS:", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.ps_staticText.Wrap( -1 )
    bSizer41.Add( self.ps_staticText, 0, wx.ALL, 5 )
    
    self.ps_textCtrl = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"Please inptu "'"PS"'" contents before click Get Report button.", wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE|wx.TE_WORDWRAP )
    bSizer41.Add( self.ps_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    fgSizer13.Add( bSizer41, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
    
    bSizer8 = wx.BoxSizer( wx.VERTICAL )
    
    self.m_panel7 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
    bSizer27 = wx.BoxSizer( wx.VERTICAL )
    
    self.m_staticline2 = wx.StaticLine( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer27.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
    
    bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

    self.get_button = wx.Button( self.m_panel7, wx.ID_ANY, u"&Get Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    bSizer25.Add( self.get_button, 0, wx.ALL, 5 )
    self.get_button.Bind(wx.EVT_BUTTON, self.getbutton, self.get_button)
    
    self.update_button = wx.Button( self.m_panel7, wx.ID_ANY, u"&Update Issue", wx.DefaultPosition, wx.DefaultSize, 0 )
    bSizer25.Add( self.update_button, 0, wx.ALL, 5 )
    self.update_button.Bind(wx.EVT_BUTTON, self.updatebutton)
    
    self.clear_button = wx.Button( self.m_panel7, wx.ID_ANY, u"&Clear Data", wx.DefaultPosition, wx.DefaultSize, 0 )
    bSizer25.Add( self.clear_button, 0, wx.ALL, 5 )
    
    self.exit_button = wx.Button( self.m_panel7, wx.ID_ANY, u"&Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
    bSizer25.Add( self.exit_button, 0, wx.ALL, 5 )
    self.exit_button.Bind(wx.EVT_BUTTON, self.closebutton, self.exit_button)
    self.exit_button.Bind(wx.EVT_CLOSE, self.closewindow)
    
    bSizer27.Add( bSizer25, 1, wx.ALL, 5 )
    
    bSizer23 = wx.BoxSizer( wx.VERTICAL )
    
    bSizer27.Add( bSizer23, 0, wx.EXPAND, 5 )
      
    self.m_panel7.SetSizer( bSizer27 )
    self.m_panel7.Layout()
    bSizer27.Fit( self.m_panel7 )
    bSizer8.Add( self.m_panel7, 0, wx.EXPAND, 5 )
        
    fgSizer13.Add( bSizer8, 1, wx.EXPAND, 5 )
    
    
    fgSizer212.Add( fgSizer13, 1, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
    
    
    bSizer11.Add( fgSizer212, 0, wx.ALL, 5 )
    
    bSizer21 = wx.BoxSizer( wx.VERTICAL )
    
    self.m_panel6 = wx.Panel( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
    bSizer22 = wx.BoxSizer( wx.VERTICAL )
    
    self.m_staticline15 = wx.StaticLine( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
    bSizer22.Add( self.m_staticline15, 1, wx.ALL|wx.EXPAND, 5 )
    
    
    self.m_panel6.SetSizer( bSizer22 )
    self.m_panel6.Layout()
    bSizer22.Fit( self.m_panel6 )
    bSizer21.Add( self.m_panel6, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
    
    
    bSizer11.Add( bSizer21, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
    
    
    self.m_panel3.SetSizer( bSizer11 )
    self.m_panel3.Layout()
    bSizer11.Fit( self.m_panel3 )
    bSizer1.Add( self.m_panel3, 0, wx.EXPAND, 5 )
    
    bSizer6 = wx.BoxSizer( wx.VERTICAL )
    
    self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
    self.m_scrolledWindow1.SetScrollRate( 5, 5 )
    bSizer28 = wx.BoxSizer( wx.VERTICAL )
    
    self.omnicast_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Genetec-Omnicast Report", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
    self.omnicast_staticText.Wrap( -1 )
    bSizer28.Add( self.omnicast_staticText, 0, wx.ALL, 5 )
    
    self.omnicast_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.omnicast_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline13 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.security_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Genetec-Security center Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.security_staticText.Wrap( -1 )
    bSizer28.Add( self.security_staticText, 0, wx.ALL, 5 )
    
    self.security_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.security_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline6 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.milestone_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Milestone Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.milestone_staticText.Wrap( -1 )
    bSizer28.Add( self.milestone_staticText, 0, wx.ALL, 5 )
    
    self.milestone_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.milestone_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline7 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline7, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.nd8321_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"ND8321 Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.nd8321_staticText.Wrap( -1 )
    bSizer28.Add( self.nd8321_staticText, 0, wx.ALL, 5 )
    
    self.nd8321_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.nd8321_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline14 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.nd8322p_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"ND8322P Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.nd8322p_staticText.Wrap( -1 )
    bSizer28.Add( self.nd8322p_staticText, 0, wx.ALL, 5 )
    
    self.nd8322p_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.nd8322p_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
  
    self.m_staticline8 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.onvif_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"ONVIF Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.onvif_staticText.Wrap( -1 )
    bSizer28.Add( self.onvif_staticText, 0, wx.ALL, 5 )
    
    self.onvif_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.onvif_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline9 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.shpherd_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Shepherd Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.shpherd_staticText.Wrap( -1 )
    bSizer28.Add( self.shpherd_staticText, 0, wx.ALL, 5 )
    
    self.shpherd_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.shpherd_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline10 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
    
    self.vast_staticText = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"VAST Report", wx.DefaultPosition, wx.DefaultSize, 0 )
    self.vast_staticText.Wrap( -1 )
    bSizer28.Add( self.vast_staticText, 0, wx.ALL, 5 )
    
    self.vast_textCtrl = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,800 ), wx.HSCROLL|wx.TE_AUTO_URL|wx.TE_LEFT|wx.TE_MULTILINE )
    bSizer28.Add( self.vast_textCtrl, 1, wx.ALL|wx.EXPAND, 5 )
    
    self.m_staticline11 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
    bSizer28.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
    
    
    self.m_scrolledWindow1.SetSizer( bSizer28 )
    self.m_scrolledWindow1.Layout()
    bSizer28.Fit( self.m_scrolledWindow1 )
    bSizer6.Add( self.m_scrolledWindow1, 1, wx.EXPAND, 5 )
    
    
    bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )
    
    
    self.SetSizer( bSizer1 )
    self.Layout()
    self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
    
    self.Centre( wx.BOTH )
	
  def __del__( self ):
    pass
	

