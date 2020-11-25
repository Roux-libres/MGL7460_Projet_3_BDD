from BaseModel import BaseModel

class Query(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.id = None
        self.user_id = None
        self.date = None
        self.content = None

