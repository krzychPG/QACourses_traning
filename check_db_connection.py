import pymysql.cursors
from fixture.orm import ORMFixture

db = DbFixture(host="localhost", name = "addressbook", user = "root", password = "")

try:
    l = db.get_customer_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    db.destroy()
