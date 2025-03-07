class PhotoAlbum:
    MAX_PHOTOS_PER_PAGE = 4
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages_needed = photos_count // cls.MAX_PHOTOS_PER_PAGE
        remainder = photos_count % cls.MAX_PHOTOS_PER_PAGE
        if remainder:
            pages_needed += 1
        return cls(pages_needed)

    def add_photo(self, label: str):
        first_available_page = [i for i in range(len(self.photos)) if len(self.photos[i]) < PhotoAlbum.MAX_PHOTOS_PER_PAGE]
        if len(first_available_page) == 0:
            return  "No more free slots"
        self.photos[first_available_page[0]].append(label)
        first_available_slot = self.photos[first_available_page[0]].index(label)
        return f"{label} photo added successfully on page {first_available_page[0] + 1} slot {first_available_slot + 1}"


    def display(self):
        output_string = ['-----------']
        for i in range(self.pages):
            output_string.append(' '.join(str('[]') for x in self.photos[i]))
            output_string.append('-----------')
        return '\n'.join(output_string)

