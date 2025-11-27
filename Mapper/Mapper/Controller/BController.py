from Model.BModel import BookEntity
from Model.BModel import BookMapper

class BookController:
    def __init__(self):
        self.books = [
            BookEntity(1, "1984", "George Orwell", 12.5, "ic-001"),
            BookEntity(2, "Brave New World", "Aldous Huxley", 10.0, "ic-002"),
        ]

    def get_all_books(self):
        return BookMapper.to_dto_list(self.books)
               
