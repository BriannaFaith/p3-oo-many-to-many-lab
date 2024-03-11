from datetime import datetime
class Author:
    all_authors = []
    def __init__(self, name):
        if not isinstance(name,str):
            raise Exception(f'{name} is not a string')
        self.name = name
        Author.all_authors.append(self)
        self._contracts= []

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]
    def books(self):
        return [contract.book for contract in self.contracts()]
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all_contracts if contract.author == self])



class Book:
    all_books= []
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception(f'{title} must be a string')
        self.title = title
        self.all_books.append(self)
    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]
    def authors(self):
        return [contract.author for contract in Contract.all_contracts if contract.book == self]


class Contract:
    all_contracts = []
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception(f'{author} is not an Author object')
        self.author = author

        if not isinstance(book,Book):
            raise Exception(f'{book} is not a Book object')
        self.book = book

        if not isinstance(date, str):
            raise Exception(f'{date} is not a string')
        self.date = date

        if not isinstance(royalties, int):
            raise Exception(f'{royalties} is not an integer')
        self.royalties = royalties
        self.all_contracts.append(self)


