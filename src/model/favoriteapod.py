import peewee

from model.basemodel import BaseModel
from model.user import User



class FavoriteAPOD(BaseModel):
    id = peewee.AutoField()
    user_id = peewee.ForeignKeyField(User)
    name = peewee.TextField()
    date = peewee.DateField()
    url = peewee.TextField()
