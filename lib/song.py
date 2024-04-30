class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls): #note: the class method takes cls as the arguement.
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre) #note that it is Song.genres(accessing the class itself using dot notation, so we mention the class.) and not self.genres that is being appended.

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    @classmethod
    def add_to_genre_count(cls):
        for song in cls.genres:
            if song in cls.genre_count:
                cls.genre_count[song] += 1
            else:
                cls.genre_count[song] = 1

    @classmethod
    def add_to_artist_count(cls):
        for song in cls.artists:
            if song in cls.artist_count:
                cls.artist_count[song] += 1
            else:
                cls.artist_count[song] = 1

## class RESOURCES:
# - https://docs.python.org/3/
# - https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
# - https://realpython.com/instance-class-and-static-methods-demystified/
# - https://realpython.com/factory-method-python/
