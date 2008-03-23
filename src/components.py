"""
PureMVC Python Demo - wxPython Employee Admin 
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
"""

import wx
import wx.grid
import enum

class WxApp(wx.App):
	
	appFrame = None
	
	def OnInit(self):
		self.appFrame = AppFrame()
		self.appFrame.Show()
		#self.SetTopWindow(self.frame)
		
		return True

class AppFrame(wx.Frame):
	
	userForm = None
	userList = None
	rolePanel = None
	
	def __init__(self):
		wx.Frame.__init__(self,parent=None, id=-1, title="PureMVC Demo",size=(660,535))
		self.rolePanel = RolePanel(self)
		self.userList = UserList(self)
		self.userForm = UserForm(self)
	
class RolePanel(wx.Panel):
	
	evt_ADD_ROLE = wx.NewEventType()
	EVT_ADD_ROLE = wx.PyEventBinder(evt_ADD_ROLE, 1)
	
	evt_REMOVE_ROLE = wx.NewEventType()
	EVT_REMOVE_ROLE = wx.PyEventBinder(evt_REMOVE_ROLE, 2)

	user = None
	selectedRole = None
	
	roleList = None
	roleCombo = None
	addBtn = None
	removeBtn = None
	
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,id=1,pos=(330,220),size=(330,300))
		#self.SetBackgroundColour('Red')
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		hboxBottom = wx.BoxSizer(wx.HORIZONTAL)
		
		self.roleList = wx.ListBox(self,-1,size=(300,200))
		self.roleList.Bind(wx.EVT_LISTBOX, self.onListClick)
		self.roleCombo = wx.ComboBox(self, -1, size=wx.DefaultSize)
		self.roleCombo.Bind(wx.EVT_COMBOBOX, self.onComboClick)
		self.addBtn = wx.Button(self, -1, "Add")
		self.addBtn.Disable()
		self.addBtn.Bind(wx.EVT_BUTTON, self.onAdd)
		self.removeBtn = wx.Button(self, -1, "Remove")
		self.removeBtn.Disable()
		self.removeBtn.Bind(wx.EVT_BUTTON, self.onRemove)
		
		hboxBottom.Add(self.roleCombo, 0, wx.RIGHT,10)
		hboxBottom.Add(self.addBtn, 0, wx.RIGHT,10)
		hboxBottom.Add(self.removeBtn, 0, wx.RIGHT,10)
		vbox.Add(self.roleList, 1, wx.TOP|wx.CENTER,10)
		vbox.Add(hboxBottom, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT,10)

		self.SetAutoLayout(True)
		self.SetSizer(vbox)
		self.Layout()
	
	def updateRoleList(self,items):
		self.roleList.Clear()
		self.roleList.AppendItems(items)
	
	def updateRoleCombo(self,choices, default):
		self.roleCombo.Clear()
		self.roleCombo.AppendItems(choices)
		self.roleCombo.SetValue(default)
	
	def onComboClick(self, evt):
		if not self.roleCombo.GetValue() == enum.ROLE_NONE_SELECTED:
			self.addBtn.Enable()
		else:
			self.addBtn.Disable()
		self.roleList.SetSelection(-1)
		self.selectedRole=self.roleCombo.GetValue()
	
	def onListClick(self, evt):
		if not self.roleList.GetSelection() == enum.ROLE_NONE_SELECTED:
			self.removeBtn.Enable()
		else:
			self.removeBtn.Disable()
		self.roleCombo.SetValue(enum.ROLE_NONE_SELECTED)
		self.selectedRole=self.roleList.GetStringSelection()
	
	def onAdd(self, evt):
		self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_ADD_ROLE, self.GetId()))
	
	def onRemove(self,evt):
		self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_REMOVE_ROLE, self.GetId()))

