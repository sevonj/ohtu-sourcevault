class Book:
    def __init__(self, author:str, title:str, publisher:str, year:int, tags:list=None):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.tags = tags
    
    def __str__(self):
        return f"{self.author}. {self.title}.\n{self.publisher}, {self.year}"

def generate_book(author:str, title:str, publisher:str, year:int):
    return Book(author, title, publisher, year)

if __name__ == "__main__":
    book = generate_book("ville", "villen kirja", "villen kustantamo", 2023)
    print(book)