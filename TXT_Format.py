import csv
class TXT_Format:
    def __init__(self, nacitane_bludiste):
        self.nacitane_bludiste = nacitane_bludiste
    def nacist_soubor(self):
    #tady je blueprint na nacteni txt souboru
        with open(self.nacitane_bludiste, 'r') as file:
            reader = csv.reader(file)
            self.content = list(reader)
        return self.content