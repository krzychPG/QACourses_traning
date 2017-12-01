

class SessionHelper:


    def __init__(self, ap):
        self.ap = ap


    def login(self, username, password):
        wd = self.ap.wd
        wd.get("http://localhost/addressbook/index.php")
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

    def is_logged_in(self):
        wd = self.ap.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.ap.wd
        return self.get_logged_user() == username


    def get_logged_user(self):
        wd = self.ap.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text[1:-1]

    def ensure_logout(self):
        wd = self.ap.wd
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.ap.wd
        if len(wd.find_elements_by_link_text("Logout")) > 0:
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)



