#!/usr/bin/python
# -*- coding: utf-8 -*-
import gspread
import accGoogleSpreadSheet as ACGSS
import pptWorkers as PPW

DATABASE = "ptt.db"
def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    table = "contact"
    contacts = ACGSS.GetFellowWorkersInfo.read_from_contact()
    PPW.DBManager.create_table(DATABASE, table)
    PPW.DBManager.insert_data_to_table(DATABASE, table, contacts)
    print ACGSS.GetFellowWorkersInfo.get_info_from_db()


if __name__ == '__main__':
    main()
