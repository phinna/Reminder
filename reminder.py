#!/usr/bin/python
# -*- coding: utf-8 -*-
import gspread
import accGoogleSpreadSheet as ACGSS
import pptWorkers as PPW
import sendEmail as SE

DATABASE = "ptt.db"
def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    # table = "contact"
    # contacts = ACGSS.GetFellowWorkersInfo.read_from_contact()
    # PPW.DBManager.create_table(DATABASE, table)
    # PPW.DBManager.insert_data_to_table(DATABASE, table, contacts)
    # print ACGSS.GetFellowWorkersInfo.get_info_from_db()
    userEmailAddress = "flowerphinna37@gmail.com" 
    userEmailPassword = "t01105701#M98#"
    nameList = GetFellowWorkersInfo.get_names_for_sunday()
    contents = ("Hi everyone,\n Please see below for"
                " Sunday woreship PPT schedule:\n"
                "Right:{right}\nLeft:{left}\nPropresenter:{pro}\n".format(
                    right=nameList[0], left=nameList[1], pro=nameList[2]))
    smtpObj = SE.SendEmail(userEmailAddress, userEmailPassword, contents)
    smtpObj.connect_SMTP_server()
    



if __name__ == '__main__':
    main()
