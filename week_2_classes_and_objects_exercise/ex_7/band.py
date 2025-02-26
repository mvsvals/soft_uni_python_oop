from album import Album
from song import Song

class Band:
    def __init__(self, name: str, ):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        found_album = next((x for x in self.albums if x.name == album_name), None)
        if not found_album:
            return f"Album {album_name} is not found."
        if found_album.published:
            return "Album has been published. It cannot be removed."
        self.albums = [x for x in self.albums if x.name != album_name]
        return f"Album {album_name} has been removed."

    def details(self):
        return f"Band {self.name}\n" + "\n".join(x.details() for x in self.albums)

