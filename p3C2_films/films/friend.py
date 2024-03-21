class Friend:
    def __init__(self, name, film=None):
        self.name = name
        self.film = film
        if film:
            film.location = self