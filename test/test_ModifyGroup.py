from model.group import Group


def test_modify_firstGroup(ap):
    ap.session.login( username="admin", password="secret")
    ap.group.modify_firstGroup(Group(name="test1EDIT", header="test2EDIT", footer="test4EDIT"))
    ap.session.logout()