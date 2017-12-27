from model.customer import Customer
import re


class CustomerHelper:

    def __init__(self, app):
        self.app = app

    def open_customer_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create(self, customer):
        wd = self.app.wd
        # click add new contact
        wd.find_element_by_link_text("add new").click()
        # new contact form
        self.fill_contact_form(customer)
        # safe contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.customer_cache = None

    def fill_contact_form(self, customer):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(customer.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(customer.lastname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(customer.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(customer.email)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(customer.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(customer.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(customer.workphone)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(customer.secondaryphone)


    def select_customer_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def delete_firstCustomer(self):
        self.delete_customer_by_index(0)

    def delete_customer_by_index(self, index):
        wd = self.app.wd
        self.select_customer_by_index(index)
        #check delete button
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.customer_cache = None

    def modify_firstCustomer(self):
        self.modify_customer_by_index(0)

    def modify_customer_by_index(self, index, newContactData):
        wd = self.app.wd
        #edit some contact
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()
        self.fill_contact_form(newContactData)
        #update changes
        wd.find_element_by_name("update").click()
        self.customer_cache = None

    def count(self):
        wd = self.app.wd
        self.open_customer_page()
        return len(wd.find_elements_by_name("selected[]"))


    customer_cache = None

    def get_customer_list(self):
        if self.customer_cache is None:
            wd = self.app.wd
            self.open_customer_page()
            self.customer_cache = []
            for element in wd.find_elements_by_css_selector("tr[name = 'entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = wd.find_elements_by_tag_name("td")
                lastname = element.find_elements_by_css_selector("td")[1].text
                firstname = element.find_elements_by_css_selector("td")[2].text
                address = element.find_elements_by_css_selector("td")[3].text
                email = element.find_elements_by_css_selector("td")[4].text
                all_phones = cells[5].text
                self.customer_cache.append(Customer(firstname=firstname, lastname=lastname, address=address,
                                                    email=email, all_phones_from_home_page=all_phones, id=id))
        return list(self.customer_cache)


    def open_customer_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_customer_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()


    def get_customer_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_customer_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Customer(firstname=firstname, lastname=lastname, address = address, email=email,
                        homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                        secondaryphone=secondaryphone, id=id)


    def open_customer_view_by_index(self, index):
        wd = self.app.wd
        self.open_customer_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()


    def get_customer_from_view_page(self, index):
        wd = self.app.wd
        self.open_customer_view_by_index(index)
        text = wd.find_element_by_id("content").text
        text1 = wd.page_source
        email = re.search('mailto:(.*)"', text1).group(1)
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Customer(email=email, homephone=homephone, mobilephone=mobilephone,
                        workphone=workphone, secondaryphone=secondaryphone)








