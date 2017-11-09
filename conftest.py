import pytest
from fixture.application import Application



@pytest.fixture(scope = "session")
def ap(request):
    fixture = Application()
    request.addfinalizer(fixture.destr)
    return fixture