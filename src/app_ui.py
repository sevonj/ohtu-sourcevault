from root import Root
from reference import Reference
import os

class AppUI:
    def __init__(self, root):
        self.root = root

    def run_app(self):
        self.root.read_sources_from_database()
        
        while True:
            command = self.root.io_handler.read_input(("\n1 : create new\n2 : list sources as text\n3 : create bibtext\n4 : list all citation keys\n"
                            "5 : show based on citation key\n6 : delete based on citation key\n7 : find based on a tag\n8 : exit program\n"))

            match command:
                
                case "1":
                    #Uuden lähteen luonti

                    skip = False
                    reference_type = ""
                    fields_data = {}

                    while True:
                        source_type = self.root.io_handler.read_input("Choose source type (type a number):\n1. Book\n2. Article\n3. Inproceeding\n4. Cancel operation\nChoice: ")
                        required_fields = []
                        match source_type:
                            case "1":
                                required_fields = "author|title|year|publisher"
                                reference_type = "book"
                            case "2":
                                required_fields = "author|title|journal|year|volume|pages"
                                reference_type = "article"
                            case "3":
                                required_fields = "author|title|year|booktitle"
                            case "4":
                                break
                            case default:
                                self.root.io_handler.write_output("Please print a valid option")
                                continue

                                for field in required_fields.split("|"):
                                    fields_data[field] = self.root.io_handler.read_input(f"insert {field}")                    

                        break
                            
                    if skip:
                        continue

                    ref = Reference(reference_type, **fields_data)
                    ref.citation_key = ref.generate_citation_key()
                    
                    tags = []
                        
                    while True:
                        # Read tags
                        tag = self.root.io_handler.read_input("Enter a tag or type q to stop: ").strip()
                        if tag == "q":
                            break
                        else:
                            tags.append(tag)
                    
                    ref.tags = tags
                    
                    self.root.add_source(ref)
                    
                    self.root.io_handler.write_output("Reference added")

                case "2":
                    #Lähteiden lukeminen inhimillisessä muodossa
                    if not self.root.my_sources:
                        self.root.io_handler.write_output('no sources yet :/ \n')
                    
                    for i, ref in enumerate(self.root.my_sources):
                        self.root.io_handler.write_output(f'Reference {i+1}:')
                        self.root.io_handler.write_output(ref)
                        self.root.io_handler.write_output('\n')
                
                case "3":
                    #Bibtextiin kääntäminen
                    if not self.root.my_sources:
                        self.root.io_handler.write_output('no sources yet :/ \n')
                    else:
                        self.root.io_handler.write_output(f'Wrote to: {os.getcwd()}\{self.root.location} \n')
                        self.root.write_sources_bibtex()
                
                case "4":
                    # listaa kaikki citation_keyt
                    self.root.io_handler.write_output(f"There exists {len(self.root.my_sources)} citation keys:")
                    for ref in self.root.my_sources:
                        self.root.io_handler.write_output(ref.citation_key)
                
                case "5":
                    citation_key = self.root.io_handler.read_input("Enter the citation key of the reference you wish to examine: ")
                    ref = self.root.get_reference_by_key(citation_key)

                    if not ref:
                        self.root.io_handler.write_output(f"Citation key {citation_key} did not match any references\n")
                    else:
                        self.root.io_handler.write_output(str(ref))
                
                case "6":
                    # poista citation_key:n perusteella
                    citation_key = self.root.io_handler.read_input("Enter the citation key of the reference you wish to remove: ").strip()
                    if self.root.remove_reference(citation_key):
                        self.root.io_handler.write_output("Citation removed succesfully.")
                    else:
                        self.root.io_handler.write_output("No such citation.")
                
                case "7":
                    tag_search = self.root.io_handler.read_input("Enter the tag you want to search by or q to quit: ").strip()
                    if tag_search == "q":
                        continue

                    found_refs = list(filter(lambda x: tag_search in x.tags, self.root.my_sources))

                    if len(found_refs) == 0:
                        self.root.io_handler.write_output(f"No sources found with tag {tag_search}!")
                    else:
                        self.root.io_handler.write_output(f"Found {len(found_refs)} references with tag: {tag_search}\n")
                        for ref in found_refs:
                            self.root.io_handler.write_output(str(ref))
                    
                
                case "8":
                    #Lopetus
                    break
        self.root.update_database()