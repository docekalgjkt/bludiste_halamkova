from TXT_Format import *
from CSV_Format import *
from NacistSeznam import *

class Factory:
    def __init__(self, nacitane_bludiste, file_format):
        self.nacitane_bludiste = nacitane_bludiste
        if file_format == "txt":
            self.helper = TXT_Format() 
        if file_format == "csv":
            self.helper = CSV_Format()
    def objekt_nacitajici_soubor(self):
        return self.helper.kod(self.nacitane_bludiste)
