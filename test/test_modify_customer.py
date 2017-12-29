from model.customer import Customer
import random


def test_modify_firstCustomer(app, db, check_ui):
    if len(db.get_customer_list()) == 0:
        app.customer.create(Customer(firstname="newFirstname", lastname="newLastname", address="newAddres",
                                    email="newEmail", homephone = "12345667", mobilephone="1243224",
                                    workphone="1231412", secondaryphone="423423423"))
    old_customers = db.get_customer_list()
    customer = random.choice(old_customers)
    customer.firstname = "test"
    app.customer.modify_customer_by_id(customer.id, customer)
    #assert len(old_customers) == app.customer.count()
    new_customers = db.get_customer_list()
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)
    if check_ui:
        assert sorted(new_customers, key=Customer.id_or_max) == sorted(app.customer.get_customer_list(),
                                                                      key=Customer.id_or_max)