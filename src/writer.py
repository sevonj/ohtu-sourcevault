


class Writer:
    """Kirjoittaa Rootin antamaa BibTeXiä annettuun lokaatioon"""

    def __init__(self, location, content):
        
        self.location = location
        self.content  = content

    def write_file(self, name):
        f = open("{name}.bib", "w")
        f.write(self.content)
        f.close()
        # write_file(location, content, "{name}.BibTeX/LaTeX")