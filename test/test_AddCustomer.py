# -*- coding: utf-8 -*-

from model.customer import Customer
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata2 = [
    Customer(firstname=firstname, lastname=lastname, address=address)
    for firstname in ["", random_string("Imie", 10)]
    for lastname in ["", random_string("Nazwisko", 20)]
    for address in ["", random_string("address", 10)]
]

@pytest.mark.parametrize("customer", testdata2, ids=[repr(x) for x in testdata2])
def test_addNewCustomer(ap, customer):

    old_customers = ap.customer.get_customer_list()
    ap.customer.create(customer)
    assert len(old_customers) + 1 == ap.customer.count()
    new_customers = ap.customer.get_customer_list()
    old_customers.append(customer)
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)


