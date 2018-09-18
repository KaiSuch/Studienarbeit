import xlrd
import contest_scraper_no_class as contest



#------------------------ Setup ----------------------------

n = 29 #number of contests you want to crawl -> change order etc. in xlsx sheet

NamedesDokumentes = "contest_list.xlsx"
NamedesTabellenblattes = "Tabelle2"


#------------------------- functions -------------------------

workbook = xlrd.open_workbook((NamedesDokumentes))
worksheet = workbook.sheet_by_name(NamedesTabellenblattes)



def read_contest(Y2):
    for x in range(1, Y2):
        contest_page = worksheet.cell(x, 1).value
        name = contest.project_classification(contest_page)
        
        print("------------------------")
        print(name)
        print("------------------------")
        x += 1
        

read_contest(n)

