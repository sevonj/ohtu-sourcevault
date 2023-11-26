"""Moduuli joka vastaa tiedostojen lukemista ja kirjoittamisesta"""
import re
from bibtex_converter import convert_to_bibtex
from reference import Reference



class Writer:
    """
    Kuvaus luokan päätehtävästä
    ...

    Attributes
    ----------
    attr : tyyppi
        Kuvaus

    Methods
    -------
    method():
        kuvaus.
    """

    def __init__(self, location):
        """
        Luokan konstruktori.
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self.location = location

    def read_from_file(self):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        refs = []
        with open(self.location, "r", encoding="utf-8") as file:
            data = file.read()

            # Etsitään kaikki BibTeX-viitteet
            entries = re.findall(r"@\w+\{[^@]+", data)
            for entry in entries:
                # Etsitään kenttien tiedot
                ref_type, ref_body = entry.split("{", 1)
                ref_type = ref_type.strip("@").strip()

                # Parsitaan kentät
                fields = re.findall(r"(\w+)\s*=\s*\{(.+?)\}", ref_body, re.DOTALL)
                fields_dict = {field.strip(): value.strip() for field, value in fields}

                refs.append(Reference(ref_type, **fields_dict))
        return refs

    def write_all_to_file(self, content):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        if content != []:
            with open(self.location, "w", encoding="utf-8")  as file:
                for ref in content:
                    bibtex_str = convert_to_bibtex(ref.reference_type, **ref.fields)
                    file.write(bibtex_str)
