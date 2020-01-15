import pickle
pickle_in=open("PronoMatch","rb")
Liste1=pickle.load(pickle_in)
Liste8=pickle.load(pickle_in)
Liste9=pickle.load(pickle_in)
Liste10=pickle.load(pickle_in)
argent=pickle.load(pickle_in)
MAJ=pickle.load(pickle_in)
pickle_in=open("CoteProno","rb")
Liste2=pickle.load(pickle_in)
Liste3=pickle.load(pickle_in)
pickle_in=open("Update.pickle","rb")
L=pickle.load(pickle_in)
ListeUpdate=pickle.load(pickle_in)
pickle_in=open("Bonus.pickle","rb")
bonus=pickle.load(pickle_in)
pickle_in=open("PariMoi.pickle","rb")
MonPari=pickle.load(pickle_in)
Pari5=pickle.load(pickle_in)
print(MonPari)
Liste4=[]
Liste7=[]
Pari=[]
Cote2=[]
Cote=[]
Cote3=[]
Cote4=[]
cote=1
print(Liste1)
print(Liste8)
print(ListeUpdate)
print(Liste3)
ListeC=[len(Liste2)]
ListeC.append(Liste2)
if ListeC[1]==ListeUpdate[1]:
    New=False
    print("Pas Nouveau")
    Q=input("Il y a déjà un pari pour aujourd'hui, voulez-vous recommencer?: ")
    Q.lower()
    if Q=="oui":
        Nouveau=True
    else:
        Nouveau=False
else:
    Nouveau=True
    New=True
    print("Nouveau")
if New==True:
    for i in range(len(argent)):
        argent[i]=float(argent[i])
        if argent[i]>=10:
            bonus[i]=round(bonus[i]+(argent[i]-5),2)
            argent[i]=5
        elif argent[i]==0:
            bonus[i]=round(bonus[i]-5,2)
            argent[i]=5
        else:
            pass
else:
    for i in range(len(argent)):
        print(argent[i])
        argent[i]=float(argent[i])
        if argent[i]>=10:
            argent[i]=5
        elif argent[i]==0:
            argent[i]=5
print(argent)
print(bonus)
def mise(Liste):
    cote=1
    Liste4=[]
    ListeA=[]
    for i in range(len(Liste)):
        for c in range(len(Liste2)):
            for v in range(2):
                if Liste[i]==Liste2[c][v]:
                    print(Liste2[c])
                    print(Liste2[c][v])
                    print(Liste3[c][v])
                    Liste4.append(Liste3[c][v])
                    ListeAB=[Liste2[c],Liste[i]]
                    ListeA.append(ListeAB)
                    ListeAB=[]
    for i in range(len(Liste4)):
        cote=cote*Liste4[i]
        cote=round(cote,2)
    print("La cote combiné est de:",cote)
    cote=[cote]
    #ListeC=[len(Liste2)]
    ListeC=cote+ListeA
    #ListeC.append(ListeG)
    return ListeC

def pari(Liste,ListeB,nbListe):
    mise=float(argent[nbListe])
    print("Vous avez:",mise,"euros")
    print("Cela pourrait vous rapporterez:",round(mise*Liste[0][0],2))
    Question=input("Etes vous surs de parier: ")
    Question=Question.lower()
    Liste5=[]
    if Question=='oui':
        print(round(mise*Liste[0][0],2))
        Liste5=[str(mise),str(Liste[0][0]),str(round(mise*Liste[0][0],2))]
        for i in range(len(ListeB)):
            Liste5.append(ListeB[i])
            for c in range(len(Liste2)):
                for v in range(2):
                    if ListeB[i]==Liste2[c][v]:
                        Liste5.append(Liste2[c][0])
                        Liste5.append(Liste2[c][1])
    else:
        print(Liste5)
    return Liste5
def read():
    l=[]
    fichier=open("prono.txt","r")
    l=fichier.readlines()
    print(len(l))
    print(l)
    return l
def save(Liste):
    fichier=open("prono.txt","w")
    for i in range(len(Liste)):
        for b in range(len(Liste[i])):
            fichier.write(Liste[i][b]+"\n")
        fichier.write("\n")
    fichier.close()
if Nouveau==True:
    Cote.append(mise(Liste1))
    pari1=pari(Cote,Liste1,0)
    print(pari1)
    Cote2.append(mise(Liste8))
    pari2=pari(Cote2,Liste8,1)
    print(pari2)
    Cote3.append(mise(Liste9))
    pari3=pari(Cote3,Liste9,2)
    print(pari3)
    Cote4.append(mise(Liste10))
    pari4=pari(Cote4,Liste10,3)
    print(pari4)
    ListePari=[pari1,pari2,pari3,pari4,Pari5]
    save(ListePari)
    ListeComparaison=[]
    if len(pari1)!=0 and len(pari2)!=0 and len(pari3)!=0 and len(pari4)!=0:
        ListeComparaison=[len(Liste2),[Liste1,pari1[0],pari1[2]],[Liste8,pari2[0],pari2[2]],[Liste9,pari3[0],pari3[2]],[Liste10,pari4[0],pari4[2]],MonPari]
        print(ListeComparaison)
        if New==False:
            del L[-1]
        else:
            del L[0]
        L.append(ListeComparaison)
        print(L)
        pickle_out=open("Update.pickle","wb")
        pickle.dump(L,pickle_out)
        pickle.dump(ListeC,pickle_out)
if New==True:
    pickle_out=open("Bonus.pickle","wb")
    pickle.dump(bonus,pickle_out)
print(bonus)
    