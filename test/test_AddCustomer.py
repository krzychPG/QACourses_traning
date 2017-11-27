# -*- coding: utf-8 -*-

from model.customer import Customer



def test_addNewCustomer(ap):

    old_customers = ap.customer.get_customer_list()
    customer = Customer(firstname="name", lastname="lastname", address="test 12", email="test@xyz.com", phone="123456789")
    ap.customer.create(customer)
    new_customers = ap.customer.get_customer_list()
    assert len(old_customers) + 1 == len(new_customers)
    old_customers.append(customer)
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)


