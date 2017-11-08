from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    # def openHomePage(self):
    #     wd = self.wd
    #     wd.get("http://macbook-pro-123.local/addressbook/index.php")


    def login(self, username, password):
        wd = self.wd
        wd.get("http://macbook-pro-123.local/addressbook/index.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    # def openGroupPage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("groups").click()

    def createGroup(self, group):
        wd = self.wd
        #open group page
        wd.find_element_by_link_text("groups").click()
        # add new group
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit created group
        wd.find_element_by_name("submit").click()
        #back to group page
        wd.find_element_by_link_text("group page").click()

    # def backToGroupPage(self):
    #     wd = self.wd
    #     wd.find_element_by_link_text("group page").click()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def destr(self):
        self.wd.quit()