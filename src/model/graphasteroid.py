import peewee

from model.basemodel import BaseModel



class GraphAsteroid(BaseModel):
    id = peewee.AutoField()
    date = peewee.DateField()
