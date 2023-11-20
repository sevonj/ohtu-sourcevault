from root import Root
import os

class AppUI:
    def __init__(self, root):
        self.root = root

    def run_app(self):
        while True:
            command = input("1 : create new\n2 : read sources\n3 : create bibtext\n4 : stop\n")

            match command:
                
                case "1":
                    #Uuden lähteen luonti
                    
                    author = input("insert author: ")
                    title = input("insert title: ")
                    publisher = input("insert publisher: ")
                    year = input("insert year: ")
                    source_info = [author, title, publisher, year]
                    self.root.add_source(source_info)
                    
                
                case "2":
                    #Lähteiden lukeminen inhimillisessä muodossa
                    if not self.root.my_sources:
                        print('no sources yet :/ \n')
                    
                    for i, book in enumerate(self.root.my_sources):
                        print(f'Book {i+1}:')
                        print(book)
                        print('\n')
                
                case "3":
                    #Bibtextiin kääntäminen
                    if not self.root.my_sources:
                        print('no sources yet :/ \n')
                    else:
                        print(f'Wrote to: {os.getcwd()}\{self.root.location} \n')
                        self.root.write_sources_bibtex()
                    
                
                case "4":
                    #Lopetus
                    break



