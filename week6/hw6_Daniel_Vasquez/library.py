class LibraryMember:
    def __init__(self, member_id:str,name:str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def add_book(self,book_title):
        if book_title not in self.borrowed_books:
            self.borrowed_books.append(book_title)
        else:
            raise ValueError(f"{book_title} is already checked out")

    def remove_book(self,book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
        else:
            raise ValueError(f"{book_title} not found.")
        
    def count_books(self):
        return len(self.borrowed_books)

    def __str__(self):
        return f"LibraryMember(member_id='{self.member_id}', name='{self.name}', total_borrowed={self.count_books()})"
    
    def __repr__(self):
        return self.__str__()