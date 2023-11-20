from writer import Writer
from bibtex_converter import convert_to_bibtex
from reference import Reference


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

    def __init__(self, writer, sources = [], location = "data.bib"):
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
        self.writer = writer
        self.writer.location = location
        self.my_sources = sources
        self.location   = location


    def write_sources_bibtex(self):
        """
        Kirjottaa lähdeoliot bibtexinä tallennuspaikkaan.
        ...
       
        """
        self.writer.write_all_to_file(self.my_sources)

    def read_sources_from_file(self):
        try:
            self.my_sources = self.writer.read_from_file()
        except:
            pass


    def add_source(self, source_type, source_fields):
        """
        Lisää annetun lähdeolion lähdelistaan.
        ...

        Parameters
        ----------
        source_info : str
            Lähdeolion tiedot string-muodossa.
        """
        self.my_sources.append(Reference(source_type, **source_fields))