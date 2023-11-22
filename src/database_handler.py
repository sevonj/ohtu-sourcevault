import sqlite3
from reference import Reference


class Database:
    def __init__(self, location):
        self.location = location

    def add_reference_to_database(self, reference):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO bibtex_references (citation_key, reference_type, author, title, year, booktitle, volume, pages, journal, publisher) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (reference.citation_key,
             reference.reference_type,
             reference.fields.get('author'),
             reference.fields.get('title'),
             reference.fields.get('year'),
             reference.fields.get('booktitle'),
             reference.fields.get('volume'),
             reference.fields.get('pages'),
             reference.fields.get('journal'),
             reference.fields.get('publisher')))

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
                journal TEXT,
                publisher TEXT
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
    
    def get_all_references(self):
        connection = sqlite3.connect(self.location)
        cursor = connection.cursor()

        # Hae viitteet
        cursor.execute('SELECT * FROM bibtex_references')
        references_rows = cursor.fetchall()

        references = []
        for row in references_rows:
            # Hae tagit
            cursor.execute('SELECT tag FROM bibtex_tags WHERE reference_id = ?', (row[0],))
            tags = [tag_row[0] for tag_row in cursor.fetchall()]

            reference = None
            if row[2] == "book":
                reference = Reference(
                    reference_type=row[2],
                    citation_key=row[1],
                    tags=tags,
                    author=row[3],
                    title=row[4],
                    year=row[5],
                    publisher=row[10]
                )
            elif row[2] == "article":
                reference = Reference(
                    reference_type=row[2],
                    citation_key=row[1],
                    tags=tags,
                    author=row[3],
                    title=row[4],
                    journal=row[9],
                    year=row[5],
                    volume=row[7],
                    pages=row[8]
                )
            elif row[2] == "inproceeding":
                reference = Reference(
                    reference_type=row[2],
                    citation_key=row[1],
                    tags=tags,
                    author=row[3],
                    title=row[4],
                    year=row[5],
                    booktitle=row[6]
                )

            references.append(reference)

        connection.close()
        return references

    def update_database(self, refs:list):
        connection = sqlite3.connect(self.location)
        self.clear_database()
        self.initialize_database()

        for ref in refs:
            self.add_reference_to_database(ref)
        
        connection.commit()
        connection.close()