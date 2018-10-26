from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

# Logins to the website Hackser.io [Enter your Data in this function]
def site_login(url):
    driver = webdriver.Firefox()
    driver.get("https://www.hackster.io/users/sign_in")
    driver.find_element_by_id("email_address_email").send_keys("enter_your_mail_here")
    driver.find_element_by_id ("password_password").send_keys("enter_your_passwort_here")
    driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/div/div/div/div/div/div/div[4]/form/button").click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user-nav-face']/img"))
        )
        print("Found element")
    except:
        print("nothing found")
    driver.get(url)
    web_page = driver.page_source
    return web_page


def site_login_driver():
    driver = webdriver.Firefox()
    driver.get("https://www.hackster.io/users/sign_in")
    driver.find_element_by_id("email_address_email").send_keys("kaifranksuchanek@outlook.com")
    driver.find_element_by_id ("password_password").send_keys("TIM_TU2018")
    driver.find_element_by_xpath("//*[@id='content']/div/div/div[2]/div/div/div/div/div/div/div[4]/form/button").click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='user-nav-face']/img"))
        )
        print("Found element")
    except:
        print("nothing found")
    return driver


# Loads the page with silenium if an exception is thrown
def selenium_load_page(url, driver):
    driver.get(url)
    web_page = driver.page_source
    print("driver works")
    return web_page

# Parses the project difficulty
def project_difficulty_function2(web_page):
    try:
        a = soup_function2(web_page)
        difficulty = a.find('div', class_='hckui__typography__bodyS project-details').span.a.span.text
        if difficulty == "Easy":
            return difficulty
        if difficulty == "Intermediate":
            return difficulty
        if difficulty == "Advanced":
            return difficulty
        if difficulty == "Expert":
            return difficulty
    except:
        print("Selenium: project_diffictulty_function error")

# Counts the number of words
def project_number_of_words_function(web_page):
    try:
        a = soup_function2(web_page)
        text = a.find(id='story').text
        number = len(re.findall(r'\w+', text))
        return number
    except:
        print("Selenium: project_number_of_words_function error")
        number = 0
        return number

# Counts the number of images
def project_number_of_images_function(web_page):
    try:
        a = soup_function2(web_page)
        story = a.find(id='story')
        number = len(story.find_all('img'))
        return number
    except:
        print("project_number_of_images_function error")
        number = 0
        return number

# Checks if full instructions are provided
def project_instruction_function(web_page):
    try:
        a = soup_function2(web_page)
        instruction = a.find('div', class_='hckui__typography__bodyS project-details').span.find_next_sibling().text
        if instruction == "Full instructions provided":
            instruction = 1
            return instruction
        else:
            instruction = 0
            return instruction
    except:
        print("Selenium: project_instruction_function instruction = 0")
        instruction = 0
        return instruction

# Parses the page with bs4
def soup_function2(web_page):
    a = BeautifulSoup(web_page, 'lxml')
    return a
