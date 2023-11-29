import boto3
import sqlite3
from os import getenv
from database_handler import Database
from reference import Reference

class ServerHandler:
    def __init__(self):
        print(getenv("AWS_ACCESS_KEY_ID"))
        self.s3 = boto3.client(
            's3',
            aws_access_key_id="key",
            aws_secret_access_key="key",
            region_name='eu-north-1'
            )
        

    def get_references(self, bucketname:str, remote_db_name:str, local_path:str):
        self.s3.download_file(bucketname, remote_db_name, local_path)

    def upload_references(self, local_path:str, bucketname:str, remote_db_name:str):
        self.s3.upload_file(local_path, bucketname, remote_db_name)
    
    def start_up(self):
        self.get_references("sourcevaultbucket", "tietokanta.db", "newdb.db")
    
    def end_session(self):
        self.upload_references("newdb.db", "sourcevaultbucket", "tietokanta.db")