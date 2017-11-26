from model.customer import Customer


def test_delete_firstCustomer(ap):

    if ap.customer.count() == 0:
        ap.customer.create(Customer(firstname = "newFirstname", lastname = "newLastname", address = "newAddres", email = "newEmail", phone = "newPhone"))
    old_customers = ap.customer.get_customer_list()
    ap.customer.delete_firstCustomer()
    new_customers = ap.customer.get_customer_list()
    assert len(old_customers) - 1 == len(new_customers)
    old_customers[0:1] = []
    assert old_customers == new_customers
