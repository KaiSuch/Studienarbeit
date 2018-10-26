import xlrd
import contest_scraper as contest


#------------------------ Setup ----------------------------

#number of contests you want to crawl -> change order etc. in xlsx sheet
n = 64

# names of the csv file
NamedesDokumentes = "contest_list_update.xlsx"
NamedesTabellenblattes = "Tabelle2"


#------------------------- Functions -------------------------

# opens the workbook
workbook = xlrd.open_workbook((NamedesDokumentes))
worksheet = workbook.sheet_by_name(NamedesTabellenblattes)


# main function which reads the contests from csv and passes them to the contest_scraper
def read_contest(Y2):
    for x in range(2, Y2):
        contest_page = worksheet.cell(x, 1).value
        name = contest.project_classification(contest_page)
        
        print("------------------------")
        print(name)
        print("------------------------")
        x += 1
        

# run the function
read_contest(n)

