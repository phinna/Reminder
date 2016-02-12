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

MAILSERVER = "smtp.mail.gmail.com"
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
		formatC = "Subject: {}\n\n".format(SUBJECT)
		rpEmails = SendEmail.request_email()
		for string in self.contents:
			formatC = formatC + string + '\n'
		self.smtpObj.sendmail(self.userEmAdr, rpEmail, formatC)
		self.smtpObj.quit()

	# @staticmethod
 #    def get_info_from_db():
        
 #        emails = PPW.DBManager.get_email(DATABASE, TABLE, names)
 #        return emails

	@staticmethod
	def request_email():
		path_to_db = os.path.join(BASEDIR, DBFILENAME)
		dbIsNew = not os.path.exists(path_to_db)
		if dbIsNew:
			PPW.DBManager.create_table(DBFILENAME, TABLE)
			contacts = ACGSS.GetFellowWorkersInfo.read_from_contact()
			PPW.DBManager.insert_data_to_table(DBFILENAME, TABLE, contacts)
		else:
			logging.info("Database exists, assume schema does, too")
		names = AGSS.GetFellowWorkersInfo.get_names_for_sunday()
		emails = PPW.DBManager.get_email(DBFILENAME, TABLE, names)
		print email
		return email

