from model.customer import Customer
import random

def test_delete_some_customer(app, db, check_ui):
    if len(db.get_customer_list) == 0:
        app.customer.create(Customer(firstname = "newFirstname", lastname = "newLastname", address = "newAddres",
                                    email = "newEmail", homephone = "12345667", mobilephone="1243224",
                                    workphone="1231412", secondaryphone="423423423"))
    old_customers = db.get_customer_list()
    customer = random.choice(old_customers)
    app.customer.delete_customer_by_id(customer.id)
    #assert len(old_customers) - 1 == app.customer.count()
    new_customers = db.get_customer_list()
    old_customers.remove(customer)
    assert old_customers == new_customers
    if check_ui:
        assert sorted(new_customers, key=Customer.id_or_max) == sorted(app.customer.get_customer_list(),
                                                                      key=Customer.id_or_max)