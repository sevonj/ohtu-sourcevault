from writer import Writer


class Root:
    """toiminnan ydin jota UI käskyttää

    ...

    Attributes
    ----------
    sources : list
        lista lähdeolioista
    location : str
        minne tallennetaan

    Methods
    -------
    write_sources_bibtex():
        kirjottaa lähdeoliot bibtexinä tallennuspaikkaan
    add_source():
        lisää annetun lähdeolion lähdelistaan
    """

    def __init__(self, sources = [], location = "src\data"):
        self.my_sources = sources
        self.location   = location


    def write_sources_bibtex(self):
        pass
        # ensin kutsutaan Tuukan tekemä bibtex "muotoilija"
        # muotoilijan luoma bibtex tektsi kirjoitetaan "kirjuri" luokalla

        #
        content = ""
        for source in self.my_sources:
            content.join('Bibtex_Converter(source)'\n\n)
                        
        Writer(self.location, content)
        

    def add_source(self, source_info):
        pass
        self.my_sources.add("Call source_constructor(source_info) here")
