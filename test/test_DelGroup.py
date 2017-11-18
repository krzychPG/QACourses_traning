

def test_delete_firstGroup(ap):
    ap.session.login( username="admin", password="secret")
    ap.group.delete_firstGroup()
    ap.session.logout()