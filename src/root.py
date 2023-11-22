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
    update_database():
        Päivittää tietokannan sisällön ohjelman sulkeutumisen yhteydessä
    remove_reference():
        Poistaa lähdeolion citation_keyn perusteella
    get_reference_by_key():
        Etsii lähdeolion citation_keyn perusteella
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

    def write_sources_bibtex(self):
        """
        Kirjottaa lähdeoliot bibtexinä tallennuspaikkaan.
        ...
       
        """
        self.writer.write_all_to_file(self.my_sources)
    
    def update_database(self):
        """
        Päivittää tietokannan sisällön ohjelman sulkeutumisen yhteydessä
        ...


        """
        self.data_handler.update_database(self.my_sources)

    def read_sources_from_database(self):
        """
        Hakee tietokantaan tallennetut lähdeoliot
        ...
        
        """
        try:
            self.my_sources = self.data_handler.get_all_references()
        except:
            pass


    def add_source(self, ref):
        """
        Lisää annetun lähdeolion lähdelistaan.
        ...

        Parameters
        ----------
        source_info : Reference
            Lähdeolion tiedot.
        """
        while True:
            found_duplicate = False
            for existing_ref in self.my_sources:
                if existing_ref.citation_key == ref.citation_key:
                    # Duplicate, so modify <ref> to fit
                    ref.citation_key += ref.citation_key[-1]
                    found_duplicate = True
            if not found_duplicate:
                break
        
        self.my_sources.append(ref)
    
    def remove_reference(self, citation_key):
        """
        Poistaa lähdeolion citation_keyn perusteella
        ...

        Parameters
        ----------
        citation_key : str
            Lähdeolion citation_key.
        """
        for i, ref in enumerate(self.my_sources):
            if ref.citation_key == citation_key:
                self.my_sources.pop(i)
                return True
        return False
    
    def get_reference_by_key(self, citation_key):
        """
        Etsii lähdeolion citation_keyn perusteella
        ...

        Parameters
        ----------
        citation_key : str
            Lähdeolion citation_key.
        """
        for ref in self.my_sources:
            if ref.citation_key == citation_key:
                return ref
        return False