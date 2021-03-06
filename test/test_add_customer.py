# -*- coding: utf-8 -*-
from model.customer import Customer

def test_addNewCustomer(app, db, json_customers, check_ui):
    customer = json_customers
    old_customers = db.get_customer_list()
    app.customer.create(customer)
    #assert len(old_customers) + 1 == app.customer.count()
    new_customers = db.get_customer_list()
    old_customers.append(customer)
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)
    if check_ui:
        assert sorted(new_customers, key=Customer.id_or_max) == sorted(app.customers.get_customer_list(),
                                                                       key=Customer.id_or_max)



