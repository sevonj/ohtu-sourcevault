import sqlite3
from reference import Reference


class Database:
    def __init__(self, location):
        self.location = location

    def add_reference_to_database(self, reference):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO bibtex_references (citation_key, reference_type, author, title, year, booktitle, volume, pages, journal) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (reference.citation_key,
             reference.reference_type,
             reference.fields.get('author'),
             reference.fields.get('title'),
             reference.fields.get('year'),
             reference.fields.get('booktitle'),
             reference.fields.get('volume'),
             reference.fields.get('pages'),
             reference.fields.get('journal')))

        reference_id = cursor.lastrowid

        if reference.tags:
            for tag in reference.tags:
                cursor.execute('INSERT INTO bibtex_tags (reference_id, tag) VALUES (?, ?)',
                               (reference_id, tag))

        connection.commit()
        connection.close()


    def clear_database(self):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS bibtex_references')
        cursor.execute('DROP TABLE IF EXISTS bibtex_tags')

        connection.commit()
        connection.close()

    def initialize_database(self):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bibtex_references (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                citation_key TEXT UNIQUE NOT NULL,
                reference_type TEXT NOT NULL,
                author TEXT,
                title TEXT NOT NULL,
                year INTEGER,
                booktitle TEXT,
                volume INTEGER,
                pages TEXT,
                journal TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bibtex_tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reference_id INTEGER,
                tag TEXT NOT NULL,
                FOREIGN KEY (reference_id) REFERENCES bibtex_references (id)
            )
        ''')

        connection.commit()
        connection.close()