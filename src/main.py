"""
PureMVC Python Demo - wxPython Employee Admin 
By Toby de Havilland <toby.de.havilland@puremvc.org>
Copyright(c) 2007-08 Toby de Havilland, Some rights reserved.
"""
import wx
import puremvc.patterns.facade
import controller, components

class AppFacade(puremvc.patterns.facade.Facade):
	
	STARTUP	          = "startup"
	NEW_USER          = "newUser"
	DELETE_USER       = "deleteUser"
	CANCEL_SELECTED   = "cancelSelected"

	USER_SELECTED     = "userSelected"
	USER_ADDED        = "userAdded"
	USER_UPDATED      = "userUpdated"
	USER_DELETED      = "userDeleted"

	ADD_ROLE          = "addRole"
	ADD_ROLE_RESULT   = "addRoleResult"
	
	SHOW_DIALOG       =  "showDialog"
	
	
	def __init__(self):
		self.initializeFacade()
		
	@staticmethod
	def getInstance():
		return AppFacade()
		
	def initializeFacade(self):
		super(AppFacade, self).initializeFacade()
	
		self.initializeController()
   
	def initializeController(self):
		super(AppFacade, self).initializeController()
		
		super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)
		super(AppFacade, self).registerCommand(AppFacade.DELETE_USER, controller.DeleteUserCommand)
		super(AppFacade, self).registerCommand(AppFacade.ADD_ROLE_RESULT, controller.AddRoleResultCommand)

if __name__ == '__main__':
	
	app = AppFacade.getInstance()
	wxApp = components.WxApp()
	app.sendNotification(AppFacade.STARTUP, wxApp.appFrame)
	wxApp.MainLoop()