"""Moduuli joka luo ohjelman käyttäjälle"""
from dotenv import dotenv_values
from writer import Writer
from app_ui import AppUI
from root import Root
from database_handler import Database
from sql_server import ServerHandler

env_config = dotenv_values(".env")
aws_key = env_config["AWS_ACCESS_KEY_ID"]
aws_secret_key = env_config["AWS_SECRET_ACCESS_KEY"]

app_cloud_database = ServerHandler(
    aws_key, aws_secret_key, "database.db", "tietokanta.db", "sourcevaultbucket"
)
app_database = Database("database.db")
app_writer = Writer("data.bib")
app_root = Root(app_database, app_writer, app_cloud_database)

ui = AppUI(app_root)

if __name__ == "__main__":
    ui.run_app()
