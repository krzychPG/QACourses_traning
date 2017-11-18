# -*- coding: utf-8 -*-
from model.group import Group

def test_testAddGroup1(ap):
    ap.session.login( username="admin", password="secret")
    ap.group.create(Group(name="test1", header="test2", footer="test4"))
    ap.session.logout()
