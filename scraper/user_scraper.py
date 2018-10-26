from bs4 import BeautifulSoup
import requests
import re

class author():
    
    # downloads and parses the page with bs4
    @staticmethod
    def soup_function(user_page):
        raw_user_page = requests.get(user_page).text
        a = BeautifulSoup(raw_user_page, 'lxml')
        return a
    
    # constructor
    def __init__(self, user_name, user_page, user_follower, user_following, user_tools_number, user_number_of_projects):
        self.user_name = user_name
        self.user_page = user_page
        self.user_follower = user_follower
        self.user_following = user_following
        self.user_tools_number = user_tools_number
        self.user_number_of_projects = user_number_of_projects
    
    # scrapes the user name
    def user_name_function(self):
        try:
            a = self.soup_function(self.user_page)        
            name = a.find('div', class_='user_card__userInfo__2HKBF').h1.text.encode("utf-8")
            self.user_name = name
            return name
        except:
            print("user_name_function error")
    
    # scrapes the number of projects of the user
    def user_number_of_projects_function(self):
        try:
            a = self.soup_function(self.user_page)
            project_number = a.find('div', class_='user_card__stats__3JTZY').a.text
            project_number = re.findall('\d+', project_number)[0]
            return project_number
        except:
            print("user_number_of_projects_function error")
        
    # scrapes the number of the follower
    def user_number_of_follower_function(self):
        try:
            a = self.soup_function(self.user_page)
            number_of_follower = a.find('div', class_='user_card__stats__3JTZY').a.find_next_sibling().text
            number_of_follower = re.findall('\d+', number_of_follower)[0]
            return number_of_follower
        except:
            print("user_number_of_follower_function error")
    
    # scrapes the number of people following the author
    def user_number_of_following_function(self):
        try:
            a = self.soup_function(self.user_page)
            number_of_following = a.find('div', class_='user_card__stats__3JTZY').a.find_next_sibling().find_next_sibling().text
            number_of_following = re.findall('\d+', number_of_following)[0]
            return number_of_following
        except:
            print("user_number_of_following_function error")
    
    # scrapes the number of projects of the user
    def user_tools_number_function(self):
        try:
            a = self.soup_function(self.user_page)
            tools_number = a.find('div', class_='profile__toolsAndCommunities__1sKc7')# .section.header.span.find_next_sibling().text
           # tools_number = re.findall('\d+', tools_number)[0]
            return tools_number
        except:
            print("user_tools_number_function error")

        
        