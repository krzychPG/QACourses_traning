

class GroupHelper:

    def __init__(self, ap):
        self.ap =ap


    def create(self, group):
        wd = self.ap.wd
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

    def delete_firstGroup(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("groups").click()
        #check first group
        wd.find_element_by_name("selected[]").click()
        #check delete button
        wd.find_element_by_name("delete").click()
        # back to group page
        wd.find_element_by_link_text("group page").click()