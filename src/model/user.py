from basemodel import BaseModel



class User(BaseModel):
    def __init__(self, database):
        super().__init__(database)
        self.id = None
        self.username = None
        self.password = None
