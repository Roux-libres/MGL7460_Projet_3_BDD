from basemodel import BaseModel



class Point(BaseModel):
    def __init__(self, database):
        super().__init__(database)
        self.id = None
        self.graph_asteroid_id = None
        self.x = None
        self.y = None
        self.radius = None
