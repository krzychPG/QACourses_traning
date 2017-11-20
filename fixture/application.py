from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.customer import CustomerHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.customer = CustomerHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    # def openHomePage(self):
    #     wd = self.wd
    #     wd.get("http://macbook-pro-123.local/addressbook/index.php")


    # def openGroupPage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()


    # def backToGroupPage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("group page").click()



    def destr(self):
        self.wd.quit()