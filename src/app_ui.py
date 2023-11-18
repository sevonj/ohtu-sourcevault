from root import Root

class AppUI:
    def __init__(self):
        self.value = 1

    def run_app(self):
        while True:
            command = input("1 : create new\n2 : read sources\n3 : create bibtext\n4 : stop\n")

            match command:
                
                case "1":
                    #Uuden lähteen luonti
                    pass
                    """
                    author = input("insert author")
                    title = input("insert title")
                    publisher = input("insert publisher")
                    year = input("insert year")
                    source_info = [author, title, publisher, year]
                    Root.add_source(source_info[0], source_info[1], source_info[2], source_info[3])
                    """
                
                case "2":
                    #Lähteiden lukeminen inhimillisessä muodossa
                    """
                    for book in Root.sources:
                        print(book)
                    """
                    pass
                
                case "3":
                    #Bibtextiin kääntäminen
                    """
                    Root.write_sources_bibtex()
                    """
                    pass
                
                case "4":
                    #Lopetus
                    break

if __name__ == "__main__":
    ui = AppUI()
    ui.run_app()

