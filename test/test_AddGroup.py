# -*- coding: utf-8 -*-

from model.group import Group


def test_testAddGroup1(ap):

    ap.group.create(Group(name="test1", header="test2", footer="test4"))

