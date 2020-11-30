from basemodel import BaseModel



class Query(BaseModel):
    def __init__(self, database):
        super().__init__(database)
        self.id = None
        self.user_id = None
        self.date = None
        self.content = None
