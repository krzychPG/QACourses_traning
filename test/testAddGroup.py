# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture()
def ap(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture


def test_testAddGroup1(ap):
    ap.session.login( username="admin", password="secret")
    ap.group.create(Group(name="test1", header="test2", footer="test4"))
    ap.session.logout()
