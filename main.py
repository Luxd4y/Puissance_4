##----- Importation des Modules -----##
from tkinter import *
import verifie as v
import math as m
import random as r
#from PIL import ImageTk, Image
import time

tab=[[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "],\
 [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]
pos = 4
t=True
dessous="==============="
tour=1
mem_hauteur=0

def affichage(tab):
    for t in tab:
        print("|", end="")
        for pos in t:
            print(pos, end="|")
        print(" ")
    print(dessous)

def maximum(tab):
    choisis=[(-m.inf, -1)]
    for i in tab:
        if i[0]>choisis[0][0]:
            choisis=[i]
        if i[0]==choisis[0][0]:
            choisis.append(i)
    return choisis[r.randint(0, len(choisis)-1)]

def verifier(col):
  global tab
  for i in range(5, -1, -1):
    if tab[i][col]==" ":
      return (True, i)
  return (False, i)



def jouer(event, j='1'):
  global tab
  global pos
  global tour
  ver=verifier(pos-1)
  if tour==1:
      if ver[0]:
        tab[ver[1]][pos-1]=str(j)
        aff(tab)
        tour+=1
        if not v.verifie(tab):
            fen.after(100, botjouer)
        else:
            canevas.create_text(377, 437, text= "VICTOIRE !!",fill="black",font=('Helvetica 15 bold'))
        
def joueurPred(tabex, pos, j):
    tab=[[p for p in tabin] for tabin in tabex]
    for i in range(len(tab)-1, -1, -1):
        if tab[i][pos]==" ":
          tab[i][pos]=str(j%2+1)
          return tab
    return tab

def botjouer():
    j=2
    global tab
    global tour
    global pos
    global id1
    global id2
    new = []
    complet=[]
    ver2=verifier(pos-1)
    for i in range(7):
        if tab[0][i] in ["1", "2"]:
            complet.append(i)
    canevas.create_rectangle(697-95*7, 770, 32, 720,fill = '#CDCF00')
    for i in range(7):
        if i not in complet:
            canevas.create_rectangle(697-95*(6-i), 770, 32, 720,fill = '#CDCF00')
            new.append((min(joueurPred(tab, i, 1), 5), i))
            canevas.update()
    max=maximum(new)[1]
    ver=verifier(max)
    if ver[0]:
      tab[ver[1]][max]=str(j)
    tour-=1
    time.sleep(0.5)
    canevas.create_rectangle(697, 770, 32,720,fill = '#A20101')
    aff(tab)
    if ver2[0]:
      id1=canevas.create_oval(largeur_carre*0+padding+104*(pos-1), 687-102*(5-ver2[1]) ,largeur_carre*1-padding+104*(pos-1),585+padding-102*(5-ver2[1]) ,fill = '#A77B7B')
      id2=canevas.create_oval(largeur_carre*0+padding+10+104*(pos-1), 677-102*(5-ver2[1]), largeur_carre*1-padding-10+104*(pos-1), 595+padding-102*(5-ver2[1]),fill = '#FFB1B1')
    if v.verifie(tab):
        canevas.create_text(377, 437, text= "GAME OVER...",fill="black",font=('Helvetica 15 bold'))
  

def min(tabex, nb):
    c=0
    if nb==0:
        return 0
    if v.verifie(tabex):
        return 1*10**nb
    for i in range(7):
        c+=max(joueurPred(tabex, i, 2), nb-1)
    return c

def max(tabex, nb):
    c=0
    if nb==0:
        return 0
    if v.verifie(tabex):
        return -1*10**nb
    for i in range(7):
        c+=min(joueurPred(tabex, i, 1), nb-1)
    return c        


def droite(event):
    global pos
    global id1
    global id2
    if tour==1:
      if pos < 7:
          pos = pos + 1
          canevas.move(triangle,104,0)
          ver=verifier(pos-1)
          canevas.delete(id1)
          canevas.delete(id2)
          if ver[0]:
            id1=canevas.create_oval(largeur_carre*0+padding+104*(pos-1), 687-102*(5-ver[1]) ,largeur_carre*1-padding+104*(pos-1),585+padding-102*(5-ver[1]) ,fill = '#A77B7B')
            id2=canevas.create_oval(largeur_carre*0+padding+10+104*(pos-1), 677-102*(5-ver[1]), largeur_carre*1-padding-10+104*(pos-1), 595+padding-102*(5-ver[1]),fill = '#FFB1B1')
          else:
            id1=canevas.create_oval(1000, 1000, 1000, 1000, fill='red')
        
   
def gauche(event):
    global pos
    global id1
    global id2
    if tour==1:
      if pos > 1:
          pos = pos - 1
          canevas.move(triangle,-104,0)
          ver=verifier(pos-1)
          canevas.delete(id1)
          canevas.delete(id2)
          if ver[0]:
            id1=canevas.create_oval(largeur_carre*0+padding+104*(pos-1), 687-102*(5-ver[1]) ,largeur_carre*1-padding+104*(pos-1),585+padding-102*(5-ver[1]) ,fill = '#A77B7B')
            id2=canevas.create_oval(largeur_carre*0+padding+10+104*(pos-1), 677-102*(5-ver[1]), largeur_carre*1-padding-10+104*(pos-1), 595+padding-102*(5-ver[1]),fill = '#FFB1B1')
          else:
            id1=canevas.create_oval(1000, 1000, 1000, 1000, fill='red')
 
        
    


##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Puissance 4')


##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 1, column = 1, padx = 3, pady = 3, sticky=E)

##----- Création du canevas -----##
canevas = Canvas(fen, width = 730, height = 800, bg = '#000d8F')
canevas.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady =3)

padding = 2

largeur_carre = int((canevas.winfo_reqwidth())/7)

##----- canevaser dans le canevas -----##
def aff(tab):
    n = 75
    m = -27
    for i in range(len(tab)):
        n= n + 102
        m = m + 102
        for j in range(len(tab[i])):
            if tab[i][j] == ' ':
                canevas.create_oval(largeur_carre*j+padding, n ,largeur_carre*(j+1)-padding,m+padding ,fill = '#D7F2FF')
            if tab[i][j] == '1':
                canevas.create_oval(largeur_carre*j+padding, n ,largeur_carre*(j+1)-padding,m+padding ,fill = '#A20101')
                canevas.create_oval(largeur_carre*j+padding+10, n-10,largeur_carre*(j+1)-padding-10,m+padding+10 ,fill = '#FF0000')
            if tab[i][j] == '2':
                canevas.create_oval(largeur_carre*j+padding, n ,largeur_carre*(j+1)-padding,m+padding , fill = '#CDCF00')
                canevas.create_oval(largeur_carre*j+padding+10, n-10,largeur_carre*(j+1)-padding-10,m+padding+10, fill = '#fcff00')
    canevas.update()

canevas.create_rectangle(0,0,755,75,fill = '#D7F2FF')
canevas.create_rectangle(697, 770, 32,720,fill = '#A20101')
points = [365,60, 390, 10, 340, 10]
triangle = canevas.create_polygon(points, outline='#000000',fill='#FF0000', width=2)
aff(tab)
id1=canevas.create_oval(largeur_carre*3+padding, 687 ,largeur_carre*4-padding,585+padding ,fill = '#A77B7B')
id2=canevas.create_oval(largeur_carre*3+padding+10, 677, largeur_carre*4-padding-10, 595+padding,fill = '#FFB1B1')
canevas.bind_all('<Right>', droite)
canevas.bind_all('<Left>', gauche)
canevas.bind_all('<Down>', jouer)


##----- Programme principal -----##

fen.mainloop()             