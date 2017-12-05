# -*- coding: utf-8 -*-

from data.groups import testdata
import pytest

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_testAddGroup1(ap, group):
    old_groups = ap.group.get_group_list()
    ap.group.create(group)
    assert len(old_groups) + 1 == ap.group.count()
    new_groups = ap.group.get_group_list()
    old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



