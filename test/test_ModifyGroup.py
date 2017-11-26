from model.group import Group



def test_modify_group_name(ap):
    if ap.group.count() == 0:
        ap.group.create(Group(name = "New group1"))
    old_groups = ap.group.get_group_list()
    ap.group.modify_firstGroup(Group(name="New group"))
    new_groups = ap.group.get_group_list()
    assert len(old_groups)  == len(new_groups)



def test_modify_group_header(ap):
    if ap.group.create == 0:
        ap.group.create(Group(header = "New header1"))
    old_groups = ap.group.get_group_list()
    ap.group.modify_firstGroup(Group(name="New header"))
    new_groups = ap.group.get_group_list()
    assert len(old_groups) == len(new_groups)

