from model.group import Group


def test_delete_firstGroup(ap):

    if ap.group.count() == 0:
        ap.group.create(Group(name="test"))
    ap.group.delete_firstGroup()
