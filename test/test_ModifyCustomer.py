from model.customer import Customer


def test_modify_firstCustomer(ap):
    if ap.customer.count() == 0:
        ap.customer.create(Customer(firstname="newFirstname", lastname="newLastname", addres="newAddres", email="newEmail", phone="newPhone"))
    old_customers = ap.customer.get_customer_list()
    customer = Customer(firstname="nameEDIT", lastname="lastnameEDIT", address="testEDIT 12", email="testEDIT@xyz.com", phone="12345983")
    ap.customer.modify_firstCustomer(customer)
    new_customers = ap.customer.get_customer_list()
    assert len(old_customers)  == len(new_customers)
    old_customers[0] = customer
    assert sorted(old_customers, key=Customer.id_or_max) == sorted(new_customers, key=Customer.id_or_max)