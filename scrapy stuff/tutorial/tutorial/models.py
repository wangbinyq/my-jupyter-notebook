from peewee import *

db = SqliteDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class Author(BaseModel):
    name = CharField(unique=True)

class Quote(BaseModel):
    text = CharField()
    author = ForeignKeyField(Author, backref='quotes')

class Tag(BaseModel):
    name = CharField(unique=True)

class QuoteTag(BaseModel):
    tag = ForeignKeyField(Tag, backref='tags')
    quote = ForeignKeyField(Quote, backref='quotes')

