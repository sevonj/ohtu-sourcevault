from root import Root
import os

class AppUI:
    def __init__(self, root):
        self.root = root

    def run_app(self):
        self.root.read_sources_from_file()
        
        while True:
            command = input("1 : create new\n2 : read sources\n3 : create bibtext\n4 : stop\n")

            match command:
                
                case "1":
                    #Uuden lähteen luonti

                    skip = False
                    fields_data = {}

                    while True:
                        source_type = input("Choose source type (type a number):\n1. Book\n2. Article\n3. Inproceeding\n4. Cancel operation\nChoice: ")
                        if source_type == "1":
                            author = input("insert author: ")
                            title = input("insert title: ")
                            year = input("insert year: ")
                            publisher = input("insert publisher: ")

                            fields_data["author"] = author
                            fields_data["title"] = title
                            fields_data["year"] = year
                            fields_data["publisher"] = publisher
                            self.root.add_source("book", fields_data)
                        elif source_type == "2":
                            author = input("insert author: ")
                            title = input("insert title: ")
                            journal = input("insert journal: ")
                            year = input("insert year: ")
                            volume = input("insert volume: ")
                            pages = input("insert pages (for example 38--46): ")

                            fields_data["author"] = author
                            fields_data["title"] = title
                            fields_data["journal"] = journal
                            fields_data["year"] = year
                            fields_data["volume"] = volume
                            fields_data["pages"] = pages
                            self.root.add_source("article", fields_data)
                        elif source_type == "3":
                            author = input("insert author: ")
                            title = input("insert title: ")
                            year = input("insert year: ")
                            booktitle = input("insert booktitle: ")

                            fields_data["author"] = author
                            fields_data["title"] = title
                            fields_data["year"] = year
                            fields_data["volume"] = booktitle
                            self.root.add_source("inproceeding", fields_data)
                        elif source_type == "4":
                            skip = True
                        else:
                            print("Please print a valid option")
                            continue

                        break
                            
                    
                    if skip:
                        continue
                    
                    print("Reference added")

                    
                    
                
                case "2":
                    #Lähteiden lukeminen inhimillisessä muodossa
                    if not self.root.my_sources:
                        print('no sources yet :/ \n')
                    
                    for i, ref in enumerate(self.root.my_sources):
                        print(f'Reference {i+1}:')
                        print(ref)
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



