"""Moduuli joka sisältää käyttöliittymästubin"""


class StubIO:
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

    def __init__(self, inputs):
        """
        Luokan konstruktori.
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self.inputs = inputs
        self.outputs = []

    def read_input(self, msg=""):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        return self.inputs.pop(0)

    def write_output(self, text):
        """
        Kuvaus Funktion toiminnalisuudesta
        ...

        Parameters
        ----------
        muuttuja : tyyppi
            kuvaus
        """
        self.outputs.append(text)
