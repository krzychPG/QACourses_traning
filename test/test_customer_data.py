import re

def test_customer_data_on_home_page(app):
    customer_from_home_page = app.customer.get_customer_list()[0]
    customer_from_edit_page = app.customer.get_customer_info_from_edit_page(0)
    assert customer_from_home_page.firstname == clear(customer_from_edit_page.firstname)
    assert customer_from_home_page.lastname == clear(customer_from_edit_page.lastname)
    assert customer_from_home_page.address == customer_from_edit_page.address
    assert customer_from_home_page.email == customer_from_edit_page.email
    assert customer_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(customer_from_edit_page)



def test_customer_data_on_customer_view_page(app):
    customer_from_view_page = app.customer.get_customer_from_view_page(0)
    customer_from_edit_page = app.customer.get_customer_info_from_edit_page(0)
    assert customer_from_view_page.email == customer_from_edit_page.email
    assert customer_from_view_page.homephone == customer_from_edit_page.homephone
    assert customer_from_view_page.mobilephone == customer_from_edit_page.mobilephone
    assert customer_from_view_page.workphone == customer_from_edit_page.workphone
    assert customer_from_view_page.secondaryphone == customer_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(customer):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [customer.homephone, customer.mobilephone, customer.workphone, customer.secondaryphone]))))