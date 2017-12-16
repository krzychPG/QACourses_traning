from model.customer import Customer
import json

testdata = [
    Customer(firstname="firstname1", lastname="lastname1", address="address1"),
    Customer(firstname="firstname2", lastname="lastname2", address="address2")
]

# with open("../data/contacts.json") as f:
#     try:
#         read_file= json.load(f)
#     except ValueError as ve:
#         print(ve)
#         read_file = []
#
# testdata = [
#     Customer(firstname = read_file[i]['firstname'], lastname = read_file[i]['lastname'], address = read_file[i]['address'])
#     for i in range(len(read_file))
# ]