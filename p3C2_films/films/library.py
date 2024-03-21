import random

from .data import films

class Library():
    def __init__(self):
        self.films = []
        for film_data in films:
            film_data.location = self
            self.films.append(film_data)

    def sort_by_date_and_name(self):
        """Tri les films par date et par nom."""
        self.films.sort(key=lambda film: (film.date, film.name))

    def sort_by_type(self):
        """Tri les films par type."""
        self.films.sort(key=lambda film: film.type)

    def get_random_film(self):
        return random.choice(self.films)

    def get_film_rent(self):
        films_rent = []
        for film in self.films:
            if film.location is not self:
                films_rent.append(film)
        return films_rent

    def find_by_name(self, name):
        for film in self.films:
            if name == film.name:
                return film
        return None