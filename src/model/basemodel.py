from peewee import SqliteDatabase



db = SqliteDatabase("nasa.db")

class BaseModel:
    class Meta:
        database = db
