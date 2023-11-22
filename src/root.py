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

    def __init__(self, data_handler, writer, sources = [], location = "data.bib"):
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
        self.data_handler = data_handler
        self.writer = writer
        self.writer.location = location
        self.my_sources = sources
        self.location   = location
        #todo:
        #self.database = database
        #self.my_sources = self.database.get_sources()


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
    
    def remove_reference(self, citation_key):
        for i, ref in enumerate(self.my_sources):
            if ref.citation_key == citation_key:
                self.my_sources.pop(i)
                return True
        return False