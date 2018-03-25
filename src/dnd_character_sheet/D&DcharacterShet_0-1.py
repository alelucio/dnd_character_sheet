from tkinter import*

finestra=Tk()

finestra.geometry('1000x300+400+200')
finestra.title('D&D CHARACTER SHEET')
#classi
lista_classi = ['BARBARIAN', 'BARD','CLERIC','DRUID','FIGHTER','MONK','PALADIN','RANGER','ROGUE','SORCER','WARLOCK','WIZARD']

selezionaClasse = StringVar()
selezionaClasse.set(lista_classi[0])
#razze
lista_razze =['DWARF', 'ELF','HALFLING','HUMAN','DRAGONBORN','GNOME','HALF ELF','HALF ORC','TIEFLING']

selezionaRazza = StringVar()
selezionaRazza.set(lista_razze[0])

#allineamento
lista_allineamenti = ['LEGALE BUONO','NEUTRALE BUONO','CAOTICO BUONO', 'NEUTRALE BUONO','NEUTRALE','CAOTICO NEUTRALE', 'LEGALE MALVAGIO,', 'NEUTRALE MALVAGIO','CAOTICO MALVAGIO']

selezionaAllineamento= StringVar()
selezionaAllineamento.set(lista_allineamenti[0])

# canvas nome personaggio
nome_personaggio = Label(text='HIMO',fg='white',bg='gray43',width=10,height=1,font = 'Helvetica 50 bold').grid(row=0,column=0,sticky=N)
etichetta_nomePersonaggio = Label (text='CHARACTER NAME' ,fg='gray34',bg='DarkGoldenrod1',width=31,height=1).grid(row=1,column=0,sticky=S)


# canvans livello, classe, nome giocatore, razza , allineamento e esperienza
#bo= Label(bg='orange',width=120,height=5).grid(row=0,column=1)

livello = Label ( text='LEVEL = ', fg='black', width=20).grid(row=0,column=1)# numero livello

classiMenu= OptionMenu(finestra,selezionaClasse,*lista_classi)# elenco classi
classiMenu.grid(row=0,column=2)
classiMenu.config(bg="ORANGE")

nome_giocatore = Label (text ='player name : LUCIO', fg='black', bg='orange',width=20).grid(row=0,column=3)#nome giocatore

razzeMenu= OptionMenu(finestra,selezionaRazza,*lista_razze)# elenco razze
razzeMenu.grid(row=1,column=1)
razzeMenu.config(bg='orange')

allineamentiMenu = OptionMenu(finestra,selezionaAllineamento,*lista_allineamenti)# elenco allineamenti
allineamentiMenu.grid(row=1,column=2)
allineamentiMenu.config(bg='orange')

finestra.mainloop()
