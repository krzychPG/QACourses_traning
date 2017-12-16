from model.customer import Customer
from random import randrange


def test_modify_firstCustomer(app):
    if app.customer.count() == 0:
        app.customer.create(Customer(firstname="newFirstname", lastname="newLastname", address="newAddres",
                                    email="newEmail", homephone = "12345667", mobilephone="1243224",
                                    workphone="1231412", secondaryphone="423423423"))
    old_customers = app.customer.get_customer_list()
    customer = Customer(firstname="nameEDIT", lastname="lastnameEDIT", address="testEDIT 12", email="testEDIT@xyz.com",
                        homephone = "12345667", mobilephone="1243224",workphone="1231412", secondaryphone="423423423")
    index = randrange(len(old_customers))
    app.customer.modify_customer_by_index(index, customer)
    assert len(old_customers) == app.customer.count()
    new_customers = app.customer.get_customer_list()
    old_customers[index] = customer
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)