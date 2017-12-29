from pony.orm import *
from datetime import datetime
from model.group import Group
from model.customer import Customer
from pymysql.converters import decoders

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        is = PrimaryKey(int, column = 'group_id')
        name = Optional(str, strcolumn = 'group_name')
        header = Optional(str, strcolumn = 'group_header')
        footer = Optional(str, strcolumn = 'group_footer')

    class ORMCustomer(db.Entity):
        _table_ = 'addressbook'
        is = PrimaryKey(int, column = 'id')
        firstname = Optional(str, strcolumn = 'firstaname')
        lastname = Optional(str, strcolumn = 'lastname')
        deprecated = Optional(datetime, strcolumn = 'deprecated')



    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database = name, user = user, password = password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer = group.footer)
        return list(map(convert, groups))

    def conver_customer_to_model(self, customer):
        def convert(customer):
            return Group(id=str(customer.id), firstnaame=customer.firstname, lastname=customer.lastname)
        return list(map(convert, customer))



    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_customer_list(self):
        return self.convert_customer_to_model(select(c for c in ORMFixture.ORMCustomer if c.deprecated is None))

