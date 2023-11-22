def convert_to_bibtex(type, **fields):
    """
    Luo BibTeX-viitteen.

    :param type: Viitteen tyyppi, esim. 'article', 'book'.
    :param fields: Avain-arvo -parit, jotka kuvaavat viitettä (esim. author='Martin, Robert', title='Kirjan nimi').
    :return: BibTeX merkkijonomuodossa.
    """
    names = str(fields.get("author")).split(" and ")
    identifier = "".join(s.split()[-1][0] for s in names)

    if len(names) == 1:
        identifier = names[0].split(", ")[0]
    
    identifier += str(fields.get("year"))[-2:]
    bibtex_str = f"@{type}" + "{" + f"{identifier},\n"
    for field, value in fields.items():
        bibtex_str += f"    {field} = {{{value}}},\n"
    return bibtex_str + "}\n"
