# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class testAddGroup1(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def openHomePage(self, wd):
        wd.get("http://macbook-pro-123.local/addressbook/index.php")


    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def openGroupPage(self, wd):
        wd.find_element_by_link_text("groups").click()

    def createGroup(self, wd, name, header, footer):
        # add new group
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # submit created group
        wd.find_element_by_name("submit").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def backToGroupPage(self, wd):
        wd.find_element_by_link_text("group page").click()


    def test_testAddGroup1(self):
        success = True
        wd = self.wd
        self.openHomePage(wd)
        self.login(wd, username="admin", password="secret")
        self.openGroupPage(wd)
        self.createGroup(wd, name="test1", header="test2", footer="test4")
        self.backToGroupPage(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
