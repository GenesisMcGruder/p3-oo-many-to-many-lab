class Author:
    all = []
    def __init__(self, name):
        if isinstance(self, Author):
            self.name = name
            Author.all.append(self)
        else:
            raise Exception('N/A')

    def contracts(self):
        related_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                related_contracts.append(contract)
        return related_contracts

    def books(self):
        related_books = []
        for contract in Contract.all:
            if contract.author == self:
                related_books.append(contract.book)
        return related_books

    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        totals = []
        for contract in Contract.all:
            if contract.author == self:
                totals.append(contract.royalties)
                complete_total = sum(totals)
        return complete_total


class Book:
    all = []
    def __init__(self, title):
        if isinstance(self, Book):
            self.title = title
            Book.all.append(self)
        else:
            raise Exception('N/A')
    
    def contracts(self):
        book_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                book_contracts.append(contract)
        return book_contracts

    def authors(self):
        book_authors = []
        for contract in Contract.all:
            if contract.book == self:
                book_authors.append(contract.author)
        return book_authors


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception('N/A')
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception('N/A')
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception('N/A')
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception('N/A')
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        sorted_date = []
        for contract in Contract.all:
            if contract.date == date:
                sorted_date.append(contract)
        return sorted_date