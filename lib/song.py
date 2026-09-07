class Song:
    # Class attributes — shared across every Song instance
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}   # matches the test file's attribute name

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Each of these fires every time a new Song is created
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    def add_song_to_count(self):
        # Increment the total song count by 1
        Song.count += 1

    def add_to_genres(self):
        # Only add the genre if it isn't already in the list
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        # Only add the artist if it isn't already in the list
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        # If the genre already exists as a key, bump its count
        # Otherwise, add it with a starting count of 1
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artists_count(self):
        # Same pattern, but updates the artist_count dict
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1