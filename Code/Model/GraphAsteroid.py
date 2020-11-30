from BaseModel import BaseModel

class GraphAsteroid(BaseModel):
    def __init__(self, db):
        BaseModel.__init__(self, db)
        self.id = None
        self.date = None

    def display_asteroid(self):
        pass