from model.customer import Customer


def test_modify_firstCustomer(ap):
    ap.session.login( username="admin", password="secret")
    ap.customer.modify_firstCustomer(Customer(firstname="nameEDIT", lastname="lastnameEDIT", address="testEDIT 12", email="testEDIT@xyz.com", phone="12345983"))
    ap.session.logout()