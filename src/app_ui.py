from root import Root
from reference import Reference
import os

class AppUI:
    def __init__(self, root):
        self.root = root

    def run_app(self):
        self.root.read_sources_from_database()
        
        while True:
            command = input(("1 : create new\n2 : read sources\n3 : create bibtext\n4 : list all citation keys\n"
                            "5 : show based on citation key\n6 : delete based on citation key\n7 : exit program\n"))

            match command:
                
                case "1":
                    #Uuden lähteen luonti

                    skip = False
                    reference_type = ""
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
                            reference_type = "book"
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
                            reference_type = "article"
                        elif source_type == "3":
                            author = input("insert author: ")
                            title = input("insert title: ")
                            year = input("insert year: ")
                            booktitle = input("insert booktitle: ")

                            fields_data["author"] = author
                            fields_data["title"] = title
                            fields_data["year"] = year
                            fields_data["booktitle"] = booktitle
                            reference_type = "inproceeding"
                        elif source_type == "4":
                            skip = True
                        else:
                            print("Please print a valid option")
                            continue

                        break
                            
                    if skip:
                        continue

                    ref = Reference(reference_type, **fields_data)
                    ref.citation_key = ref.generate_citation_key()
                    
                    tags = []
                        
                    while True:
                        # Read tags
                        tag = input("Enter a tag or type q to stop: ").strip()
                        if tag == "q":
                            break
                        else:
                            tags.append(tag)
                    
                    ref.tags = tags
                    
                    self.root.add_source(ref)
                    
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
                    # listaa kaikki citation_keyt
                    print(f"There exists {len(self.root.my_sources)} citation keys:")
                    for ref in self.root.my_sources:
                        print(ref.citation_key)
                
                case "5":
                    citation_key = input("Enter the citation key of the reference you wish to examine: ")
                    ref = self.root.get_reference_by_key(citation_key)

                    if not ref:
                        print(f"Citation key {citation_key} did not match any references\n")
                    else:
                        print(str(ref))
                
                case "6":
                    # poista citation_key:n perusteella
                    citation_key = input("Enter the citation key of the reference you wish to remove: ").strip()
                    if self.root.remove_reference(citation_key):
                        print("Citation removed succesfully.")
                    else:
                        print("No such citation.")
                
                case "7":
                    #Lopetus
                    break
        self.root.update_database()