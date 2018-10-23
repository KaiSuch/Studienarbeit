import re
import json
from user_scraper import author 



#------------------- class --------------------------

class project(author):
    
    # constructor
    def __init__(self, user_name, user_page, user_follower, user_following, user_tools_number, user_number_of_projects, project_name, project_page, publish_date, views, comments, likes, difficulty, instruction, words, images, winorloose):
        super().__init__(user_name, user_page, user_follower, user_following, user_tools_number, user_number_of_projects)
        self.project_name = project_name
        self.project_page = project_page
        self.publish_date = publish_date
        self.views = views
        self.comments = comments
        self.likes = likes
        self.difficulty = difficulty
        self.instruction = instruction
        self.words = words 
        self.images = images
        self.winorloose = winorloose
        
    # Not working correctly    
    def project_name_function(self):
        try:
            a = self.soup_function(self.project_page)
            project_name = a.find('h1', class_="hckui__typography__h1".h1.text)
            return project_name
        except:
            print("project_name_function error")
        
        
    # Get the project publish date
    def project_publish_date_function(self):
        try:
            a = self.soup_function(self.project_page)
            publish_date = a.find('div', class_='hckui__typography__pebble').meta
            if publish_date.has_attr('content'):
                        publish_date = publish_date['content']
            return publish_date
        except:
            print("project_publish_date_function")
    
    # Get the project views
    def project_number_of_views_function(self):
        try:
            a = self.soup_function(self.project_page)
            views = a.find('span', class_='impressions-stats').text.replace(",", ".") # replace the comma with dot to avoid csv problems
            return views
        except:
            print("project_number_of_views error")
            
    # Get the project comments
    def project_number_of_comments_function(self):
        try:
            a = self.soup_function(self.project_page)
            comments1 = a.find('span', class_='nav-count').text # replace the () with nothing
            comments2 = comments1.replace("(","")
            comments = comments2.replace(")", "")  
            return comments
        except:
            print("project_number_of_comments_function error")
    
    # Get the number of project likes
    def project_number_of_likes_function(self):
        try:
            a = self.soup_function(self.project_page)
            likes = a.find('div', class_='hckui__layout__marginTop30').span.span
            likes = likes['data-hacksternova-props']
            likes = json.loads(likes)["respects"]
            return likes
        except:
            print("project_number_of_likes_function error")
     
    # Get the difficulty of the project
    def project_difficulty_function(self):
        a = self.soup_function(self.project_page)
        difficulty = a.find('div', class_='hckui__typography__bodyS project-details').span.a.span.text
        #difficulty = a.find('a', class_='hckui__typography__textWithIcon project-difficulty text-danger')
        if difficulty == "Easy":
            return difficulty
        if difficulty == "Intermediate":
            return difficulty
        if difficulty == "Advanced":
            return difficulty
        if difficulty == "Expert":
            return difficulty

    
    # Get the information about the provided instructions 1 for full instructions else 0
    def project_instruction_function(self):
        a = self.soup_function(self.project_page)
        instruction = a.find('div', class_='hckui__typography__bodyS project-details').span.find_next_sibling().text
        if instruction == "Full instructions provided":
            instruction = 1
            return instruction
        else:
            instruction = 0
            return instruction

            
    # Get the number of words used in the discription
    def project_number_of_words_function(self):
        a = self.soup_function(self.project_page)
        text = a.find(id='story').text
        number = len(re.findall(r'\w+', text))
        return number

    
    # Get the number of images in the discription
    def project_number_of_images_function(self):
        a = self.soup_function(self.project_page)
        story = a.find(id='story')
        number = len(story.find_all('img'))
        return number


    def user_name_scraper_function(self):
        try:
            a = self.soup_function(self.project_page)
            user_id = a.find('div', class_="hckui__typography__bold").a.get('href')
            user_page = "https://www.hackster.io" + user_id 
            return user_page
        except:
            print("user_name_scraper_function error (in project_scraper.py)")

    # Function for debugging
    def __repr__(self):
        return "Project('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(self.user_name, self.user_page, self.user_follower, self.user_following, self.user_tools_number, self.user_number_of_projects, self.project_name, self.project_page, self.publish_date, self.views, self.comments, self.likes, self.difficulty, self.instruction, self.words, self.images, self.winorloose)
    







