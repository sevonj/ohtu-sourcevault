from writer import Writer
from app_ui import AppUI
from root import Root

app_writer = Writer("data.bib")
app_root = Root(app_writer)

ui = AppUI(app_root)

if __name__ == "__main__":
    ui.run_app()