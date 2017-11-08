# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture()
def ap(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture


def test_testAddGroup1(ap):
    ap.login( username="admin", password="secret")
    ap.createGroup( Group(name="test1", header="test2", footer="test4"))
    ap.logout()
