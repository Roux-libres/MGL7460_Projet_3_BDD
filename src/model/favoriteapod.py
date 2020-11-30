from basemodel import BaseModel



class FavoriteAPOD(BaseModel):
    def __init__(self, database):
        super().__init__(database)
        self.id = None
        self.user_id = None
        self.name = None
        self.date = None
        self.url = None
