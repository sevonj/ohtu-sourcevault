class Writer:
    """Kirjoittaa Rootin antamaa BibTeXiä annettuun lokaatioon"""

    def __init__(self, location, content):
        
        self.location = location
        self.content  = content
    
    def read_from_file(self):
        with open(f"{self.location}", "r") as f:
            
    
    def write_all_to_file(self):


    def write_file(self, name):
        f = open("f{name}.bib", "w")
        f.write(self.content)
        f.close()
        # write_file(location, content, "{name}.BibTeX/LaTeX")