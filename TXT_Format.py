import csv

class TXT_Format:
    def kod(self, nacitane_bludiste):
    #tady je blueprint na nacteni txt souboru
        with open(nacitane_bludiste, 'r') as file:
            reader = csv.reader(file)
            self.content = list(reader)
            return self.content
