from tkinter import*
from random import*
import pickle
pickle_in=open("CoteProno","rb")
Matchs=pickle.load(pickle_in)
Cote=pickle.load(pickle_in)

buttons=[]
ListeVar=[]
ListeEquipe=[]
fen=Tk()


def onPress1(i):
    state=i
    buttons[state][1].deselect()
def onPress2(i):
    state=i
    buttons[state][0].deselect()
    
def Change():
    nombre=['1','2','3','4','5','6','7','8','9','0','.']
    global ListeAA
    global ListeBB
    ListeA=[]
    ListeAA=[]
    ListeBB=[]
    CoteTotal=1
    texte=E.get()
    Boo=False
    bo=0
    for r in range(len(texte)):
        for p in range(len(nombre)):
            if texte[r]==nombre[p]:
                bo+=1
                print(texte[r])
    if bo==len(texte) and bo!=0:
        Boo=True
    else:
        Boo=False
        
    if Boo==False:
        pass
    else:
        E.destroy()
        L.destroy()
        away.destroy()
        home.destroy()
        for t in range(len(ListeEquipe)):
            for g in range(len(ListeEquipe[t])):
                ListeEquipe[t][g].destroy()
        for c in range(len(buttons)):
            for v in range(len(buttons[c])):
                buttons[c][v].destroy()
        for a in range(len(ListeVar)):
            for i in range(len(ListeVar[a])):
                val=ListeVar[a][i].get()
                if val==1:
                    ListeA.append(Matchs[a][i])
                    CoteTotal=CoteTotal*Cote[a][i]
        
        B.destroy()
        Tex=Label(fen,text="Votre pari a bien été enregistré!",fg="red")
        Tex.place(x=150,y=150)
        CoteTotal=round(CoteTotal,2)
        print(CoteTotal)
        texte=float(texte)
        Pari=round(texte*CoteTotal,2)
        print(Pari)
        ListeAA.append(ListeA)
        ListeAA.append(str(texte))
        ListeAA.append(str(Pari))
        ListeBB.append(str(texte))
        ListeBB.append(str(CoteTotal))
        ListeBB.append(str(Pari))
        for i in range(len(ListeA)):
            ListeBB.append(ListeA[i])
        print(ListeAA)
        print(ListeBB)
    
longF=str(len(Matchs)*50+150)
longueurBouton=12
hauteurBouton=3
fen.title("Ma fenetre")
fen.geometry("500x"+longF+"+300+300")
fen.resizable(width=False,height=False)
fen.update_idletasks()
B=Button(fen,text="PARIER",width=longueurBouton,height=hauteurBouton,fg="red",bg="yellow",font="arial",command= Change)
B.place(x=180,y=50*len(Matchs)+50)
L=Label(fen,text="Mise:")
home=Label(fen,text="Domicile",fg="green")
away=Label(fen,text="Exterieur",fg="red")
home.place(x=80,y=25)
away.place(x=310,y=25)
for i in range(len(Matchs)):
    z=str(i)
    nom="var"+z
    nom2="variable"+z
    nom=IntVar()
    nom2=IntVar()
    n=Matchs[i][0]
    n1=Matchs[i][1]
    M=Label(fen,text=Matchs[i][0])
    P=Label(fen,text=Matchs[i][1])
    C=Label(fen,text=Cote[i][0])
    C2=Label(fen,text=Cote[i][1])
    n=Checkbutton(fen,onvalue=1,offvalue=0,variable=nom,command=(lambda i=i : onPress1(i)))
    n1=Checkbutton(fen,onvalue=1,offvalue=0,variable=nom2,command=(lambda i=i : onPress2(i)))
    n.place(x=200,y=50+50*i)
    n1.place(x=430,y=50+50*i)
    C.place(x=20,y=70+50*i)
    C2.place(x=250,y=70+50*i)
    M.place(x=20,y=50+50*i)
    P.place(x=250,y=50+50*i)
    Liste2=[n,n1]
    Liste3=[nom,nom2]
    Liste4=[M,P,C,C2]
    ListeEquipe.append(Liste4)
    ListeVar.append(Liste3)
    buttons.append(Liste2)
E=Entry(fen)
L.place(x=150,y=0)
E.place(x=200,y=0)

print(E.get())
fen.mainloop()
pickle_out=open("PariMoi.pickle","wb")
pickle.dump(ListeAA,pickle_out)
pickle.dump(ListeBB,pickle_out)