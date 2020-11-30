from basemodel import BaseModel



class GraphAsteroid(BaseModel):
    def __init__(self, db):
        super().__init__(self, db)
        self.id = None
        self.date = None

    def display_asteroid(self):
        pass
