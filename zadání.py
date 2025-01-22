from BludisteView import *
from Bludiste import *
from NacistSeznam import *
from Factory import *
from TXT_Format import *
from CSV_Format import *

nacitane_bludiste = 'maze_big.txt'

seznam = NacistSeznam(nacitane_bludiste)
format = seznam.poznej_format()
bludiste = Bludiste(seznam.vyuzit_factory())
bludiste_GUI = BludisteView(bludiste.seznam)
bludiste_GUI.vygenerovat_GUI()
