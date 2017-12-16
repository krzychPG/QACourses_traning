from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.customer import CustomerHelper

class Application:

    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.customer = CustomerHelper(self)
        self.baseUrl = baseUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def openHomePage(self):
         wd = self.wd
         if not (wd.current_url.endswith("/adressbook/") and len(wd.find_elements_by_name()) > 0):
             wd.get(self.baseUrl)


    # def openGroupPage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()


    # def backToGroupPage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("group page").click()



    def destroy(self):
        self.wd.quit()