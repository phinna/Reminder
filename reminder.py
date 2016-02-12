#!/usr/bin/python
# -*- coding: utf-8 -*-
import gspread
import loadData as LD
import accGoogleSpreadSheet as AGSS
import pptWorkers as PPW
import sendEmail as SE

DATABASE = "ptt.db"
def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    
    userEAddr = LD.load_yaml()["userEmailAddress"]
    userEPass = LD.load_yaml()["password"]

    nameList = AGSS.GetFellowWorkersInfo.get_names_for_sunday()
    contents = ("Hi everyone,\n\n Please see below for"
                " Sunday woreship PPT schedule:\n\n"
                "Right: {right}\nLeft: {left}\nPropresenter: {pro}\n".format(
                    right=nameList[0], left=nameList[1], pro=nameList[2]))

    smtpObj = SE.SendEmail(userEAddr, userEPass, contents)
    smtpObj.connect_SMTP_server()
    smtpObj.log_into_SMTP_server()
    smtpObj.write_and_send_email()
    



if __name__ == '__main__':
    main()
