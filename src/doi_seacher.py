""" Kirjasto DOI-hakuja varten """
import re
from habanero import cn
from reference import Reference

class DOISearcher:
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
    def __init__(self):
        pass

    def find_by_doi(self, doi="10.48550/arxiv.2304.08505"):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        entry = cn.content_negotiation(ids=doi, format="bibentry")
        ref_type, rest = entry.split("{", 1)
        ref_key, fields_part = rest.split(",", 1)

        ref_type = ref_type.strip().strip("@").strip()
        ref_key = ref_key.strip()

        fields = re.findall(r'(\w+)\s*=\s*(?:\{([^}]+)\}|(\w+))', fields_part)
        all_fields = {field: value or month for field, value, month in fields}

        fields_by_type = {
            'book': {'author', 'title', 'year', 'publisher'},
            'article': {'author', 'title', 'journal', 'year', 'volume', 'pages'},
            'inproceedings': {'author', 'title', 'year', 'booktitle'},
            'misc': {'author', 'title', 'howpublished', 'year', 'note'},
            'phdthesis': {'author', 'title', 'year', 'school', 'address', 'month'},
        }

        required_fields = fields_by_type.get(ref_type, set())
        parsed_fields = {field: value for field, value in all_fields.items() if field in required_fields}

        return Reference(ref_type, ref_key, tags=[], **parsed_fields)
