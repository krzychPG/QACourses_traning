# -*- coding: utf-8 -*-

from model.customer import Customer


    
def test_addNewCustomer(ap):
    ap.session.login( username="admin", password="secret")
    ap.customer.create(Customer(firstname="name", lastname="lastname", address="test 12", email="test@xyz.com", phone="123456789"))
    ap.session.logout()
