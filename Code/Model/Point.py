from BaseModel import BaseModel

class Point(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.id = None
        self.graph_asteroid_id = None
        self.x = None
        self.y = None
        self.radius = None

