"""
PureMVC Python Port by Toby de Havilland <toby.de.havilland@puremvc.org> 
PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved. 
Your reuse is governed by the Creative Commons Attribution 3.0 License
"""

import puremvc.patterns.command
import puremvc.interfaces
import model, view, main

class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
	def execute(self,note):
		self.facade.registerProxy(model.UserProxy())
		self.facade.registerProxy(model.RoleProxy())
    
		mainPanel = note.getBody()
		self.facade.registerMediator(view.DialogMediator(mainPanel))
		self.facade.registerMediator(view.UserFormMediator(mainPanel.userForm))
		self.facade.registerMediator(view.UserListMediator(mainPanel.userList))
		self.facade.registerMediator(view.RolePanelMediator(mainPanel.rolePanel))

class AddRoleResultCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
	def execute(self,note):
		result = note.getBody()
		if not result:
			self.facade.sendNotification(main.AppFacade.SHOW_DIALOG, "Role already exists for this user.")

class DeleteUserCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
	def execute(self,note):
           user = note.getBody()
           userProxy = self.facade.retrieveProxy(model.UserProxy.NAME)
           roleProxy = self.facade.retrieveProxy(model.RoleProxy.NAME)
           userProxy.deleteItem(user)       
           roleProxy.deleteItem(user)
           self.facade.sendNotification(main.AppFacade.USER_DELETED)