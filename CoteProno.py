import bs4 as bs 
import urllib.request
import pickle
Liste1=[]
Liste2=[]
Liste3=[]
Liste5=[]
mot=[]
mots=[]
a=0
nbLettres=0
sauce=urllib.request.urlopen('https://paris-sportifs.pmu.fr/pari/competition/3502/basket-us/nba-matchs').read()
soup=bs.BeautifulSoup(sauce,'lxml')

for div in soup.find_all('ul',class_='row trow--odd event-list-odds-list'):
    v=div.text
    v=v.replace(",",".")
    v=v.replace("","")
    v=v.replace(" ","")
    v=v.replace("\n","")
    Liste2=[v]
    Liste5.append(Liste2)
    Liste2=[]

l=[]
e=[]
cote1=['']
cote2=['']
cote=[]
for i in range(len(Liste5)):
    for j in range(4):
        l.append(Liste5[i][0][j])
    for d in range(len(l)):
        cote2[0]=cote2[0]+l[d]
    for u in range(4,len(Liste5[i][0])):
        e.append(Liste5[i][0][u])
    for k in range(len(e)):
        cote1[0]=cote1[0]+e[k]
    cote2[0]=float(cote2[0])
    cote1[0]=float(cote1[0])
    liste89=cote2+cote1
    cote.append(liste89)
    cote1=['']
    cote2=['']
    l=[]
    e=[]
    liste89=[]
for div in soup.find_all('em',class_='trow--event--name'):
    t=div.text
    t=t.replace("//","-")
    t=t.replace("\n","")
    Liste2=[t]
    Liste1.append(Liste2)
    Liste2=[]
for i in range(len(Liste1)):
    for letters in Liste1[i]:
        for b in range(len(letters)):
            if letters[b]=='-':
                nbLettres=b
                for r in range(b):
                    mot.append(letters[r])
                for y in range(b+2,len(letters)):
                    mots.append(letters[y])
        Liste4=[nbLettres,len(letters)-nbLettres-2]
        Liste3.append(Liste4)
        Liste4=[]

while '-' in mots:
    mots.remove('-')
Att=''
Home=[]
Ext=[]
Liste4=[]
Match=[]
nb=0
for i in range(len(Liste3)):
    for a in range(Liste3[i][0]-1):
        Att=Att+mot[nb+a]
    nb+=Liste3[i][0]
    Home.append(Att)
    Att=''
nb=0
for i in range(len(Liste3)):
    for a in range(Liste3[i][1]):
        Att=Att+mots[nb+a]
    nb+=Liste3[i][1]
    Ext.append(Att)
    Att=''
for i in range(len(Home)):
    Liste4=[Home[i],Ext[i]]
    Match.append(Liste4)
    Liste4=[]
print(Match)
print(cote)
if len(input("Enregistrer? :"))>=1:
    pickle_out=open("CoteProno","wb")
    pickle.dump(Match, pickle_out)
    pickle.dump(cote, pickle_out)
    print("ok")