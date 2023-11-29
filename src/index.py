"""Moduuli joka luo ohjelman käyttäjälle"""
from writer import Writer
from app_ui import AppUI
from root import Root
from database_handler import Database
from sql_server import ServerHandler

#from server_handler import ServerHandler
#url = "www.osoite.com"
#server_handler = ServerHandler(url)
#server_handler.get_refs()
my_database_handler = ServerHandler()
my_database_handler.start_up()


app_database = Database('newdb.db')#"database.db")
app_writer = Writer("data.bib")
app_root = Root(app_database, app_writer)

ui = AppUI(app_root)

if __name__ == "__main__":
    ui.run_app()
my_database_handler.end_session()
