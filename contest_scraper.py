from project_scraper import project
import Selenium_login as sl

driver = sl.site_login_driver()

# find and save the projects
def find_projects(status, winorloose, contest_page):
    f = open("Validation_data.txt", "a+")
    project_list = []
    for i in status.find_all('div', class_='card-body'):
        try:
            pro_1 = project("", "", "", "", "", "", "", "","", "", "", "", "", "", "", "", "")
            project_id = i.a.get('href')
            pro_1.project_page = 'https://www.hackster.io' + project_id
            try:
                author_id = i.find('div', class_='authors').a.get('href')
                pro_1.user_page = 'https://www.hackster.io' + author_id
                pro_1.user_name = pro_1.user_name_function()
                pro_1.user_follower = pro_1.user_number_of_follower_function()
                pro_1.user_following = pro_1.user_number_of_following_function()
                #pro_1.user_tools_number = pro_1.user_tools_number_function()
                pro_1.user_number_of_projects = pro_1.user_number_of_projects_function()
            except:
                try:
                    pro_1.user_page = pro_1.user_name_scraper_function()
                    pro_1.user_name = pro_1.user_name_function()
                    pro_1.user_follower = pro_1.user_number_of_follower_function()
                    pro_1.user_following = pro_1.user_number_of_following_function()
                    #pro_1.user_tools_number = pro_1.user_tools_number_function()
                    pro_1.user_number_of_projects = pro_1.user_number_of_projects_function()
                    print("Team -> picking the first member")
                except:
                    pro_1.user_page = 'not available'
                    print("No user page available")
            pro_1.comments = pro_1.project_number_of_comments_function()
            try:
                pro_1.difficulty = pro_1.project_difficulty_function()
                pro_1.images = pro_1.project_number_of_images_function()
                pro_1.instruction = pro_1.project_instruction_function()
                pro_1.words = pro_1.project_number_of_words_function()
                if pro_1.words == "None":
                    raise Exception
            except:
                # Selenium section -------------------------------------------------------------
                print("Project scraping error, starting selenium")
                try:
                    web_page = sl.selenium_load_page(pro_1.project_page,driver)
                except:
                    print("Selenium: Login error")
                try:
                    pro_1.difficulty = sl.project_difficulty_function2(web_page)
                except:
                    pro_1.difficulty = "None"
                pro_1.images = sl.project_number_of_images_function(web_page)
                pro_1.instruction = sl.project_instruction_function(web_page)
                pro_1.words = sl.project_number_of_words_function(web_page)
            pro_1.views = pro_1.project_number_of_views_function()
            pro_1.likes = pro_1.project_number_of_likes_function()
            #pro_1.project_name = pro_1.user_name_function()
            pro_1.publish_date = pro_1.project_publish_date_function()
            pro_1.winorloose = winorloose

            print("###########################")
            print(pro_1.winorloose, contest_page, pro_1.project_page, pro_1.views, pro_1.difficulty, pro_1.likes, pro_1.comments, pro_1.words, pro_1.images, pro_1.instruction, pro_1.user_page, pro_1.user_follower, pro_1.user_following, pro_1.user_number_of_projects)
           # print(pro_1)
            print("###########################")
            project_list.append(pro_1)
            #print(pro_1.winorloose,",", pro_1.project_page, ",", pro_1.views, ",", pro_1.difficulty, ",", pro_1.likes, ",", pro_1.comments, ",", pro_1.words, ",", pro_1.images, ",", pro_1.instruction, ",", pro_1.user_page, ",", pro_1.user_follower, ",", pro_1.user_following, ",", pro_1.user_number_of_projects, file=f)
            print(pro_1.winorloose, contest_page, pro_1.project_page, pro_1.views, pro_1.difficulty, pro_1.likes, pro_1.comments, pro_1.words, pro_1.images, pro_1.instruction, pro_1.user_page, pro_1.user_follower, pro_1.user_following, pro_1.user_number_of_projects, file=f)             
            #csv_writer.writerow(["'{}, {}".format(pro_1.project_page, pro_1.likes)])
        except:
            print("Whole Scraper dindn´t worked")

        
# searches if the project won or not    
def project_classification(contest_page):
    i =1
    while i <= 12:
        try:
            source = contest_page + '/projects?page=' + str(i)  
            a = project.soup_function(source)
            if i == 1: # On the first page are winners and loosers, here we need to distinguish
                winner = a.find('div', class_='thumb-list')
                find_projects(winner, '1', contest_page)
                looser = a.find('div', class_='thumb-list').nextSibling.nextSibling
                find_projects(looser, '0', contest_page)
            else: # the following pages just contain 'loosers' :D
                looser = a.find('div', class_='thumb-list')
                find_projects(looser, '0', contest_page)
            print("IIIIIIIII", i, "IIIIIIIIIIIII")
            i = i +1
        except:
            return
    return

def project_scraper(contest_page):
    i = 1 
    while i < 12:
        try: 
            source = contest_page + '/projects?page=' + str(i)  
            a = project.soup_function(source)
            winnerorlooser = a.find('div', class_='thumb-list')
            find_projects(winnerorlooser, '1')
            print("IIIIIIIII", i, "IIIIIIIIIIIII")

            i = i +1
        except:
            print("No more projects on page: " + i)
            return

