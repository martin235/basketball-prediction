from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pickle

def make_soup(url):
    thepage=uReq(url)
    soupdata=soup(thepage,"html.parser")
    return soupdata

Match=[]
Liste0=[]
Liste2=[]
Liste3=[]
Score=[]
Liste5=[]
Liste6=[]
Liste7=[]
Liste8=[]
Months=['october','november','december','january']
v=0
url2='https://www.basketball-reference.com/leagues/NBA_2020_games-'+Months[-1]+'.html'
if input("Initialisation: ").lower()=='oui':
    for h in range(0,len(Months)-1):
        url1='https://www.basketball-reference.com/leagues/NBA_2020_games-'+Months[h]+'.html'
        print(url1)
        sou=make_soup(url1)
        container=sou.find("table",{"id":"schedule"})
        for record in container.findAll('td'):
            Score.append(record.get_text())
            #print(record.get_text())
            for data in record.findAll('a'):
                #print(data.get_text())
                Liste0.append(data.get_text())
    while '' in Score:
        Score.remove('')
    while 'OT' in Score:
        Score.remove('OT')
    while '2OT' in Score:
        Score.remove('2OT')
    while 'at Mexico City, Mexico' in Score:
        Score.remove('at Mexico City, Mexico')
    for i in range(int((len(Score)+1)/7)):
        if i==478:
            v=v-1
        v+=2
        Liste6.append(int(Score[v]))
        v+=2
        Liste7.append(int(Score[v]))
        v+=3
        Liste5.append(Liste6+Liste7)
        Liste6=[]
        Liste7=[]
    
    while 'Box Score' in Liste0:
        Liste0.remove('Box Score')
    for i in range(0,len(Liste0),2):
        Liste2.append(Liste0[i])
        Liste2.append(Liste0[i+1])
        Match.append(Liste2)
        Liste2=[]
    """pickle_out=open("Match2019-2020.pickle","wb")
    pickle.dump(Match, pickle_out)"""
Score=[]
"""pickle_in=open("Match2019-2020.pickle","rb")
Match=pickle.load(pickle_in)"""
nbMatchs=100
sou=make_soup(url2)
container=sou.find("table",{"id":"schedule"})
for record in container.findAll('td'):
    Score.append(record.get_text())
    #   print(record.get_text())
    for data in record.findAll('a'):
        #print(data.get_text())
        Liste0.append(data.get_text())
print(url2)
while '' in Score:
    Score.remove('')
while 'OT' in Score:
    Score.remove('OT')
while '2OT' in Score:
    Score.remove('2OT')
while 'at Mexico City, Mexico' in Score:
    Score.remove('at Mexico City, Mexico')
av=-1
v=0
for i in range(nbMatchs):
    if i==195:
        v=v-1
    av=0
    v+=2
    Liste6.append(int(Score[v]))
    v+=2
    Liste7.append(int(Score[v]))
    v+=3
    Liste5.append(Liste6+Liste7)
    Liste6=[]
    Liste7=[]

while 'Box Score' in Liste0:
    Liste0.remove('Box Score')
for i in range((len(Liste5)-nbMatchs)*2,len(Liste5)*2,2):
    Liste2.append(Liste0[i])
    Liste2.append(Liste0[i+1])
    Match.append(Liste2)
    Liste2=[]
for i in range(len(Liste5)*2,len(Liste0),2):
    Liste2.append(Liste0[i])
    Liste2.append(Liste0[i+1])
    Liste8.append(Liste2)
    Liste2=[]
print(Match)
print(Liste5)
print(Liste8)
pickle_out=open("scrapperCalender2019-2020.pickle","wb")
pickle.dump(Match, pickle_out)
pickle.dump(Liste5,pickle_out)
pickle.dump(Liste8,pickle_out)