class Author:

    all = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    
    all = []

    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author: Author, book: Book, date: str, royalties: int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class.")
        else:
            self._author = author
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class.")
        else:
            self._book = book

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string.")
        else:
            self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer.")
        else:
            self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        matching_contracts = []
        for contract in cls.all:
            if contract.date == date:
                matching_contracts.append(contract)
        return matching_contracts