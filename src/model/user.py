import peewee

from model.basemodel import BaseModel



class User(BaseModel):
    id = peewee.AutoField()
    username = peewee.TextField()
    password = peewee.TextField()
