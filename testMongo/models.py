from mongoengine import *

# Create your models here.

class TestMongo(Document):
    test_key = IntField(required=True)
    test_value = IntField(required=False)
