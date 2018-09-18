from project_scraper import project

#----------------------- class ---------------------------------

class contest(project):
    
    # constructor
    def __init__(self, user_name, user_page, user_follower, user_following, user_tools_number, project_name, project_page, publish_date, views, comments, likes, difficulty, instruction, words, images, winorloose, contest_name):
        super().__init__(project_name, project_page, publish_date, views, comments, likes, difficulty, instruction, words, images, winorloose)
        self.contest_name = contest_name

    # returns the contest name
    def contest_name_function(self, contest_page):
        a = self.soup_function(contest_page)
        contest_name = a.find('div', class_='media').h1.text
        return contest_name
    
    
    # NOT finished!
    def find_projects(self, status, winorloose):
        try:
            for i in status.find_all('div', class_='card-body'):
                pro_1 = project("", "", "", "", "", "", "","", "", "", "", "", "", "", "", "")
                project_id = i.a.get('href')
                pro_1.project_page = 'https://www.hackster.io' + project_id
                try:
                    author_id = i.find('div', class_='authors').a.get('href')
                    pro_1.user_page = 'https://www.hackster.io' + author_id
                except:
                    pro_1.user_page = 'not available'
                print(pro_1)
        except:
            return 
    
    # searches if the project won or not    
    def project_classification(self, contest_page):
        i = 1
        while i <= 10:
            source = contest_page + '/projects?page=' + str(i)  
            a = self.soup_function(source)
            if i == 1: # On the first page are winners and loosers, here we need to distinguish
                winner = a.find('div', class_='thumb-list')
                self.find_projects(winner, '1')
                looser = a.find('div', class_='thumb-list').nextSibling.nextSibling
                self.find_projects(looser, '0')
            else: # the following pages just contain 'loosers' :D
                looser = a.find('div', class_='thumb-list')
                self.find_projects(looser, '0')
            i = i +1
        return
            
            
