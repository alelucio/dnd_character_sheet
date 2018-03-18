from tkinter import*

finestra=Tk()

finestra.geometry('1000x300+400+200')
finestra.title('D&D CHARACTER SHEET')

lista_classi = ['BARBARIAN', 'BARD','CLERIC','DRUID','FIGHTER','MONK','PALADIN','RANGER','ROGUE','SORCER','WARLOCK','WIZARD']

selezionaClasse = StringVar()
selezionaClasse.set(lista_classi[0])

# canvas nome personaggio
nome_personaggio = Label(text='HIMO',fg='white',bg='gray43',width=10,height=1,font = 'Helvetica 50 bold').grid(row=0,column=0,sticky=N)
etichetta_nomePersonaggio = Label (text='CHARACTER NAME' ,fg='gray34',bg='DarkGoldenrod1',width=31,height=1).grid(row=0,column=0,sticky=S)

bo= Label(bg='orange',width=120,height=5).grid(row=0,column=1)

classiMenu= OptionMenu(finestra,selezionaClasse,*lista_classi).grid(row=0,column=1,sticky=W)

finestra.mainloop()
