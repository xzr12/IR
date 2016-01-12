from mongoengine import *

# Create your models here.
class ChineseModel(Document):
    word = StringField(required=True)
    document = StringField(required=True)
    tfIdf = FloatField(required=False)
    times = IntField(required=True)
    tf = FloatField(required=False)

class ChineseDocumentModel(Document):
    document = StringField(required=True)
    length = FloatField(required=False)
    href = StringField(required=True)
    title = StringField(required=True)
    # similarity = FloatField(required=False)


class ChineseWordModel(Document):
    word = StringField(required=True)
    length = IntField(required=True)
    idf = FloatField(required=False)
    pinyin = StringField(required=True)


class EnglishModel(Document):
    word = StringField(required=True)
    document = StringField(required=True)
    tfIdf = FloatField(required=False)
    times = IntField(required=True)
    tf = FloatField(required=False)


class EnglishDocumentModel(Document):
    document = StringField(required=True)
    length = FloatField(required=False)
    href = StringField(required=True)
    title = StringField(required=True)
    # similarity = FloatField(required=False)


class EnglishWordModel(Document):
    word = StringField(required=True)
    length = IntField(required=True)
    idf = FloatField(required=False)