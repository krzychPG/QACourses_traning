from model.group import Group
from random import randrange



def test_modify_group_name(ap):
    if ap.group.count() == 0:
        ap.group.create(Group(name = "New group1"))
    old_groups = ap.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    ap.group.modify_group_by_index(index, group)
    assert len(old_groups) == ap.group.count()
    new_groups = ap.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_modify_group_header(ap):
#     if ap.group.create == 0:
#         ap.group.create(Group(header = "New header1"))
#     old_groups = ap.group.get_group_list()
#     ap.group.modify_firstGroup(Group(name="New header"))
#     new_groups = ap.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

