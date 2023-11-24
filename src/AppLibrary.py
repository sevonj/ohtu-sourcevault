from root import Root
from app_ui import AppUI
from database_handler import Database
from writer import Writer
from stub_io import StubIO

class AppLibrary:
    def __init__(self):
        self._io=StubIO([])
        self.root=Root(Database("robot_data.db"), Writer("robot_bibtex.bib"), self._io)
        self.app=AppUI(self.root)

    def output_should_contain(self, value):
        if not value in self._io.outputs:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(self._io.outputs)}"
            )

    def input(self, value):
        self._io.inputs.append(value)

    def run_application(self):
        self.app.run_app()

    def clear(self):
        self.root.data_handler.clear_database()
        self.root.remove_reference("Kirjailija23")
