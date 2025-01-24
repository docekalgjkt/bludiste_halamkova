from Factory import *

class NacistSeznam:
    def __init__(self, nacitane_bludiste):
        self.nacitane_bludiste = nacitane_bludiste
    def poznej_format(self):
        #tato metoda rozpozna, zda je nacitany soubor txt nebo csv, a na zaklade toho pak vola vhodny kod ze tridy Factory
        if str(self.nacitane_bludiste)[-4:] == ".txt":
            self.file_format = "txt"
            return self.file_format
        elif str(self.nacitane_bludiste)[-4:] == ".csv":
            self.file_format = "csv"
            return self.file_format
        else:
            pass

    def vyuzit_factory(self):
        seznam = Factory(self.nacitane_bludiste, self.file_format)
        return seznam.objekt_nacitajici_soubor()

