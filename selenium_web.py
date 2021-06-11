from selenium import webdriver

class inflow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/HP/Downloads/chromedriver.exe")

    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()

class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/HP/Downloads/chromedriver.exe")

    def play(self,query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        vedio = self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        vedio.click()

