from writer import Writer
from bibtex_converter import convert_to_bibtex
from source_constructor import Book


class Root:
    """
    Toiminnan ydin jota UI käskyttää.
    ...

    Attributes
    ----------
    my_sources : list
        Lista lähdeolioista.
    location : str
        Minne tallennetaan.

    Methods
    -------
    write_sources_bibtex():
        Kirjottaa lähdeoliot bibtexinä tallennuspaikkaan.
    add_source():
        Lisää annetun lähdeolion lähdelistaan.
    """

    def __init__(self, sources = [], location = "src\data"):
        """
        Luokan konstruktori.
        ...

        Parameters
        ----------
        sources : list
            Lista lähdeolioista.
        location : str
            Minne tallennetaan.
        """
        self.my_sources = sources
        self.location   = location


    def write_sources_bibtex(self):
        """
        Kirjottaa lähdeoliot bibtexinä tallennuspaikkaan.
        ...
        """
        content="\n".join([convert_to_bibtex('book', source) for source in self.my_sources])
        Writer(self.location, content)


    def add_source(self, source_info):
        """
        Lisää annetun lähdeolion lähdelistaan.
        ...

        Parameters
        ----------
        source_info : str
            Lähdeolion tiedot string-muodossa.
        """
        self.my_sources.add(Book(source_info[0], source_info[1], source_info[2], source_info[3]))
