from BaseModel import BaseModel

class Point(BaseModel):
    def __init__(self, db):
        BaseModel.__init__(self, db)
        self.id = None
        self.graph_asteroid_id = None
        self.x = None
        self.y = None
        self.radius = None

