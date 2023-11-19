class Book:
    def __init__(self, author:str, title:str, publisher:str, year:int, tags:list=None):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.tags = tags
    
    def generate_dict(self):
        return {"author": self.author, "title": self.title, "year": self.year, "publisher": self.publisher}
    def __str__(self):
        return f"{self.author}. {self.title}.\n{self.publisher}, {self.year}"


