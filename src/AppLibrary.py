"""Moduuli joka ..."""
from root import Root
from app_ui import AppUI
from database_handler import Database
from writer import Writer
from stub_io import StubIO

class AppLibrary:
    """
    Apin hyödyntämä kirjasto.
    ...

    Attributes
    ----------
    _io : StubIO([])
        Käyttöliittymä stubi
    root: Root()
        Hyödynnetty root olio
    self.app: AppUI(self.root)
        käytetty UI

    Methods
    -------
    output_should_contain():
        placeholder
    input():
        placeholder
    run_application():
        placeholder
    clear():
        placeholder
    """

    def __init__(self):
        """
        Luokan konstruktori.
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self._io = StubIO([])
        
        self.root = Root(
            Database("robot_data.db"), Writer("robot_bibtex.bib"), cloud_data_handler=None, uses_database=False, io_handler=self._io
        )
        self.app = AppUI(self.root)

    def output_should_contain(self, value):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        if not value in self._io.outputs:
            raise AssertionError(f'Output "{value}" is not in {str(self._io.outputs)}')

    def input(self, value):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self._io.inputs.append(value)

    def run_application(self):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self.app.run_app()

    def clear(self):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self.root.data_handler.clear_database()
        self.root.remove_reference("Kirjailija23")
