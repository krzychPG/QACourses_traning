# -*- coding: utf-8 -*-

from model.group import Group


def test_testAddGroup1(ap):
    old_groups = ap.group.get_group_list()
    ap.group.create(Group(name="test1", header="test2", footer="test4"))
    new_groups = ap.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    new_groups[0:1] = []
    assert len(old_groups) == len(new_groups)


