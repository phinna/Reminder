#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
import time
import datetime

import pptWorkers as PPW

import gspread
from oauth2client.client import SignedJwtAssertionCredentials


basedir = os.path.abspath(os.path.dirname(__file__))

GCREDENTIALS = 'gspread_cred.json'
CREDENTIALS_PATH = os.path.join(basedir, GCREDENTIALS)
DATABASE = 'ppt.db'
TABLE = 'contact'

def get_credentialg():
    '''
    '''
    jsonKey = json.load(open(CREDENTIALS_PATH))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials(jsonKey['client_email'],
                                                jsonKey['private_key'], scope)
    gc = gspread.authorize(credentials)

    return gc

def access_spreadsheet(url):
    gc = get_credentialg()
    sh = gc.open_by_url(url)
    wksList = sh.worksheets()
    return wksList



def open_ith_wks(wksList, i):
    return wksList[i]

class GetFellowWorkersInfo(object):

    @classmethod
    def read_data_from_PPTSpreadsheet(cls,index):
        url = ("https://docs.google.com/spreadsheets/d/"
            "1AYTcSf6Ew6RMd5oHYD8Mc5LWjhdZ_zpiP3daKo7aBuY/edit#gid=0")
        wksList = access_spreadsheet(url)
        wks = open_ith_wks(wksList, index)
        return wks

    @staticmethod
    def get_next_sunday():
        today = datetime.date.today()
        nextSunday = today + datetime.timedelta(6 - today.weekday())
        reformatSun = nextSunday.strftime("%-m/%-d/%Y")
        return reformatSun

    @staticmethod
    def get_names_for_sunday():
        worksheet = GetFellowWorkersInfo.read_data_from_PPTSpreadsheet(0)
        nextSunDate = GetFellowWorkersInfo.get_next_sunday()
        cell = worksheet.find(nextSunDate)
        rowNum = cell.row
        colNum = cell.col
        rightLaptop = worksheet.cell(rowNum + 1, colNum).value
        leftLaptop = worksheet.cell(rowNum + 2, colNum).value
        propresenter = worksheet.cell(rowNum + 3, colNum).value
        return [rightLaptop, leftLaptop, propresenter]

    @classmethod
    def read_from_contact(cls):
        worksheet = GetFellowWorkersInfo.read_data_from_PPTSpreadsheet(2)
        fellowWorkers = []
        for i in range(2, len(worksheet.col_values(1))+1):
            row = worksheet.row_values(i)
            fellowWorkers.append((row[0].rstrip().capitalize(),
                                    row[1].capitalize(), row[2]))
        return fellowWorkers









