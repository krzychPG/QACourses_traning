from model.customer import Customer
from random import randrange

def test_delete_some_customer(ap):

    if ap.customer.count() == 0:
        ap.customer.create(Customer(firstname = "newFirstname", lastname = "newLastname", address = "newAddres",
                                    email = "newEmail", homephone = "12345667", mobilephone="1243224",
                                    workphone="1231412", secondaryphone="423423423"))
    old_customers = ap.customer.get_customer_list()
    index = randrange(len(old_customers))
    ap.customer.delete_customer_by_index(index)
    assert len(old_customers) - 1 == ap.customer.count()
    new_customers = ap.customer.get_customer_list()
    old_customers[index:index+1] = []
    assert old_customers == new_customers
