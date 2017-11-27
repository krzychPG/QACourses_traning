from model.group import Group


def test_delete_firstGroup(ap):
    if ap.group.count() == 0:
        ap.group.create(Group(name="test"))
    old_groups = ap.group.get_group_list()
    ap.group.delete_firstGroup()
    assert len(old_groups) - 1 == ap.group.count()
    new_groups = ap.group.get_group_list()
    old_groups[0:1] = []
    assert old_groups ==  new_groups
