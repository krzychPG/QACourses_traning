from model.customer import Customer


def test_delete_firstCustomer(ap):
    if ap.customer.count() == 0:
        ap.customer.create(Customer(firstname = "newFirstname", lastname = "newLastname", addres = "newAddres", email = "newEmail", phone = "newPhone"))
    ap.customer.delete_firstCustomer()
