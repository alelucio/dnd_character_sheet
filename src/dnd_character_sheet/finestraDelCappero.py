from tkinter import *

from dnd_character_sheet.sheets.Abilities import Abilities

finestra = Tk()

finestra.geometry('500x300+400+200')
finestra.title('D&D CHARACTER SHEET')

abilities = Abilities()

abilities.strength = 13
abilities.dexterity = 16
abilities.constitution = 14
abilities.intelligence = 11
abilities.wisdom = 16
abilities.charisma = 11

# caselle modificatori di caratteristica
scritta_forza = Label(text='STRENGTH', fg='black', bg='ghost white', width=10).grid(row=2, column=0)
valore_forza = Label(text=abilities.strength, fg='black', bg='dark goldenrod', width=10, height=5).grid(row=1, column=0)
modificatore_forza = Label(text=abilities.getModifierStrength(), fg='black', bg='goldenrod', width=10).grid(row=0, column=0)

finestra.mainloop()
