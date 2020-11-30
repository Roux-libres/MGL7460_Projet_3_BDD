import os

import peewee
from playhouse.sqlite_ext import SqliteExtDatabase



DATABASE = SqliteExtDatabase(os.path.join(os.path.abspath(os.path.dirname(__file__)), r"..\..\src\database.db"))

class BaseModel(peewee.Model):
    class Meta:
        database = DATABASE