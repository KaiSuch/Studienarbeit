import xlrd
import contest_scraper as contest
import re
import json
from user_scraper import author



#------------------------ Setup ----------------------------

n = 64 #number of contests you want to crawl -> change order etc. in xlsx sheet

NamedesDokumentes = "contest_list_update.xlsx"
NamedesTabellenblattes = "Tabelle2"


#------------------------- functions -------------------------

workbook = xlrd.open_workbook((NamedesDokumentes))
worksheet = workbook.sheet_by_name(NamedesTabellenblattes)



def read_contest(Y2):
    for x in range(2, Y2):
        contest_page = worksheet.cell(x, 1).value
        name = contest.project_classification(contest_page)
        
        print("------------------------")
        print(name)
        print("------------------------")
        x += 1
        

read_contest(n)

