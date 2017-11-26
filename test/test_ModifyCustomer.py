from model.customer import Customer


def test_modify_firstCustomer(ap):
    if ap.customer.count() == 0:
        ap.customer.create(Customer(firstname =  "newFirstname", lastname = "newLastname", addres = "newAddres", email = "newEmail", phone = "newPhone"))
    old_customers = ap.customer.get_customer_list()
    ap.customer.modify_firstCustomer(Customer(firstname="nameEDIT", lastname="lastnameEDIT", address="testEDIT 12", email="testEDIT@xyz.com", phone="12345983"))
    new_customers = ap.customer.get_customer_list()
    assert len(old_customers)  == len(new_customers)