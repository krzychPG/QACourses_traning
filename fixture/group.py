

class GroupHelper:

    def __init__(self, ap):
        self.ap =ap

    def openGroupPage(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.ap.wd
        self.openGroupPage()
        # add new group
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit created group
        wd.find_element_by_name("submit").click()
        self.backToGroupPage()

    def fill_group_form(self, group):
        wd = self.ap.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_firstGroup(self):
        wd = self.ap.wd
        self.openGroupPage()
        #check first group
        wd.find_element_by_name("selected[]").click()
        #check delete button
        wd.find_element_by_name("delete").click()
        self.backToGroupPage()

    def modify_firstGroup(self, new_form_data):
        wd = self.ap.wd
        self.openGroupPage()
        # check first group
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        # edit group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_form_data)
        #update changes
        wd.find_element_by_name("update").click()
        self.backToGroupPage()


    def backToGroupPage(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("group page").click()



