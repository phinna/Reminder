#!/usr/bin/python
# -*- coding: utf-8 -*-
import gspread
import accGoogleSpreadSheet as ACGSS

def main():
    """Shows basic usage of the Google Drive API.

    Creates a Google Drive API service object and outputs the names and IDs
    for up to 10 files.
    """
    # worksheet = ACGSS.read_data_from_PPTSpreadsheet()

    # print (worksheet.acell('E3').value)
    # print (worksheet.cell(3, 5).value)
    # print (worksheet.cell(3, 6).value)

    # nSun = ACGSS.get_next_sunday()


    # cell1 = worksheet.find(nSun)
    # print("Found something at R%sC%s" % (cell1.row, cell1.col))

    left, right, propre = ACGSS.get_names_sunday()
    print (left)
    print (right)
    print (propre)

if __name__ == '__main__':
    main()
