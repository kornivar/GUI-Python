class BookView:
    @staticmethod
    def render_books(entity_list):
        for book in entity_list:
            print(f"ID {book.id}: {book.title} - {book.author}")
