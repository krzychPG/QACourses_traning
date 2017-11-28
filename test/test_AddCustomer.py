# -*- coding: utf-8 -*-

from model.customer import Customer



def test_addNewCustomer(ap):

    old_customers = ap.customer.get_customer_list()
    customer = Customer(firstname="name", lastname="lastname", address="test 12", email="test@xyz.com",
                        homephone = "12345667", mobilephone="1243224", workphone="1231412", secondaryphone="423423423")
    ap.customer.create(customer)
    assert len(old_customers) + 1 == ap.customer.count()
    new_customers = ap.customer.get_customer_list()
    old_customers.append(customer)
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)


