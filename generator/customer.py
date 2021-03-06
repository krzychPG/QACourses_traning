
from model.customer import Customer
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of customers", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=3
f ="data/groups.json"


for o, a in opts:
    if o == "-n":
        n= int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Customer(firstname="", lastname="", address="")] + [
    Customer(firstname=random_string("Imie", 10), lastname=random_string("Nazwisko", 20), address=random_string("address", 10))
    for i in range(n)
]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    #out.write(json.dumps(testdata2, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))