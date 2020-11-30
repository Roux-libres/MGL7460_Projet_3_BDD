from peewee import SqliteDatabase



class BaseModel:
    def __init__(self, database):
        self.database = database
