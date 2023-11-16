from source_constructor import generate_book

def SourceStub():
    lähteet = []
    
    for i in range(5):
        lähteet.append(generate_book('Kirjailija_{i}', 'Kirja_{i}', 'Julkaisija_{i}', '{i}'))
    
    return lähteet