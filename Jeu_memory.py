# Créé par otmanbenbouziane, le 27/03/2023 en Python 3.7
from tkinter import *
from random import*
root=Tk()
root.title("jeu de memory")

dos_de_carte=PhotoImage(file="images/dosdecart.png")
c=0
Jeu=12

#dimensions et variables utilisés dans les fonctions

écart=5
Lignes=2
Colonnes=6

DimensionCarteLongueur=150
DimensionCarteLargeur=250


côté=DimensionCarteLongueur+écart
côté2=DimensionCarteLargeur+écart

Longueur=Colonnes*côté
Largeur=Lignes*côté2




Abcisse=côté/2
Ordonné=côté2/2
C=(Lignes*Colonnes)//2
print(C)

#Variable aléatoire pour renforcer la difficulté du jeu

vie=randint(4,10)

#Aire de jeu sur lequel va reposer les 12 cartes

Aire=Canvas(root, width=Longueur, height=Largeur, bg='brown')
Aire.grid(column=0,row=3)

#Label score et titre

Titre= Label(root, text="JEU DE MEMORY",font=("Brush Script MT",30), bg="#FF7F50")
Titre.grid(column=0,row=0)

CompteurDeVie= Label(root, text="Vies : "+str(vie),font=("Brush Script MT", 20), bg='#f54c2a')
CompteurDeVie.grid(column=9,row=2)

#Listes des noms et conversion en format compréhensible pour python

Nom=['trefles','coeurs','carreaux','piques','asdepiques','jokers']
trefle=PhotoImage(file="images/trefles.png")
coeur=PhotoImage(file="images/coeurs.png")
carreau=PhotoImage(file="images/carreaux.png")
pique=PhotoImage(file="images/piques.png")
asdepiques=PhotoImage(file="images/asdepiques.png")
jokers=PhotoImage(file="images/jokers.png")
z=[trefle,coeur,carreau,pique,asdepiques,jokers]

#Canvas "écran" de victoire ou défaite

g=Canvas(root, width=Longueur/2, height=Largeur/2,bg='white')

#Image présent sur le canvas "g"

gagné=PhotoImage(file="images/gagne.png")
perdu=PhotoImage(file="images/perdu.png")





#fonction qui mélange une liste de 12 éléments de 0 à 5 en une matrice de deux éléments

def melanger():
    cartes=list(range(C))*2
    shuffle(cartes)
    print(cartes)
    P=[]
    k=0
    for ligne in range(Lignes):
        M=[]
        for col in range(Colonnes):

            M.append(cartes[k])
            k+=1
        P.append(M)
    print(P)
    return P

Set=melanger()
w=[]


#création de la grille

for lig in range(Lignes):
    L=[]
    for col in range(Colonnes):
        centre=(col*côté+Abcisse , lig*côté2+Ordonné)
        n=Set[lig][col]
        s=z[n]
        Aire.create_image(centre, image=s)
        v=Aire.create_image(centre, image=dos_de_carte)
        L.append(v)
    w.append(L)


#liste qui représente les deux cliques consécutifs du joueur

e=[None,None]



#fonction qui permet le retournement d'une carte au clique

def clique(event):
    if e[1] is not None:
        return
    X,Y=(event.x,event.y)
    col=X//côté
    lig=Y//côté2
    if Set[lig][col]!=-1:
        traiter(lig,col)

#fonction qui traite les cliques pour déterminer quand retourner en mettant à jour la liste e
#et affichage des images "gagné" et "perdu"

def traiter(lig,col):
    global vie,c
    item=w[lig][col]
    Aire.delete(item)
    if e[0] is None:
        e[0]=(lig,col)
    else:
        if e[0]==(lig,col):
            return
        e[1]=(lig,col)
        i,j=e[0]
        if Set[i][j]==Set[lig][col]:
            Set[i][j]=Set[lig][col]=-1
            e[0]=e[1]=None
            c=c+1
            print(c)
            if c==6:
                CompteurDeVie.config(text="Gagné!!! :)")
                g.create_image(Longueur//4,Largeur//4,image=gagné)
                g.grid(column=0,row=3)



        else:

        #animation toutes les 400 ms qui dépend de 'masquer'

            Aire.after(400,masquer,i,j,lig,col)
            vie=vie-1
            CompteurDeVie.config(text="Vies: "+str(vie))
            if vie==0 or vie<0 :
                CompteurDeVie.config(text="Perdu!!! :(")
                g.create_image(Longueur//4,Largeur//4,image=perdu)
                g.grid(column=0,row=3)
                devoiler(i,j,lig,col)





#fonction qui retourne les cartes non similaires

def masquer(i,j,lig,col):
    centre=(Abcisse+j*côté, Ordonné+i*côté2)
    w[i][j]=Aire.create_image(centre, image=dos_de_carte)
    centre=(Abcisse+col*côté , Ordonné+lig*côté2)
    w[lig][col]=Aire.create_image(centre, image=dos_de_carte)
    e[0]=e[1]=None

#fonction qui transforme les cartes en 'joker' après la défaite du joueur

def devoiler(i,j,lig,col):
    centre=(Abcisse+j*côté, Ordonné+i*côté2)
    w[i][j]=Aire.create_image(centre, image=jokers)
    centre=(Abcisse+col*côté , Ordonné+lig*côté2)
    w[lig][col]=Aire.create_image(centre, image=jokers)
    e[0]=e[1]=None











#le canva Aire est associé à un type d'évènement et à une fonction à effectuer

Aire.bind("<Button>",clique)







root.mainloop()
