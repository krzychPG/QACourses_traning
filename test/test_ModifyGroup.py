from model.group import Group



def test_modify_group_name(ap):
    if ap.group.count() == 0:
        ap.group.create(Group(name = "New group1"))
    ap.group.modify_firstGroup(Group(name="New group"))



def test_modify_group_header(ap):
    if ap.group.create == 0:
        ap.group.create(Group(header = "New header1"))
    ap.group.modify_firstGroup(Group(name="New header"))