class UserList(wx.Panel):
	
	evt_USER_SELECTED = wx.NewEventType()
	EVT_USER_SELECTED = wx.PyEventBinder(evt_USER_SELECTED, 1)
	
	evt_NEW = wx.NewEventType()
	EVT_NEW = wx.PyEventBinder(evt_NEW, 1)
	
	evt_DELETE = wx.NewEventType()
	EVT_DELETE = wx.PyEventBinder(evt_DELETE, 1)
	
	userGrid = None
	newBtn = None
	deleteBtn = None
	
	users = None
	selectedUser = None
	
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,id=2,size=(660,220))
		#self.SetBackgroundColour('Blue')
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		hboxBottom = wx.BoxSizer(wx.HORIZONTAL)
		
		self.userGrid = wx.grid.Grid(self,-1, )
		self.userGrid.Bind(wx.grid.EVT_GRID_SELECT_CELL,self.onSelect)
		self.userGrid.Bind(wx.grid.EVT_GRID_CELL_CHANGE,self.onSelect)
		self.userGrid.CreateGrid(6,6)
		self.userGrid.SetColLabelValue(0,"Username")
		self.userGrid.SetColLabelValue(1,"First Name")
		self.userGrid.SetColLabelValue(2,"Last Name")
		self.userGrid.SetColLabelValue(3,"Email")
		self.userGrid.SetColLabelValue(4,"Department")
		self.userGrid.SetColLabelValue(5,"Password")
		
		self.newBtn = wx.Button(self, -1, "New")
		self.newBtn.Bind(wx.EVT_BUTTON, self.onNew)
		self.deleteBtn = wx.Button(self, -1, "Delete")
		self.deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)
		
		hboxBottom.Add(self.newBtn, 0, wx.RIGHT,10)
		hboxBottom.Add(self.deleteBtn, 0, wx.RIGHT,10)
		vbox.Add(self.userGrid, 0, wx.ALL|wx.ALIGN_LEFT,10)
		vbox.Add(hboxBottom, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_RIGHT,10)

		self.SetAutoLayout(True)
		self.SetSizer(vbox)
		self.Layout()
	
	def updateUserGrid(self, users):
		self.userGrid.ClearGrid()
		self.users = users
		for i in range(len(users)):
			self.userGrid.SetCellValue(i, 0, users[i].username)
			self.userGrid.SetCellValue(i, 1, users[i].fname)
			self.userGrid.SetCellValue(i, 2, users[i].lname)
			self.userGrid.SetCellValue(i, 3, users[i].email)
			self.userGrid.SetCellValue(i, 4, users[i].department)
			self.userGrid.SetCellValue(i, 5, users[i].password)
		self.userGrid.AutoSize()
	
	def onSelect(self,evt):
		try:
			self.selectedUser = self.users[evt.GetRow()]
			self.userGrid.SelectRow(evt.GetRow())
			self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_USER_SELECTED, self.GetId()))
		except IndexError:
			pass
	
	def deSelect(self):
		self.userGrid.SelectRow(-1)
	
	def onNew(self, evt):
		self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_NEW, self.GetId()))
		self.deSelect()
		
	def onDelete(self, evt):
		if self.selectedUser:
			self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_DELETE, self.GetId()))
			self.deSelect()

