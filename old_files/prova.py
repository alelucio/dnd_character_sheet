
from tkinter import*

finestra=Tk()

finestra.geometry('500x300+400+200')
finestra.title('D&D CHARACTER SHEET')


strength = 13
dexterity = 16
constitution = 14
intelligence = 11
wisdom = 16
charisma = 11

def mod_strength():
    if strength >= 1 and strength < 2:
        return(1)
    elif strength >= 2 and strength < 4:
        return(2)
    elif strength >= 4 and strength < 6:
        return(3)
    elif strength >= 6 and strength < 8:
        return(3)
    elif strength >= 8 and strength < 10:
        return(-1)
    elif strength >= 10 and strength < 12:
        return(0)
    elif strength >= 12 and strength < 14:
        return(1)
    elif strength >= 14 and strength < 16:
        return(2)
    elif strength >= 16 and strength < 18:
        return(3)
    elif strength >= 18 and strength < 20:
        return(4)
    elif strength >= 20 and strength < 22:
        return(5)
    elif strength >= 22 and strength < 24:
        return(6)
    elif strength >= 24 and strength < 26:
        return(7)
    elif strength >= 26 and strength < 28:
        return(8)
    elif strength >= 28 and strength < 30:
        return(9)
    elif strength >= 30 :
        return(10)

def mod_dexterity():
    if dexterity >= 1 and dexterity < 2:
        return(1)
    elif dexterity >= 2 and dexterity < 4:
        return(2)
    elif dexterity >= 4 and dexterity < 6:
        return(3)
    elif dexterity >= 6 and dexterity < 8:
        return(3)
    elif dexterity >= 8 and dexterity < 10:
        return(-1)
    elif dexterity >= 10 and dexterity < 12:
        return(0)
    elif dexterity >= 12 and dexterity < 14:
        return(1)
    elif dexterity >= 14 and dexterity < 16:
        return(2)
    elif dexterity >= 16 and dexterity < 18:
        return(3)
    elif dexterity >= 18 and dexterity < 20:
        return(4)
    elif dexterity >= 20 and dexterity < 22:
        return(5)
    elif dexterity >= 22 and dexterity < 24:
        return(6)
    elif dexterity >= 24 and dexterity < 26:
        return(7)
    elif dexterity >= 26 and dexterity < 28:
        return(8)
    elif dexterity >= 28 and dexterity < 30:
        return(9)
    elif dexterity >= 30 :
        return(10)
    
def mod_constitution():
    if constitution >= 1 and constitution < 2:
        return(1)
    elif constitution >= 2 and constitution < 4:
        return(2)
    elif constitution >= 4 and constitution < 6:
        return(3)
    elif constitution >= 6 and constitution < 8:
        return(3)
    elif constitution >= 8 and constitution < 10:
        return(-1)
    elif constitution >= 10 and constitution < 12:
        return(0)
    elif constitution >= 12 and constitution < 14:
        return(1)
    elif constitution >= 14 and constitution < 16:
        return(2)
    elif constitution >= 16 and constitution < 18:
        return(3)
    elif constitution >= 18 and constitution < 20:
        return(4)
    elif constitution >= 20 and constitution < 22:
        return(5)
    elif constitution >= 22 and constitution < 24:
        return(6)
    elif constitution >= 24 and constitution < 26:
        return(7)
    elif constitution >= 26 and constitution < 28:
        return(8)
    elif constitution >= 28 and constitution < 30:
        return(9)
    elif constitution >= 30 :
        return(10)

def mod_intelligence():
    if intelligence >= 1 and intelligence < 2:
        return(1)
    elif intelligence >= 2 and intelligence < 4:
        return(2)
    elif intelligence >= 4 and intelligence < 6:
        return(3)
    elif intelligence >= 6 and intelligence < 8:
        return(3)
    elif intelligence >= 8 and intelligence < 10:
        return(-1)
    elif intelligence >= 10 and intelligence < 12:
        return(0)
    elif intelligence >= 12 and intelligence < 14:
        return(1)
    elif intelligence >= 14 and intelligence < 16:
        return(2)
    elif intelligence >= 16 and intelligence < 18:
        return(3)
    elif intelligence >= 18 and intelligence < 20:
        return(4)
    elif intelligence >= 20 and intelligence < 22:
        return(5)
    elif intelligence >= 22 and intelligence < 24:
        return(6)
    elif intelligence >= 24 and intelligence < 26:
        return(7)
    elif intelligence >= 26 and intelligence < 28:
        return(8)
    elif intelligence >= 28 and intelligence < 30:
        return(9)
    elif intelligence >= 30 :
        return(10)

def mod_wisdom():
    if wisdom >= 1 and wisdom < 2:
        return(1)
    elif wisdom >= 2 and wisdom < 4:
        return(2)
    elif wisdom >= 4 and wisdom < 6:
        return(3)
    elif wisdom >= 6 and wisdom < 8:
        return(3)
    elif wisdom >= 8 and wisdom < 10:
        return(-1)
    elif wisdom >= 10 and wisdom < 12:
        return(0)
    elif wisdom >= 12 and wisdom < 14:
        return(1)
    elif wisdom >= 14 and wisdom < 16:
        return(2)
    elif wisdom >= 16 and wisdom < 18:
        return(3)
    elif wisdom >= 18 and wisdom < 20:
        return(4)
    elif wisdom >= 20 and wisdom < 22:
        return(5)
    elif wisdom >= 22 and wisdom < 24:
        return(6)
    elif wisdom >= 24 and wisdom < 26:
        return(7)
    elif wisdom >= 26 and wisdom < 28:
        return(8)
    elif wisdom >= 28 and wisdom < 30:
        return(9)
    elif wisdom >= 30 :
        return(10)

def mod_charisma():
    if charisma >= 1 and charisma < 2:
        return(1)
    elif charisma >= 2 and charisma < 4:
        return(2)
    elif charisma >= 4 and charisma < 6:
        return(3)
    elif charisma >= 6 and charisma < 8:
        return(3)
    elif charisma >= 8 and charisma < 10:
        return(-1)
    elif charisma >= 10 and charisma < 12:
        return(0)
    elif charisma >= 12 and charisma < 14:
        return(1)
    elif charisma >= 14 and charisma < 16:
        return(2)
    elif charisma >= 16 and charisma < 18:
        return(3)
    elif charisma >= 18 and charisma < 20:
        return(4)
    elif charisma >= 20 and charisma < 22:
        return(5)
    elif charisma >= 22 and charisma < 24:
        return(6)
    elif charisma >= 24 and charisma < 26:
        return(7)
    elif charisma >= 26 and charisma < 28:
        return(8)
    elif charisma >= 28 and charisma < 30:
        return(9)
    elif charisma >= 30 :
        return(10)


# caselle modificatori di caratteristica
scritta_forza= Label (text='STRENGTH',fg='black',bg='ghost white',width=10).grid(row=2,column=0)
valore_forza = Label (text=strength,fg='black',bg='dark goldenrod',width=10,height=5).grid(row=1,column=0)
modificatore_forza= Label (text=mod_strength(),fg='black',bg='goldenrod',width=10).grid(row=0,column=0)


        
finestra.mainloop()
