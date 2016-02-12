#!/usr/bin/env python

#############################################################
#
#   sendEmail.py
#   
#   Author: Phinna Huang; 

#   Copyright (c) 2016 Apple Inc. All rights reserved.
#           
# #############################################################
import os
import logging
import smtplib

import pptWorkers as PPW
import accGoogleSpreadSheet as AGSS

MAILSERVER = "smtp.gmail.com"
PORT = 587
DBFILENAME = "ppt.db"
BASEDIR = os.path.dirname(os.path.abspath(__file__))
TABLE = "contact"
SUBJECT = "[Reminder]Sunday Woreship PPT"

class SendEmail(object):

	def __init__(self, userEmailAddress, userEmailPassword,  contents):
		self.smtpObj = None
		self.userEmAdr = userEmailAddress
		self.userEmPd = userEmailPassword
		self.contents = contents

	def connect_SMTP_server(self):
		self.smtpObj = smtplib.SMTP(MAILSERVER, PORT)
		self.smtpObj.ehlo()
		self.smtpObj.starttls()

	def log_into_SMTP_server(self):
		self.smtpObj.login(self.userEmAdr, self.userEmPd)

	def write_and_send_email(self):
		subject = "Subject: {sub}\n\n".format(sub=SUBJECT)
		self.contents = subject + self.contents
		rpEmails = SendEmail.request_email()
		rpEmails = [(u'phinna37@gmail.com ',), (u'phinna37@gmail.com',)]
		for rpemail in rpEmails:
			sendMailStatus = self.smtpObj.sendmail(self.userEmAdr, 
					rpemail[0].encode('utf-8'), self.contents)
		self.smtpObj.quit()


	@staticmethod
	def request_email():
		path_to_db = os.path.join(BASEDIR, DBFILENAME)
		dbIsNew = not os.path.exists(path_to_db)
		if dbIsNew:
			PPW.DBManager.create_table(DBFILENAME, TABLE)
			contacts = AGSS.GetFellowWorkersInfo.read_from_contact()
			PPW.DBManager.insert_data_to_table(DBFILENAME, TABLE, contacts)
		else:
			logging.info("Database exists, assume schema does, too")
		names = AGSS.GetFellowWorkersInfo.get_names_for_sunday()
		emails = PPW.DBManager.get_email(DBFILENAME, TABLE, names)
		return emails

