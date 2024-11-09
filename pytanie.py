class Pytanie:
    numer: int
    tresc: list[str]
    poprawna_odpowiedz: str
    odpowiedzi: list[list[str]]

    def __init__(self, numer, tresc, poprawna_odpowiedz, odpowiedzi):
        self.numer = numer
        self.tresc = tresc
        self.poprawna_odpowiedz = poprawna_odpowiedz
        self.odpowiedzi = odpowiedzi