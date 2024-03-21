class Film:
    """"Un film classique"""

    def __init__(self, name):
        self.name = name

    def watch(self, player):
        print("Bon visionnage !")

class FilmCassette(Film):
    """"Un film en cassette"""

    def __init__(self, name):
        super().__init__(name)
        self.magnetic_tape = True

    def rewind(self):
        """"Rembobine le film"""
        print("C'est long à rembobiner !")
        self.magnetic_tape = True

    def watch(self, player):
        """"Regarder le film"""
        if player.type != "cassette":
            print("Le lecteur ne peut pas lire les cassettes.")
        else:
            print("Le film commence.")
            super.watch(player)

class Player:

    def __init__(self, type):
        self.type = type

player = Player("DVD")

film = Film("2001: l'odyssée de l'espace")
film_cassette = FilmCassette("Blade Runner")

print(film.name)
film.watch(player)

print(film_cassette.name)
print(film_cassette.magnetic_tape)
film_cassette.watch(player)
film_cassette.rewind()