class UserForm(wx.Panel):
	
	evt_ADD     = wx.NewEventType()
	EVT_ADD     = wx.PyEventBinder(evt_ADD, 1)
	evt_UPDATE 	= wx.NewEventType()
	EVT_UPDATE  = wx.PyEventBinder(evt_UPDATE, 1)
	evt_CANCEL 	= wx.NewEventType()
	EVT_CANCEL  = wx.PyEventBinder(evt_CANCEL, 1)

	MODE_ADD 	= "modeAdd";
	MODE_EDIT 	= "modeEdit";
	
	user = None
	mode = None
	
	usernameInput = None
	firstInput = None
	lastInput = None
	emailInput = None
	passwordInput = None
	confirmInput = None
	departmentCombo = None
	addBtn = None
	cancelBtn = None
	
	def __init__(self,parent):
		wx.Panel.__init__(self,parent,id=3,pos=(0,220),size=(330,300))
		#self.SetBackgroundColour('Green')
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		hboxBottom = wx.BoxSizer(wx.HORIZONTAL)
		
		grid = wx.GridSizer(7,2,6,0)
		st1 = wx.StaticText(self, -1, 'First Name')
		self.firstInput = wx.TextCtrl(self, -1)
		self.firstInput.Bind(wx.EVT_KEY_UP, self.checkValid)
		grid.Add(st1, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.firstInput, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		st2 = wx.StaticText(self, -1, 'Last Name')
		self.lastInput = wx.TextCtrl(self, -1)
		self.lastInput.Bind(wx.EVT_KEY_UP, self.checkValid)
		grid.Add(st2, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.lastInput, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		st3 = wx.StaticText(self, -1, 'Email')
		self.emailInput = wx.TextCtrl(self, -1)
		self.emailInput.Bind(wx.EVT_KEY_UP, self.checkValid)
		grid.Add(st3, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.emailInput, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		st4 = wx.StaticText(self, -1, 'Username')
		self.usernameInput = wx.TextCtrl(self, -1)
		self.usernameInput.Bind(wx.EVT_KEY_UP, self.checkValid)
		grid.Add(st4, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.usernameInput, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		st5 = wx.StaticText(self, -1, 'Password')
		self.passwordInput = wx.TextCtrl(self, -1, style = wx.TE_PASSWORD)
		self.passwordInput.Bind(wx.EVT_KEY_UP, self.checkValid)
		grid.Add(st5, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.passwordInput, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		st6 = wx.StaticText(self, -1, 'Confirm')
		self.confirmInput = wx.TextCtrl(self, -1, style = wx.TE_PASSWORD)
		self.confirmInput.Bind(wx.EVT_KEY_UP, self.checkValid)
		grid.Add(st6, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.confirmInput, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		st7 = wx.StaticText(self, -1, 'Department')
		self.departmentCombo = wx.ComboBox(self, -1)
		self.firstInput.Bind(wx.EVT_COMBOBOX, self.checkValid)
		grid.Add(st7, 0, wx.ALIGN_CENTER_VERTICAL)
		grid.Add(self.departmentCombo, 0, wx.ALIGN_RIGHT | wx.EXPAND)
		
		self.addBtn = wx.Button(self, -1, "Add User", size=(100,-1))
		self.addBtn.Disable()
		self.addBtn.Bind(wx.EVT_BUTTON, self.onAdd)
		self.cancelBtn = wx.Button(self, -1, "Cancel")
		self.cancelBtn.Bind(wx.EVT_BUTTON, self.onCancel)
		
		vbox.Add(grid, 0, wx.ALL | wx.EXPAND, 10)
		
		hboxBottom.Add(self.addBtn, 0, wx.RIGHT,10)
		hboxBottom.Add(self.cancelBtn, 0, wx.RIGHT,10)
		vbox.Add(hboxBottom, 0, wx.BOTTOM|wx.ALIGN_RIGHT,10)

		self.SetAutoLayout(True)
		self.SetSizer(vbox)
		self.Layout()
	
	def updateUser(self, user):
		self.user = user
		self.usernameInput.SetValue(self.user.username)
		self.firstInput.SetValue(self.user.fname)
		self.lastInput.SetValue(self.user.lname)
		self.emailInput.SetValue(self.user.email)
		self.passwordInput.SetValue(self.user.password)
		self.confirmInput.SetValue(self.user.password)
		self.departmentCombo.SetValue(self.user.department)
		self.checkValid()

	def updateDepartmentCombo(self,choices, default):
		self.departmentCombo.Clear()
		self.departmentCombo.AppendItems(choices)
		self.departmentCombo.SetValue(default)
	
	def updateMode(self, mode):
		self.mode = mode
		if self.mode == self.MODE_ADD:
			self.addBtn.SetLabel("Add User")
		else:
			self.addBtn.SetLabel("Update User")
		
	def onAdd(self, evt):		
		if self.mode == self.MODE_ADD:
			self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_ADD, self.GetId()))
		else:
			self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_UPDATE, self.GetId()))
		self.checkValid()
	
	def onCancel(self, evt):
		self.GetEventHandler().ProcessEvent(wx.PyCommandEvent(self.evt_CANCEL, self.GetId()))
		
	def checkValid(self, evt=None):
		if self.enableSubmit(self.usernameInput.GetValue(),self.passwordInput.GetValue(),self.confirmInput.GetValue(),self.departmentCombo.GetValue()):
			self.addBtn.Enable()
		else:
			self.addBtn.Disable()
	
	def enableSubmit(self, u, p, c, d):
		return (len(u) > 0 and len(p) >0 and p == c and not d == enum.DEPT_NONE_SELECTED)