

class SessionHelper:


    def __init__(self, ap):
        self.ap = ap


    def login(self, username, password):
        wd = self.ap.wd
        wd.get("http://macbook-pro-123.local/addressbook/index.php")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()



    def logout(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("Logout").click()