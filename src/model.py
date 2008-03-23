"""
PureMVC Python Port by Toby de Havilland <toby.de.havilland@puremvc.org> 
PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved. 
Your reuse is governed by the Creative Commons Attribution 3.0 License
"""

import puremvc.patterns.proxy
import enum, vo, main

class UserProxy(puremvc.patterns.proxy.Proxy):
	
	NAME = "UserProxy"
	def __init__(self):
		super(UserProxy, self).__init__(UserProxy.NAME, [])
		self.data = []
		self.addItem(vo.UserVO('lstooge','Larry', 'Stooge', "larry@stooges.com", 'ijk456',enum.DEPT_ACCT))
		self.addItem(vo.UserVO('cstooge','Curly', 'Stooge', "curly@stooges.com", 'xyz987',enum.DEPT_SALES))
		self.addItem(vo.UserVO('mstooge','Moe', 'Stooge', "moe@stooges.com", 'abc123',enum.DEPT_PLANT))

	def getUsers(self):
		return self.data
   
	def addItem(self, item):
		self.data.append(item)

	def updateItem(self, user):
		for i in range(0,len(self.data)):
			if self.data[i].username == user.username:
				self.data[i] = user

	def deleteItem(self, user):
		for i in range(0,len(self.data)):
			if self.data[i].username == user.username:
				del self.data[i]

class RoleProxy(puremvc.patterns.proxy.Proxy):

	NAME = "RoleProxy"
	def __init__(self):
		super(RoleProxy, self).__init__(RoleProxy.NAME, [])
		self.data = []
		self.addItem(vo.RoleVO('lstooge', [enum.ROLE_PAYROLL,enum.ROLE_EMP_BENEFITS]))
		self.addItem(vo.RoleVO('cstooge', [enum.ROLE_ACCT_PAY,enum.ROLE_ACCT_RCV,enum.ROLE_GEN_LEDGER]))
		self.addItem(vo.RoleVO('mstooge', [enum.ROLE_INVENTORY,enum.ROLE_PRODUCTION,enum.ROLE_SALES,enum.ROLE_SHIPPING]))

	def getRoles(self):
		print self.data
		return self.data

	def addItem(self, item):
		self.data.append(item)

	def deleteItem(self, item):
		for i in range(len(self.data)):
			if self.data[i].username == item.username:
				del self.data[i]
				break

	def doesUserHaveRole(self, user, role):
		hasRole = False;
		for i in range(len(self.data)):
			if self.data[i].username == user.username:
				userRoles = self.data[i].roles
				for j in range(len(userRoles)):
					if userRoles[j] == role:
						hasRole = True
						break
		return hasRole

	def addRoleToUser(self, user, role):
		result = False;
		if not self.doesUserHaveRole(user, role):
			for i in range(0,len(self.data)):
				if self.data[i].username == user.username:
					userRoles = self.data[i].roles
					userRoles.append(role)
					result = True;
					break
		self.sendNotification(main.AppFacade.ADD_ROLE_RESULT, result)

	def removeRoleFromUser(self, user, role):
		if self.doesUserHaveRole(user, role):
			for i in range(0,len(self.data)):
				if self.data[i].username == user.username:
					userRoles = self.data[i].roles
					for j in range(0,len(userRoles)):
						if userRoles[j] == role:
							del userRoles[i]
							break

	def getUserRoles(self, username):
		userRoles = []
		for i in range(0,len(self.data)):
			if self.data[i].username == username:
				userRoles = self.data[i].roles
				break
		return userRoles