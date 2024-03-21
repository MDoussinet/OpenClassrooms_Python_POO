class Film():
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.location = None

class FilmVHF(Film):

    type = "VHF"

    def __init__(self, name, date):
        super().__init__(name, date)

class FilmDVD(Film):

    type = "DVD"

    def __init__(self, name, date):
        super().__init__(name, date)
