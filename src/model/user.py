from basemodel import BaseModel



class User(BaseModel):
    def __init__(self, db):
        super().__init__(self, db)
        self.id = None
        self.username = None
        self.password = None
