# -*- coding: utf-8 -*-
from fixture.application import Application
from fixture.customer import CustomerHelper
from model.customer import Customer
import time, unittest, pytest



@pytest.fixture()
def ap(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture
    
def test_addNewCustomer(ap):
    ap.session.login( username="admin", password="secret")
    ap.customer.create(Customer(firstname="name", lastname="lastname", address="test 12", email="test@xyz.com", phone="123456789"))
    ap.session.logout()
