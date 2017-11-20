from model.customer import Customer


def test_modify_firstCustomer(ap):
    if ap.customer.count() == 0:
        ap.customer.create(Customer(firstname =  "newFirstname", lastname = "newLastname", addres = "newAddres", email = "newEmail", phone = "newPhone"))
    ap.customer.modify_firstCustomer(Customer(firstname="nameEDIT", lastname="lastnameEDIT", address="testEDIT 12", email="testEDIT@xyz.com", phone="12345983"))
