import peewee

from model.basemodel import BaseModel
from model.graphasteroid import GraphAsteroid



class Point(BaseModel):
    id = peewee.AutoField()
    graph_asteroid_id = peewee.ForeignKeyField(GraphAsteroid)
    x = peewee.IntegerField()
    y = peewee.IntegerField()
    radius = peewee.FloatField()
