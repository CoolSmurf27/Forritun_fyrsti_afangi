#try classes

class album:
    def __init__(self, name ="unknown name", artist = "unknown artist", release_year = "unknown year"):
        self.name = name
        self.artist = artist
        self.release_year = release_year

    def set_album(self, band = None, title = None, year = None):
        if band is not None:
            self.band = band
        if title is not None:
            self.title = title
        if year is not None:
            self.year = year

    def __str__(self):
        return f"Album {self.title} by {self.band}, released in {self.year}."

