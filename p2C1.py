class Thread:
    """"Fil de discussion"""

    def __init__(self, title, time_posted, post):
        """"Initialisation avec un titre, une date et le post

        Attention, on commence par un seul post, celui du sujet.
        Les réponses (autres posts) ne s'ajouterons qu'ultérieurement.
        """

        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """"Affiche le thread"""
        print("_____ THREAD _____")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display
            print()
        print("_____ END OF THREAD _____")

    def add_post(self, post):
        """"Ajoute un post"""
        self.posts.append(post)

class Post:

    def __init__(self, text, user, time_posted):
        self.text = text
        self.user = user
        self.time_posted = time_posted

    def display(self):
        print(f"Message posté par {self.user} le {self.time_posted}:")
        print(self.text)

class FilePost(Post):

    def __init__(self, text, user, time_posted, file):
        self.text = text
        self.user = user
        self.time_posted = time_posted
        self.file = file

    def display(self):
        super().display()
        print("Pièce jointe:")
        self.file.diplay()

class File:
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        print(f"Fichier: {self.name}")

class ImageFile(File):
    """Fichier image.

    Pas de spécification pour le moment
    """

    pass

class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, content, "aujourd'hui", file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", text=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self,content, "aujourd'hui")
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username

class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.text = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]