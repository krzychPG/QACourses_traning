from model.group import Group
from random import randrange

def test_delete_some_group(ap):
    if ap.group.count() == 0:
        ap.group.create(Group(name="test"))
    old_groups = ap.group.get_group_list()
    index = randrange(len(old_groups))
    ap.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == ap.group.count()
    new_groups = ap.group.get_group_list()
    old_groups[index:index+1] = []
    assert old_groups ==  new_groups
