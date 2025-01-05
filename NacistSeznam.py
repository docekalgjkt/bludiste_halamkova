from Factory import Factory
#
class NacistSeznam:
    def __init__(self, nacitane_bludiste, bludiste):
        self.nacitane_bludiste = nacitane_bludiste
        self.bludiste = bludiste
    def vytvor_bludiste(self):
        #potreba zavolat tridu Factory, ktera teto tride poskytne vhodny kod pro zpracovani nacitaneho souboru (pozna, zda je soubor txt nebo csv a podle toho zavola TXT_Format nebo CSV_Format)
        self.nacitane_bludiste = Factory()
        self.bludiste = self.nacitane_bludiste.poznej_format()
        self.bludiste
        return self.bludiste