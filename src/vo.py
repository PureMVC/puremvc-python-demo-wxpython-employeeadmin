"""
PureMVC Python Port by Toby de Havilland <toby.de.havilland@puremvc.org> 
PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved. 
Your reuse is governed by the Creative Commons Attribution 3.0 License
"""

import enum

class RoleVO(object):
	username = None
	roles = []
	
	def __init__(self, username=None,roles=None):
		if username: 
			self.username = username
		if roles:
			self.roles = roles

class UserVO(object):
	username = None
	fname = None
	lname = None
	email = None
	password = None
	department = enum.DEPT_NONE_SELECTED;
	
	def __init__(self,uname=None,fname=None,lname=None,email=None,password=None,department = None):
		if uname:
			self.username = uname
		if fname:
			self.fname = fname
		if lname:
			self.lname = lname
		if email:
			self.email = email
		if password:	
			self.password = password
		if department:
			self.department = department

	def isValid(self):
		return (len(username) > 0 and len(password) > 0 and department is not enum.DeptEnum.NONE_SELECTED)

	def givenName(self):
		return self.lname+', '+self.fname