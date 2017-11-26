from model.customer import Customer


class CustomerHelper:

    def __init__(self, ap):
        self.ap = ap

    def open_customer_page(self):
        wd = self.ap.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def create(self, customer):
        wd = self.ap.wd
        # click add new contact
        wd.find_element_by_link_text("add new").click()
        # new contact form
        self.fill_contact_form(customer)
        # safe contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, customer):
        wd = self.ap.wd
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
        wd.find_element_by_name("home").send_keys(customer.phone)

    def delete_firstCustomer(self):
        wd = self.ap.wd
        #select first customer
        wd.find_element_by_name("selected[]").click()
        #check delete button
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()


    def modify_firstCustomer(self, newContactData):
        wd = self.ap.wd
        #edit first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(newContactData)
        #update changes
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.ap.wd
        self.open_customer_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_customer_list(self):
        wd = self.ap.wd
        self.open_customer_page()
        customers = []
        for element in wd.find_elements_by_css_selector("tr[name = 'entry']"):
            id = element.find_element_by_name("selected[]").get_attribute("value")
            cells = wd.find_elements_by_tag_name("td")
            lastname = element.find_elements_by_css_selector("td")[1].text
            firstname = element.find_elements_by_css_selector("td")[2].text
            customers.append(Customer(id = id, firstname = firstname, lastname = lastname))
        return customers





