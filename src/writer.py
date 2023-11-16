from bibtex_converter import convert_to_bibtex
from reference import Reference
import re

class Writer:
    """Kirjoittaa Rootin antamaa BibTeXiä annettuun lokaatioon"""

    def __init__(self, location, content = []):
        self.location = location
        self.content = content
    
    def read_from_file(self):
        with open(self.location, "r") as file:
            data = file.read()

            # Etsitään kaikki BibTeX-viitteet
            entries = re.findall(r'@\w+\{[^@]+', data)
            for entry in entries:
                # Etsitään kenttien tiedot
                ref_type, ref_body = entry.split('{', 1)
                ref_type = ref_type.strip('@').strip()

                # Parsitaan kentät
                fields = re.findall(r'(\w+)\s*=\s*\{(.+?)\}', ref_body, re.DOTALL)
                fields_dict = {field.strip() : value.strip() for field, value in fields}

                self.content.append(Reference(ref_type, **fields_dict))

    
    def write_all_to_file(self):
        if self.content != []:
            with open(self.location, "w") as file:
                for ref in self.content:
                    bibtex_str = convert_to_bibtex(ref.reference_type, **ref.fields)
                    file.write(bibtex_str)

