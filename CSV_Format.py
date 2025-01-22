import csv

class CSV_Format:
    def kod(self, nacitane_bludiste):
    #stejny pro csv
        with open(nacitane_bludiste, 'r') as file:
            reader = csv.reader(file)
            self.content = list(reader)
            return self.content
