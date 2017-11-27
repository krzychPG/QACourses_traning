from model.group import Group

class GroupHelper:

    def __init__(self, ap):
        self.ap =ap

    def openGroupPage(self):
        wd = self.ap.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
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
        self.group_cache = None

    def change_field_value(self, field_name, text):
        wd = self.ap.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.ap.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def delete_firstGroup(self):
        wd = self.ap.wd
        self.openGroupPage()
        #check first group
        wd.find_element_by_name("selected[]").click()
        #check delete button
        wd.find_element_by_name("delete").click()
        self.backToGroupPage()
        self.group_cache = None

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
        self.group_cache = None


    def backToGroupPage(self):
        wd = self.ap.wd
        wd.find_element_by_link_text("group page").click()


    def count(self):
        wd = self.ap.wd
        self.openGroupPage()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.ap.wd
            self.openGroupPage()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = wd.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)



