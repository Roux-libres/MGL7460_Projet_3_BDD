from basemodel import BaseModel



class GraphAsteroid(BaseModel):
    def __init__(self, database):
        super().__init__(database)
        self.id = None
        self.date = None

    def display_asteroid(self):
        pass
