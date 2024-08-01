import pdb

class Author:

    all_authors = []

    def __init__(self, name: str):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)

    def contracts(self):
        return self._contracts
    
    def add_contract(self, contract):
        self._contracts.append(contract)

class Book:

    all_books = []

    def __init__(self, title: str):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def add_contract(self, contract):
        self._contracts.append(contract)


class Contract:

    all_contracts = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        if not isinstance(author, Author):
            raise Exception("Author must be instance of Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be instance of Book class.")
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)