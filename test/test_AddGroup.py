# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("test", 20)]
    for footer in ["", random_string("test", 20)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_testAddGroup1(ap, group):
    old_groups = ap.group.get_group_list()
    ap.group.create(group)
    assert len(old_groups) + 1 == ap.group.count()
    new_groups = ap.group.get_group_list()
    old_groups.append(group)
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



