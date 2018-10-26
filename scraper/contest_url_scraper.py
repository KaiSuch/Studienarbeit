from bs4 import BeautifulSoup
import requests
import csv

#------------------------ Setup ------------------------ 

source = 'https://www.hackster.io/contests'

# csv writer setup
csv_file = open('180823_all_contests.csv', 'w', newline='') # create or open csv for saving the scraped data, newline='' to avoid an extra line after each datapoint
csv_writer = csv.writer(csv_file) # define the csv writer


# scrape and parse the page
page = requests.get(source).text
soup= BeautifulSoup(page, 'lxml')

for new_contest in soup.find_all('div', class_='challenge-thumb-full'):
    new_contest_name = new_contest.div.div.div.h4.a.text
    new_contest_page = 'https://www.hackster.io' + new_contest.div.div.div.h4.a.get('href')
    csv_writer.writerow([new_contest_page,new_contest_name])
    print('--------------------------------------')
    print(new_contest_name)
    print(new_contest_page)
    print('--------------------------------------')
    
print('###########################################################################')

for contest in soup.find_all('div', class_='challenge-thumb-info'):
    contest_name = contest.a.text
    contest_page = 'https://www.hackster.io' + contest.a.get('href')
    
    print('--------------------------------------')
    print(contest_name)
    print(contest_page)
    print('--------------------------------------')

    # save data to file
    csv_writer.writerow([contest_page, contest_name])

# close csv file
csv_file.close()