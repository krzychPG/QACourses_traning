# -*- coding: utf-8 -*-
from fixture.application import Application
from model.customer import Customer
import time, unittest, pytest



@pytest.fixture()
def ap(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture
    
def test_addNewCustomer(ap):
    ap.login( username="admin", password="secret")
    ap.createCustomer(Customer(firstname="name", lastname="lastname", address="test 12", email="test@xyz.com", phone="123456789"))
    ap.logout()
