from model.group import Group



def test_modify_group_name(ap):

    ap.group.modify_firstGroup(Group(name="New group"))
    ap.session.logout()


def test_modify_group_header(ap):

    ap.group.modify_firstGroup(Group(name="New header"))

