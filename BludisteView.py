from tkinter import Tk, Canvas

class BludisteView:
    def __init__(self, seznam):
        self.seznam = seznam
        self.c = 0
        self.r = 0
        self.velikost_policka = 25

    def vygenerovat_GUI(self):
        root = Tk()
        root.title("Bludiste")
        canvas = Canvas(root, width=self.velikost_policka*len(self.seznam[0]), height=self.velikost_policka*len(self.seznam[0]), bg="white")
        canvas.pack()

        def vytvorit_ctverec(r, c, velikost_policka, barva_policka, barva_okraju):
            x1 = c * velikost_policka
            y1 = r * velikost_policka
            x2 = x1 + velikost_policka
            y2 = y1 + velikost_policka
            canvas.create_rectangle(x1, y1, x2, y2, fill=barva_policka, outline=barva_okraju)

        for i in self.seznam:
            for j in i:
                if j == "1":
                    vytvorit_ctverec(self.r, self.c, self.velikost_policka, "black", "black")
                elif j == "0":
                    vytvorit_ctverec(self.r, self.c, self.velikost_policka, "white", "white")
                elif j == "s":
                    vytvorit_ctverec(self.r, self.c, self.velikost_policka, "blue", "blue")
                elif j == "f":
                    vytvorit_ctverec(self.r, self.c, self.velikost_policka, "orange", "orange")
                else:
                    pass
                self.c += 1
            self.c = 0
            self.r += 1

        root.mainloop()
