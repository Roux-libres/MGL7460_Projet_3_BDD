import peewee

from model.basemodel import BaseModel
from model.user import User



class Query(BaseModel):
    id = peewee.AutoField()
    user_id = peewee.ForeignKeyField(User)
    date = peewee.DateTimeField()
    content = peewee.TextField()
