from BaseModel import BaseModel

class GraphAsteroid(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.id = None
        self.user_id = None
        self.name = None
        self.date = None
        self.url = None
