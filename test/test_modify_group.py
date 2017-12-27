from model.group import Group
import random



def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "New group1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "test"
    app.group.modify_group_by_id(group.id, group)
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



# def test_modify_group_header(ap):
#     if ap.group.create == 0:
#         ap.group.create(Group(header = "New header1"))
#     old_groups = ap.group.get_group_list()
#     ap.group.modify_firstGroup(Group(name="New header"))
#     new_groups = ap.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

