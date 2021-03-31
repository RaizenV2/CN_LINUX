from tkinter import *
from hw4 import *

a1, b1, c1, n1, q1, p1 = read_tridiagonal_data("a1.txt")
a2, b2, c2, n2, q2, p2 = read_tridiagonal_data("a2.txt")
a3, b3, c3, n3, q3, p3 = read_tridiagonal_data("a3.txt")
a4, b4, c4, n4, q4, p4 = read_tridiagonal_data("a4.txt")

f1 = read_free_terms("f1.txt")
f2 = read_free_terms("f2.txt")
f3 = read_free_terms("f3.txt")
f4 = read_free_terms("f4.txt")

def afiseaza_solutie(a, b, c, f, p, q, label):
    final, iteratie = Gauss_Seidel(a, b, c, f, p, q)
    text = str(final[:6]) + "..."
    text += "\nNumar de iteratii: " + str(iteratie)
    label.config(text=text)


def gui(top):

    btn1 = Button(top, text="Solutie F1", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(a1, b1, c1, f1, p1, q1, M1))
    btn1.pack()

    M1 = Label(top, text="", font="Georgia 12 bold", fg="white")
    M1.pack()

    btn2 = Button(top, text="Solutie F2", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(a2, b2, c2, f2, p2, q2, M2))
    btn2.pack()

    M2 = Label(top, text="", font="Georgia 12 bold", fg="white")
    M2.pack()

    btn3 = Button(top, text="Solutie F3", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(a3, b3, c3, f3, p3, q3, M3))
    btn3.pack()

    M3 = Label(top, text="", font="Georgia 12 bold", fg="white")
    M3.pack()

    btn4 = Button(top, text="Solutie F4", font="Georgia 10 italic bold",
                  command=lambda: afiseaza_solutie(a4, b4, c4, f4, p4, q4, M4))
    btn4.pack()

    M4 = Label(top, text="", font="Georgia 12 bold", fg="white")
    M4.pack()

    top.geometry("800x800")


top = Tk()

gui(top)

top.mainloop()
