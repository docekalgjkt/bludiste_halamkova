from TXT_Format import TXT_Format
from CSV_Format import CSV_Format

class Factory:
    def __init__(self, nacitane_bludiste, format, seznam):
        self.nacitane_bludiste = nacitane_bludiste
        self.format = None
        self.seznam = None
    def poznej_format(self):
        #tato metoda rozpozna, zda je nacitany soubor txt nebo csv, a na zaklade toho pak vola vhodny kod
        if str(self.nacitane_bludiste)[-4:] == ".txt":
            self.format = "txt"
            return self.format
        elif str(self.nacitane_bludiste)[-4:] == ".csv":
            self.format = "csv"
            return self.format
        else:
            pass
    def objekt_nacitajici_soubor(self):
        if self.format == "txt":
            self.format = TXT_Format(self.nacitane_bludiste)
            self.format.nacist_soubor() = self.seznam
            return self.seznam
        elif self.format == "csv":
            self.format = CSV_Format(self.nacitane_bludiste)
            self.format.nacist_soubor() = self.seznam
            return self.seznam
        #tady je kod schopny podle potreby prevzit informace od tridy TXT_Format nebo CSV_Format (podle toho, jakej format metoda poznej_format() identifikuje)


