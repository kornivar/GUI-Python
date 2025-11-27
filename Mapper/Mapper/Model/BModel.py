class BookEntity:
    def __init__(self, id, title, author, price, internal_code):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.internal_code = internal_code

class BookDTO:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author

class BookMapper:
    @staticmethod
    def to_dto(book_entity):
        return BookDTO(id=book_entity.id, title=book_entity.title, author=book_entity.author)

    @staticmethod
    def to_dto_list(book_entity_list):
        return [BookMapper.to_dto(book_entity) for book_entity in book_entity_list]