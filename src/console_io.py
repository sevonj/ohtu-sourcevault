"""Moduuli joka vastaa syötteen ottamisesta käyttäjältä"""


class ConsoleIO:
    """
    Kuvaus luokan päätehtävästä
    ...

    Attributes
    ----------
    attr : tyyppi
        Kuvaus

    Methods
    -------
    method():
        kuvaus.
    """

    def read_input(self, text):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        return input(text)

    def write_output(self, text):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        print(text)
