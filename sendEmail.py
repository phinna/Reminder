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

import email.MIMEMultipart as EMIME
import email.MIMEText as EMIMET

import pptWorkers as PPW
import accGoogleSpreadSheet as AGSS

MAILSERVER = "smtp.gmail.com"
PORT = 587
DBFILENAME = "ppt.db"
BASEDIR = os.path.dirname(os.path.abspath(__file__))
TABLE = "contact"
# SUBJECT = "[Reminder]Sunday Woreship PPT"

class CreateEnvelope(object):

	def __init__(self, fromEmail, toEmail, ccEmail, subject, body):
		self.__fromEmail = fromEmail
		self.__toEmail = toEmail
		self.__ccEmail = ccEmail
		self.__subject = subject
		self.__body = body

	@property
	def send_mul(self):
		msg = EMIME.MIMEMultipart()
		msg['From'] = self.__fromEmail
		msg['To'] = ','.join(self.__toEmail)
		msg['Cc'] = ','.join(self.__ccEmail)
		msg['Subject'] = self.__subject
		msg.attach(EMIMET.MIMEText(self.__body, 'plain'))
		return msg

class SendEmail(object):

	def __init__(self, fromEmail, loginPassword,  toEmail,
					ccEmail, subject, body):
		self.server = None
		self.loginEmail = fromEmail
		self.loginPassword = loginPassword
		self.toEmail = toEmail
		self.ccEmail = ccEmail
		self.subject = subject
		self.body = body

	def write_and_send_email(self):

		envl = CreateEnvelope(self.loginEmail, self.toEmail,
				self.ccEmail, self.subject, self.body)
		msg = envl.send_mul
		rpEmails = msg["To"].split(",") + msg["Cc"].split(",")

		self.server = smtplib.SMTP(MAILSERVER, PORT)
		self.server.ehlo()
		self.server.starttls()
		self.server.login(self.loginEmail, self.loginPassword)
		sendMailStatus = self.server.sendmail(self.loginEmail,
					rpEmails, msg.as_string())

		self.server.quit()


	@staticmethod
	def request_email_from_GD():

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
		emails = [e[0].encode('utf-8') for e in emails]
		return emails

