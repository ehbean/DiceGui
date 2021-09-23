import random
from tkinter import *

# Delete all spinbox content, and sets all to 0
def Reset():
    d100_ModSpinbox.delete(0, END)
    d20_ModSpinbox.delete(0, END)
    d12_ModSpinbox.delete(0, END)
    d10_ModSpinbox.delete(0, END)
    d8_ModSpinbox.delete(0, END)
    d6_ModSpinbox.delete(0, END)
    d4_ModSpinbox.delete(0, END)

    d100_QuanSpinbox.delete(0, END)
    d20_QuanSpinbox.delete(0, END)
    d12_QuanSpinbox.delete(0, END)
    d10_QuanSpinbox.delete(0, END)
    d8_QuanSpinbox.delete(0, END)
    d6_QuanSpinbox.delete(0, END)
    d4_QuanSpinbox.delete(0, END)

    d100_ModSpinbox.insert(0, '0')
    d20_ModSpinbox.insert(0, '0')
    d12_ModSpinbox.insert(0, '0')
    d10_ModSpinbox.insert(0, '0')
    d8_ModSpinbox.insert(0, '0')
    d6_ModSpinbox.insert(0, '0')
    d4_ModSpinbox.insert(0, '0')

    d100_QuanSpinbox.insert(0, '0')
    d20_QuanSpinbox.insert(0, '0')
    d12_QuanSpinbox.insert(0, '0')
    d10_QuanSpinbox.insert(0, '0')
    d8_QuanSpinbox.insert(0, '0')
    d6_QuanSpinbox.insert(0, '0')
    d4_QuanSpinbox.insert(0, '0')

# Gets the value of all spinboxes and stores them as ints.
def RollGUI():
    random.seed()
    global total
    total = 0
    dieA = 0

    d100_Quan = int(d100_QuanSpinbox.get())
    d20_Quan = int(d20_QuanSpinbox.get())
    d12_Quan = int(d12_QuanSpinbox.get())
    d10_Quan = int(d10_QuanSpinbox.get())
    d8_Quan = int(d8_QuanSpinbox.get())
    d6_Quan = int(d6_QuanSpinbox.get())
    d4_Quan = int(d4_QuanSpinbox.get())

    d100_Mod = int(d100_ModSpinbox.get())
    d20_Mod = int(d20_ModSpinbox.get())
    d12_Mod = int(d12_ModSpinbox.get())
    d10_Mod = int(d10_ModSpinbox.get())
    d8_Mod = int(d8_ModSpinbox.get())
    d6_Mod = int(d6_ModSpinbox.get())
    d4_Mod = int(d4_ModSpinbox.get())

    while d100_Quan > 0:
        dieA = (random.randrange(1, 101) + d100_Mod)
        total = total + dieA
        d100_Quan = d100_Quan - 1
    while d20_Quan > 0:
        dieA = (random.randrange(1, 21) + d20_Mod)
        total = total + dieA
        d20_Quan = d20_Quan - 1
    while d12_Quan > 0:
        dieA = (random.randrange(1, 13) + d12_Mod)
        total = total + dieA
        d12_Quan = d12_Quan - 1
    while d10_Quan > 0:
        dieA = (random.randrange(1, 11) + d10_Mod)
        total = total + dieA
        d10_Quan = d10_Quan - 1
    while d8_Quan > 0:
        dieA = (random.randrange(1, 9) + d8_Mod)
        total = total + dieA
        d8_Quan = d8_Quan - 1
    while d6_Quan > 0:
        dieA = (random.randrange(1, 7) + d6_Mod)
        total = total + dieA
        d6_Quan = d6_Quan - 1
    while d4_Quan > 0:
        dieA = (random.randrange(1, 5) + d4_Mod)
        total = total + dieA
        d4_Quan = d4_Quan - 1
    ListDisplay()

def ListDisplay():
    histSize = int(DiceHistory.size())
    if histSize != 10:
        DiceHistory.insert(0, total)
    else:
        DiceHistory.delete(9)
        DiceHistory.insert(0, total)

root = Tk()
root.geometry("350x220")
root.title('GUIDice')

# Creating/Decalring all widgets
DiceHistory = Listbox(root)

RollButton = Button(root, text="Roll!", width=7, command=RollGUI)
ResetButton = Button(root, text="Reset.", width=7, command=Reset)

quanLabel = Label(root, text="Quantity", anchor=E, justify=LEFT)
modLabel = Label(root, text="Modifier", justify=LEFT)

d100Label = Label(root, text="d100")
d20Label = Label(root, text="d20")
d12Label = Label(root, text="d12")
d10Label = Label(root, text="d10")
d8Label = Label(root, text="d8")
d6Label = Label(root, text="d6")
d4Label = Label(root, text="d4")

d100_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)
d20_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)
d12_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)
d10_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)
d8_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)
d6_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)
d4_QuanSpinbox = Spinbox(root, width=10, from_=0, to=99999)

d100_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)
d20_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)
d12_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)
d10_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)
d8_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)
d6_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)
d4_ModSpinbox = Spinbox(root, width=10, from_=-999999, to=99999)

# Clears the Modifier Spinboxes, then sets all to 0
d100_ModSpinbox.delete(0, END)
d20_ModSpinbox.delete(0, END)
d12_ModSpinbox.delete(0, END)
d10_ModSpinbox.delete(0, END)
d8_ModSpinbox.delete(0, END)
d6_ModSpinbox.delete(0, END)
d4_ModSpinbox.delete(0, END)
d100_ModSpinbox.insert(0, 0)
d20_ModSpinbox.insert(0, 0)
d12_ModSpinbox.insert(0, 0)
d10_ModSpinbox.insert(0, 0)
d8_ModSpinbox.insert(0, 0)
d6_ModSpinbox.insert(0, 0)
d4_ModSpinbox.insert(0, 0)

# Grid Placements for widgets
DiceHistory.grid(row=1, rowspan=10, column=1, columnspan=2, padx=5, pady=5)

RollButton.grid(row=11, column=1, pady=5)
ResetButton.grid(row=11, column=2, pady=5)

d100_QuanSpinbox.grid(row=3, column=3)
d20_QuanSpinbox.grid(row=4, column=3)
d12_QuanSpinbox.grid(row=5, column=3)
d10_QuanSpinbox.grid(row=6, column=3)
d8_QuanSpinbox.grid(row=7, column=3)
d6_QuanSpinbox.grid(row=8, column=3)
d4_QuanSpinbox.grid(row=9, column=3)

d100Label.grid(row=3, column=4)
d20Label.grid(row=4, column=4)
d12Label.grid(row=5, column=4)
d10Label.grid(row=6, column=4)
d8Label.grid(row=7, column=4)
d6Label.grid(row=8, column=4)
d4Label.grid(row=9, column=4)

d100_ModSpinbox.grid(row=3, column=5)
d20_ModSpinbox.grid(row=4, column=5)
d12_ModSpinbox.grid(row=5, column=5)
d10_ModSpinbox.grid(row=6, column=5)
d8_ModSpinbox.grid(row=7, column=5)
d6_ModSpinbox.grid(row=8, column=5)
d4_ModSpinbox.grid(row=9, column=5)

quanLabel.grid(row=1, column=3, pady=5)
modLabel.grid(row=1, column=5, pady=5)

root.columnconfigure(3, minsize=30)
root.columnconfigure(5, minsize=30)

root.mainloop()