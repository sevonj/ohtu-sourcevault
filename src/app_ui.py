from root import Root

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
                    for book in self.root.my_sources:
                        print(book)
                
                case "3":
                    #Bibtextiin kääntäminen
                    
                    self.root.write_sources_bibtex()
                    
                
                case "4":
                    #Lopetus
                    break



