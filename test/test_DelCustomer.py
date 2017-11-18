


def test_delete_firstCustomer(ap):
    ap.session.login( username="admin", password="secret")
    ap.customer.delete_firstCustomer()
    ap.session.logout()