from tkinter import Tk, Canvas
import csv

with open('maze_medium.csv', 'r') as file:
    reader = csv.reader(file)
    content = list(reader)

c = 0
r = 0
velikost_policka = 25

root = Tk()
root.title("Bludiste")
canvas = Canvas(root, width=velikost_policka * len(content[0]), height=velikost_policka * len(content[0]), bg="white")
canvas.pack()


def vytvorit_ctverec(r, c, velikost_policka, barva_policka, barva_okraju):
    x1 = c * velikost_policka
    y1 = r * velikost_policka
    x2 = x1 + velikost_policka
    y2 = y1 + velikost_policka
    canvas.create_rectangle(x1, y1, x2, y2, fill=barva_policka, outline=barva_okraju)


for i in content:
    for j in i:
        if j == "1":
            vytvorit_ctverec(r, c, velikost_policka, "black", "black")
        elif j == "0":
            vytvorit_ctverec(r, c, velikost_policka, "white", "white")
        elif j == "s":
            vytvorit_ctverec(r, c, velikost_policka, "blue", "blue")
        elif j == "f":
            vytvorit_ctverec(r, c, velikost_policka, "orange", "orange")
        else:
            pass
        c += 1
    c = 0
    r += 1

for i in content:
    print(i)

root.mainloop()
