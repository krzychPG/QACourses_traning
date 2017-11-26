# -*- coding: utf-8 -*-

from model.customer import Customer



def test_addNewCustomer(ap):

    old_customers = ap.customer.get_customer_list()
    ap.customer.create(Customer(firstname="name", lastname="lastname", address="test 12", email="test@xyz.com", phone="123456789"))
    new_customers = ap.customer.get_customer_list()
    assert len(old_customers) + 1 == len(new_customers)


