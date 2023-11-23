from reference import Reference

def SourceStub():
    lähteet = []
    
    for i in range(5):
        kirja = Reference(f'Kirjailija_{i}', f'Kirja_{i}', f'Julkaisija_{i}', f'{i}')
        lähteet.append(kirja)
    
    return lähteet