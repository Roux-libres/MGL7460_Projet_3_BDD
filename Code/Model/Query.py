from BaseModel import BaseModel

class Query(BaseModel):
    def __init__(self, db):
        BaseModel.__init__(self, db)
        self.id = None
        self.user_id = None
        self.date = None
        self.content = None

