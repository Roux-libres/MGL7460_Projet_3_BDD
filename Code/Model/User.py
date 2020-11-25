
from BaseModel import BaseModel

class User(BaseModel):
    def __init__(self):
        BaseModel.__init__(self)
        self.id = None
        self.username = None
        self.password = None

