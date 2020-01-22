import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from math import*

import pickle
pickle_in=open("scrapperCalender2019-2020.pickle","rb")
Liste1=pickle.load(pickle_in)
Liste3=pickle.load(pickle_in)
Liste4=pickle.load(pickle_in)
pickle_inn=open("Stat2019-2020.pickle","rb")
Liste2=pickle.load(pickle_inn)
pickle_iinn=open("Update.pickle","rb")
ListeComparaison=pickle.load(pickle_iinn)
ListeUpdate=pickle.load(pickle_iinn)
Liste5=[]
Liste12=[]
points=[]
Points=[]
ListeProno=[]
ListeAComparer=[]
ListePronoExt=[]
PronoMatch=[]
ListeNeural=[]
ListeTarget=[]
summAtt=0
summDef=0
maxa=0
maxi=0
nb0=0
nbAtt=0
nbDef=0
nb1=0
nb2=0
nb3=0
nb4=0
nbMatchs=int(input("Nombre de matchs: "))
nbMJoués=int(input("Nombre de matchs déjà joués: "))
for i in range(30):
    Liste9=[0,0,0,0,0,0,0,0]
    Liste2[i].append(Liste9)
print(Liste2[0][2][4])
for i in range(len(Liste3)):
    if Liste3[i][1]>Liste3[i][0]:
        Liste5.append(0)
        ListeTarget.append(1)
        ListeAComparer.append(Liste1[i][1])
        nb0+=1
    else:
        ListeAComparer.append(Liste1[i][0])
        ListeTarget.append(0)
        Liste5.append(1)
        nb3+=1
for i in range(len(Liste3)):
    if Liste3[i][1]<Liste3[i][0]:
        Liste12.append(0)
    else:
        Liste12.append(1)

def argent(Liste,Liste2,q):
    nm=Liste[-q][0]
    gagnant=0
    arg=[]
    for b in range(len(Liste[-q])-1,0,-1):
        for c in range(len(Liste[-q][-1*b][0])):
            for i in range(1,nm+1):
                if Liste2[-1*i]==Liste[-q][-1*b][0][c]:
                    print(Liste2[-1*i])
                    print("ok")
                    gagnant+=1
        if gagnant==len(Liste[-q][-1*b][0]):
            print(Liste[-q][-1*b][2])
            arg.append(Liste[-q][-1*b][2])
        else:
            print("0")
            arg.append(0)
        gagnant=0
    return(arg)
if ListeUpdate[0]==nbMatchs:
    var1=2
else:
    var1=1
par=argent(ListeComparaison,ListeAComparer,var1)
print(par)
print(len(Liste5))
print(nb0/len(Liste5))

def sigmoid(x):
    return 1/(1+np.exp(-x))
def cost(b,c):
    return (b-c)**2
def slope(b,c):
    return 2*(b-c)
def NNDeep(m1,m2,m3,w1,w2,w3):
    z=(m1*w1+m2*w2+m3*w3)
    return sigmoid(z)
def NN(m1,m2,m3,w1,w2,w3,b):
    z=(m1*w1+m2*w2+m3*w3+b)
    return sigmoid(z)
def sigmoid_p(x):
    return sigmoid(x)*(1-sigmoid(x))


defvic=0
for z in range(len(Liste5)):
    for i in range(30):
        if Liste2[i][0]==Liste1[z][0]:
            b=Liste2[i][0]
            f=Liste2[i][1][0]
            g=Liste2[i][1][1]
            k=float(Liste2[i][1][2])
            deff=float(Liste2[i][1][4])
            w=float(Liste2[i][1][3])
            for g in range(2,len(Liste2[i])):
                summAtt+=Liste2[i][g][5]
                summDef+=Liste2[i][g][6]
            Liste10=[Liste5[z],Liste12[z],Liste3[z][0],Liste3[z][1]]
            if Liste10[2]>Liste10[3] and Liste2[i][-1][-1]>=0:
                defvic=Liste2[i][-1][-1]+1
            elif Liste10[2]<Liste10[3] and Liste2[i][-1][-1]<=0:
                defvic=Liste2[i][-1][-1]-1
            elif Liste10[2]>Liste10[3] and Liste2[i][-1][-1]<0:
                defvic=1
            else:
                defvic=-1
            Liste11=[Liste2[i][-1][0]+Liste10[0],Liste2[i][-1][1]+Liste10[1],round((Liste2[i][-1][0]+Liste10[0])/(len(Liste2[i])-2),3),round((summAtt+Liste10[2])/(len(Liste2[i])-2),3),round((summDef+Liste10[3])/(len(Liste2[i])-2),3),Liste10[2],Liste10[3],defvic]
            Liste2[i].append(Liste11)
            summAtt=0
            summDef=0
            Liste10=[]
            Liste11=[]
            maxi=i
    for a in range(30):
        if Liste2[a][0]==Liste1[z][1]:
            c=Liste2[a][0]
            d=Liste2[a][1][0]
            e=Liste2[a][1][1]
            m=float(Liste2[a][1][2])
            deffe=float(Liste2[a][1][4])
            x=float(Liste2[a][1][3])
            for g in range(2,len(Liste2[a])):
                summAtt+=Liste2[a][g][5]
                summDef+=Liste2[a][g][6]
            Liste10=[Liste12[z],Liste5[z],Liste3[z][1],Liste3[z][0]]
            if Liste10[2]>Liste10[3] and Liste2[a][-1][-1]>=0 :
                defvic=Liste2[a][-1][-1]+1
            elif Liste10[2]<Liste10[3] and Liste2[a][-1][-1]<=0:
                defvic=Liste2[a][-1][-1]-1
            elif Liste10[2]>Liste10[3] and Liste2[a][-1][-1]<0:
                defvic=1
            else:
                defvic=-1
            Liste11=[Liste2[a][-1][0]+Liste10[0],Liste2[a][-1][1]+Liste10[1],round((Liste2[a][-1][0]+Liste10[0])/(len(Liste2[a])-2),3),round((summAtt+Liste10[2])/(len(Liste2[a])-2),3),round((summDef+Liste10[3])/(len(Liste2[a])-2),3),Liste10[2],Liste10[3],defvic]
            Liste2[a].append(Liste11)
            summDef=0
            summAtt=0
            Liste10=[]
            Liste11=[]
            maxa=a
    color="r"
    ecart=0.1
    nbMJ=9
    if z>nbMJoués:
        if (Liste2[maxa][-2][2]-Liste2[maxi][-2][2]>0 and Liste2[maxa][-2][2]-Liste2[maxi][-2][2]<0.5)  and ((Liste2[maxa][-2][3]-Liste2[maxa][-2][4])-(Liste2[maxi][-2][3]-Liste2[maxi][-2][4])>5 and (Liste2[maxa][-2][3]-Liste2[maxa][-2][4])-(Liste2[maxi][-2][3]-Liste2[maxi][-2][4])<50):
            
            ListeProno.append(0)
            ListeProno.append(z)
            ListeProno.append(Liste1[z][1])
            ListeProno.append(Liste2[maxa][-2][2]-Liste2[maxi][-2][2])
            ListeProno.append((Liste2[maxa][-2][3]-Liste2[maxa][-2][4])-(Liste2[maxi][-2][3]-Liste2[maxi][-2][4]))
            ListeProno.append(Liste2[maxa][-2][-1])
    if z>nbMJoués:
        if (Liste2[maxi][-2][2]-Liste2[maxa][-2][2]>0.32 and Liste2[maxi][-2][2]-Liste2[maxa][-2][2]<0.8)  and ((Liste2[maxi][-2][3]-Liste2[maxi][-2][4])-(Liste2[maxa][-2][3]-Liste2[maxa][-2][4])>8 and (Liste2[maxi][-2][3]-Liste2[maxi][-2][4])-(Liste2[maxa][-2][3]-Liste2[maxa][-2][4])<16):
            ListePronoExt.append(1)
            ListePronoExt.append(z)
            ListePronoExt.append(Liste1[z][0])
            ListePronoExt.append(Liste2[maxi][-2][2]-Liste2[maxa][-2][2])
            ListePronoExt.append((Liste2[maxi][-2][3]-Liste2[maxi][-2][4])-(Liste2[maxa][-2][3]-Liste2[maxa][-2][4]))
            ListePronoExt.append(Liste2[maxi][-2][-1])
    ListeN=[Liste2[maxa][-2][2]-Liste2[maxi][-2][2],(Liste2[maxa][-2][3]-Liste2[maxa][-2][4])-(Liste2[maxi][-2][3]-Liste2[maxi][-2][4])]
    if Liste2[maxa][-2][-1]<0:
        ListeN.append(Liste2[maxa][-2][-1])
    else:
        ListeN.append(Liste2[maxa][-2][-1])
    if Liste2[maxi][-2][-1]<0:
        ListeN.append(Liste2[maxi][-2][-1])
    else:
        ListeN.append(Liste2[maxi][-2][-1])
    ListeNeural.append(ListeN)
    ListeN=[]
    ajout=0
    a1=1
    a2=1
    b1=0
    b2=0
    maxa=0
    maxi=0


for z in range(nbMatchs):
    for i in range(30):
        if Liste2[i][0]==Liste4[z][0]:
            k=float(Liste2[i][1][2])
            deff=float(Liste2[i][1][4])
            w=float(Liste2[i][1][3])
    for a in range(30):
        if Liste2[a][0]==Liste4[z][1]:
            m=float(Liste2[a][1][2])
            deffe=float(Liste2[i][1][4])
            x=float(Liste2[a][1][3])
    Liste6=k,m
    points.append(Liste6)
    Liste6=[]


Resultat=0
Resultat2=0
ecartProno1=0
ecartProno2=0
ecartProno3=0
ecartProno4=0
ecartProno5=0
ecartProno6=0
ecartProno7=0
ecartProno8=0
PronoReussi2=0
PronoRater2=0
PronoReussi=0
PronoRater=0
for z in range(0,nbMatchs):
    for i in range(30):
        if Liste2[i][0]==Liste4[z][0]:
            li=i
            b=Liste2[i][0]
            f=Liste2[i][1][0]
            g=Liste2[i][1][1]
            k=float(Liste2[i][1][2])
            deff=float(Liste2[i][1][4])
            w=float(Liste2[i][1][3])
    for a in range(30):
        if Liste2[a][0]==Liste4[z][1]:
            la=a
            c=Liste2[a][0]
            d=Liste2[a][1][0]
            e=Liste2[a][1][1]
            m=float(Liste2[a][1][2])
            deffe=float(Liste2[i][1][4])
            x=float(Liste2[a][1][3])
    if (Liste2[la][-1][2]-Liste2[li][-1][2]>0 and Liste2[la][-1][2]-Liste2[li][-1][2]<0.5) and ((Liste2[la][-1][3]-Liste2[la][-1][4])-(Liste2[li][-1][3]-Liste2[li][-1][4])>5 and (Liste2[la][-1][3]-Liste2[la][-1][4])-(Liste2[li][-1][3]-Liste2[li][-1][4])<50) :
            print("")
            print(Liste2[li][0],Liste2[la][0])
            print("Victoire de: ",Liste2[la][0] )
            print(Liste2[la][-1][2]-Liste2[li][-1][2],(Liste2[la][-1][3]-Liste2[la][-1][4])-(Liste2[li][-1][3]-Liste2[li][-1][4]))
            PronoMatch.append(Liste2[la][0])
            
    elif (Liste2[li][-1][2]-Liste2[la][-1][2]>0.32 and Liste2[li][-1][2]-Liste2[la][-1][2]<0.8) and ((Liste2[li][-1][3]-Liste2[li][-1][4])-(Liste2[la][-1][3]-Liste2[la][-1][4])>8 and (Liste2[li][-1][3]-Liste2[li][-1][4])-(Liste2[la][-1][3]-Liste2[la][-1][4])<16):
            print("")
            print(Liste2[la][0],Liste2[li][0])
            print("Victoire de: ",Liste2[li][0] )
            print(Liste2[li][-1][2]-Liste2[la][-1][2],(Liste2[li][-1][3]-Liste2[li][-1][4])-(Liste2[la][-1][3]-Liste2[la][-1][4]))
            PronoMatch.append(Liste2[li][0])
            
for i in range(0,len(ListeProno),6):
    print("")
    print(ListeProno[i],Liste5[ListeProno[i+1]],ListeProno[i+2],Liste1[ListeProno[i+1]])
    if ListeProno[i]==Liste5[ListeProno[i+1]]:
        Resultat+=1
        print(ListeProno[i+3])
        print(ListeProno[i+4])
        print(ListeProno[i+5])
        ecartProno1+=ListeProno[i+3]
        ecartProno3+=ListeProno[i+4]
        PronoReussi+=1
        
    elif ListeProno[i]!=Liste5[ListeProno[i+1]]:
        print(ListeProno[i+3])
        print(ListeProno[i+4])
        print(ListeProno[i+5])
        ecartProno2+=ListeProno[i+3]
        ecartProno4+=ListeProno[i+4]
        PronoRater+=1
        
for i in range(0,len(ListePronoExt),6):
    print("")
    print(ListePronoExt[i],Liste5[ListePronoExt[i+1]],ListePronoExt[i+2],Liste1[ListePronoExt[i+1]])
    if ListePronoExt[i]==Liste5[ListePronoExt[i+1]]:
        Resultat2+=1
        #print(ListeProno[i+3])
        #print(ListeProno[i+4])
        print(ListePronoExt[i+5])
        color="g"
        ecartProno5+=ListePronoExt[i+3]
        ecartProno7+=ListePronoExt[i+4]
        PronoReussi2+=1
        
    elif ListePronoExt[i]!=Liste5[ListePronoExt[i+1]]:
        print(ListePronoExt[i+3])
        print(ListePronoExt[i+4])
        print(ListePronoExt[i+5])
        ecartProno6+=ListePronoExt[i+3]
        ecartProno8+=ListePronoExt[i+4]
        PronoRater2+=1
        
print("")
print("L'écart moyen de % entre chaque pronostic réussi est de: ",ecartProno1/PronoReussi)
print("")
print("L'écart moyen de % entre chaque pronostic rater est de: ",ecartProno2/PronoRater)
print("")
print("L'écart moyen d'ATT-DEF entre chaque match est de: ",ecartProno3/PronoReussi)
print("")
print(ecartProno4/PronoRater)
print("")
print(Resultat/(len(ListeProno)/6))
print("")
print(Resultat)
print("")
print(len(ListeProno)/6)
print("")
print("")
print(ecartProno6/PronoRater2)
print("")
print("")
print(ecartProno8/PronoRater2)
print("")
print(Resultat2/(len(ListePronoExt)/6))
print("")
print(Resultat2)
print("")
print(len(ListePronoExt)/6)
print("")
print((Resultat+Resultat2)/((len(ListeProno)/6)+(len(ListePronoExt)/6)))
print((len(ListeProno)/6)+(len(ListePronoExt)/6))
print(nb1/len(Liste5))


epochs=[]
def epochDeep(time=10,time2=100000,time3=0.001,time4=0):
    for epoch in range(1,time+1):
        print("TRY",epoch," ",end="")
        w2=np.random.random()
        w3=np.random.random()
        w1=np.random.random()
        w5=np.random.random()
        w6=np.random.random()
        w4=np.random.random()
        w7=np.random.random()
        w8=np.random.random()
        w9=np.random.random()
        w10=np.random.random()
        w11=np.random.random()
        w12=np.random.random()
        learn_rate=0.00001+time3*epoch
        costs=[]
        mi=0
        for i in range(time2):
            ri=np.random.randint(100,len(Liste1))
            g=ListeNeural[ri][0]
            k=ListeNeural[ri][1]
            d=ListeNeural[ri][2]
            if i%(time2/10)==0:
                print("/",end="")

            z0=NNDeep(g,k,d,w1,w2,w3)
            z1=NNDeep(g,k,d,w4,w5,w6)
            z2=NNDeep(g,k,d,w7,w8,w9)
            u=NNDeep(z0,z1,z2,w10,w11,w12)
            pred=u
            target=ListeTarget[ri]

            cos=cost(pred,target)
            costs.append(cos)
    
            dcos_pred=slope(pred,target)
            dpred_dz=sigmoid_p(z)
            dpred_du=sigmoid_p(u)
            dz_dw1=g
            dz_dw2=k
            dz_dw3=w
            dz_dw4=g
            dz_dw5=k
            dz_dw6=w
            dz_dw7=g
            dz_dw8=k
            dz_dw9=w
            du_dw10=z0
            du_dw11=z1
            du_dw12=z2
            dcos_dz=dpred_dz
            dcos_du=dcos_pred*dpred_du
            dcost_w1=dcos_dz*dz_dw1
            dcost_w2=dcos_dz*dz_dw2
            dcost_w3=dcos_dz*dz_dw3
            dcost_w4=dcos_dz*dz_dw4
            dcost_w5=dcos_du*dz_dw5
            dcost_w6=dcos_du*dz_dw6
            dcost_w7=dcos_dz*dz_dw7
            dcost_w8=dcos_dz*dz_dw8
            dcost_w9=dcos_dz*dz_dw9
            dcost_w10=dcos_du*du_dw10
            dcost_w11=dcos_du*du_dw11
            dcost_w12=dcos_du*du_dw12
            
            w1=w1-learn_rate*dcost_w1
            w2=w2-learn_rate*dcost_w2
            w3=w3-learn_rate*dcost_w3
            w4=w4-learn_rate*dcost_w4
            w5=w5-learn_rate*dcost_w5
            w6=w6-learn_rate*dcost_w6
            w7=w7-learn_rate*dcost_w7
            w8=w8-learn_rate*dcost_w8
            w9=w9-learn_rate*dcost_w9
            w10=w10-learn_rate*dcost_w10
            w11=w11-learn_rate*dcost_w11
            w12=w12-learn_rate*dcost_w12

            mi+=1
        print("")
        epoc=[w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12]
        epochs.append(epoc)
        epoc=[]
    return epochs
def epoch(time=10,time2=100000,time3=0.00001,time4=0):
    for epoch in range(1,time+1):
        print("TRY",epoch," ",end="")
        w2=np.random.random()
        w3=np.random.random()
        w1=np.random.random()
        w5=np.random.random()
        w6=np.random.random()
        w4=np.random.random()
        b=np.random.random()
        learn_rate=0.00001+time3*epoch
        costs=[]
        mi=0
        for i in range(time2):
            ri=np.random.randint(100,len(Liste1))
            g=ListeNeural[ri][0]
            k=ListeNeural[ri][1]
            d=ListeNeural[ri][2]
            if i%(time2/10)==0:
                print("/",end="")

            z=NN(g,k,d,w1,w2,w3,b)
            pred=z
            target=ListeTarget[ri]

            cos=cost(pred,target)
            costs.append(cos)
    
            dcos_pred=slope(pred,target)
            dpred_dz=sigmoid_p(z)
            dz_dw1=g
            dz_dw2=k
            dz_dw3=w
            dz_dw4=d
            dz_dw5=m
            dz_dw6=x
            dz_db=1
            dcos_dz=dcos_pred*dpred_dz
            dcost_w1=dcos_dz*dz_dw1
            dcost_w2=dcos_dz*dz_dw2
            dcost_w3=dcos_dz*dz_dw3
            dcost_w4=dcos_dz*dz_dw4
            dcost_w5=dcos_dz*dz_dw5
            dcost_w6=dcos_dz*dz_dw6
            dcost_db=dcos_dz*dz_db
        
            w1=w1-learn_rate*dcost_w1
            w2=w2-learn_rate*dcost_w2
            w3=w3-learn_rate*dcost_w3
            w4=w4-learn_rate*dcost_w4
            w5=w5-learn_rate*dcost_w5
            w6=w6-learn_rate*dcost_w6
            b=b-learn_rate*dcost_db
            mi+=1
        print("")
        epoc=[w1,w2,w3,b]
        epochs.append(epoc)
        epoc=[]
    return epochs
#print(w1,w2,w3,w4,w5,w6,b)
pro=0
proo=0
pct=[]
prooo=0
def epochTry(d=0.8):
    for epo in range(len(epochs)):
        pro=0
        proo=0
        prooo=0
        for i in range(len(Liste5)):
            ri=i
            g=ListeNeural[ri][0]
            k=ListeNeural[ri][1]
            d=ListeNeural[ri][2]
                

            z=NN(g,k,d,epochs[-1*epo][0],epochs[-1*epo][1],epochs[-1*epo][2],epochs[-1*epo][3])
            pred=z
            """print(Liste1[ri])
            print(Liste3[ri])
            print(Liste5[ri])"""
            if round(pred,2)>d:
                #print(pred*100,"%",Liste1[ri][1])
                pro=0
            elif round(pred,2)<1-d-0.1:
                #print((1-pred)*100,"%",Liste1[ri][0])
                pro=1
            else:
                #print("Je ne sais pas")
                pro=-1
                pass
            if pro==Liste5[ri]:
                proo+=1
                prooo+=1
                """print(proo)
                print(prooo)"""
                
            elif pro==-1:
                pass
            else:
                #print(proo)
                prooo+=1
                #print(prooo)
        """print((proo/prooo)*100)
        print(prooo)"""
        ListeA=[round((proo/prooo)*100,2),prooo,epo,epochs[epo]]
        pct.append(ListeA)
        ListeA=[]
        #print(epochs[epo])
    #print(pct)
    return "Done"
def epochTryDeep(d=0.8):
    for epo in range(len(epochs)):
        pro=0
        proo=0
        prooo=0
        for i in range(len(Liste5)):
            ri=i
            g=ListeNeural[ri][0]
            k=ListeNeural[ri][1]
            d=ListeNeural[ri][2]
                

            z0=NNDeep(g,k,d,epochs[-1*epo][0],epochs[-1*epo][1],epochs[-1*epo][2])
            z1=NNDeep(g,k,d,epochs[-1*epo][3],epochs[-1*epo][4],epochs[-1*epo][5])
            z2=NNDeep(g,k,d,epochs[-1*epo][6],epochs[-1*epo][7],epochs[-1*epo][8])
            u=NNDeep(z0,z1,z2,epochs[-1*epo][9],epochs[-1*epo][10],epochs[-1*epo][11])
            pred=u
            """print(Liste1[ri])
            print(Liste3[ri])
            print(Liste5[ri])"""
            if round(pred,2)>d:
                #print(pred*100,"%",Liste1[ri][1])
                pro=0
            elif round(pred,2)<1:
                #print((1-pred)*100,"%",Liste1[ri][0])
                pro=1
            else:
                #print("Je ne sais pas")
                pro=-1
                pass
            if pro==Liste5[ri]:
                proo+=1
                prooo+=1
                """print(proo)
                print(prooo)"""
                
            elif pro==-1:
                pass
            else:
                #print(proo)
                prooo+=1
                #print(prooo)
        """print((proo/prooo)*100)
        print(prooo)"""
        ListeA=[round((proo/prooo)*100,2),prooo,epo,epochs[epo]]
        pct.append(ListeA)
        ListeA=[]
        #print(epochs[epo])
    #print(pct)
    return "Done"
ListeEpochTest=[]
def epochTest(f=0.8,n=1):
    for epo in range(n):
        pro=0
        proo=0
        prooo=0
        for i in range(len(Liste5)):
            ri=i
            g=ListeNeural[ri][0]
            k=ListeNeural[ri][1]
            d=ListeNeural[ri][2]
                    
            
            z=NN(g,k,d,pct[-1*epo][-1][0],pct[-1*epo][-1][1],pct[-1*epo][-1][2],pct[-1*epo][-1][3])
            pred=z
            if round(pred,2)>f:
                """print(Liste1[ri])
                print(Liste3[ri])
                print(Liste5[ri])
                print(pred*100,"%",Liste1[ri][1])"""
                pro=0
                #print(pro)
            elif round(pred,2)<1-f-0.1:
                """print(Liste1[ri])
                print(Liste3[ri])
                print(Liste5[ri])
                print((1-pred)*100,"%",Liste1[ri][0])"""
                pro=1
                #print(pro)
            else:
                pro=-1
                pass
                #print("Je ne sais pas")
            if pro==Liste5[ri]:
                proo+=1
                prooo+=1
                """print(proo)
                print(prooo)"""
            elif pro==-1:
                pass
            else:
                prooo+=1
        #print((proo/prooo)*100)
        print(prooo)
        ListeI=[(proo/prooo)*100,pct[-1*epo][-1][0],pct[-1*epo][-1][1],pct[-1*epo][-1][2],pct[-1*epo][-1][3]]
        ListeEpochTest.append(ListeI)
        ListeI=[]
    return ListeEpochTest

def epochTestDeep(f=0.8,n=1):
    for epo in range(n):
        pro=0
        proo=0
        prooo=1
        for i in range(len(Liste5)):
            ri=i
            g=ListeNeural[ri][0]
            k=ListeNeural[ri][1]
            d=ListeNeural[ri][2]
                    
            
            z0=NNDeep(g,k,d,pct[-1*epo][-1][0],pct[-1*epo][-1][1],pct[-1*epo][-1][2])
            z1=NNDeep(g,k,d,pct[-1*epo][-1][3],pct[-1*epo][-1][4],pct[-1*epo][-1][5])
            z2=NNDeep(g,k,d,pct[-1*epo][-1][6],pct[-1*epo][-1][7],pct[-1*epo][-1][8])
            u=NNDeep(z0,z1,z2,pct[-1*epo][-1][9],pct[-1*epo][-1][10],pct[-1*epo][-1][11])
            pred=u
            if round(pred,2)>f:
                """print(Liste1[ri])
                print(Liste3[ri])
                print(Liste5[ri])
                print(pred*100,"%",Liste1[ri][1])"""
                pro=0
                #print(pro)
            elif round(pred,2)<1-f:
                """print(Liste1[ri])
                print(Liste3[ri])
                print(Liste5[ri])
                print((1-pred)*100,"%",Liste1[ri][0])"""
                pro=1
                #print(pro)
            else:
                pro=-1
                pass
                #print("Je ne sais pas")
            if pro==Liste5[ri]:
                proo+=1
                prooo+=1
                """print(proo)
                print(prooo)"""
            elif pro==-1:
                pass
            else:
                prooo+=1
        print((proo/prooo)*100)
        print(prooo)
        ListeI=[(proo/prooo)*100,pct[-1*epo][-1][0],pct[-1*epo][-1][1],pct[-1*epo][-1][2],pct[-1*epo][-1][3],pct[-1*epo][-1][4],pct[-1*epo][-1][5],pct[-1*epo][-1][6],pct[-1*epo][-1][7],pct[-1*epo][-1][8],pct[-1*epo][-1][9],pct[-1*epo][-1][10],pct[-1*epo][-1][11]]
        ListeEpochTest.append(ListeI)
        ListeI=[]
    return ListeEpochTest

def Predict(nbGame,t=0.8):
    PredictGame=[]
    Predictprct=[]
    for az in range(0,nbGame):
        prediction=[]
        for i in range(30):
            if Liste2[i][0]==Liste4[az][0]:
                li=i
        for a in range(30):
            if Liste2[a][0]==Liste4[int(az)][1]:
                la=a
        g=Liste2[la][-1][2]-Liste2[li][-1][2]
        k=(Liste2[la][-1][3]-Liste2[la][-1][4])-(Liste2[li][-1][3]-Liste2[li][-1][4])
        d=Liste2[la][-1][-1]
                

        z=NN(g,k,d,ListeEpochTest[-1][1],ListeEpochTest[-1][2],ListeEpochTest[-1][3],ListeEpochTest[-1][4])
        pred=z
        if round(pred,2)>t:
            print(Liste4[int(az)])
            prct=pred*100
            print(prct,"%",Liste4[az][1])
            pro=0
            print(pro)
            prediction=[Liste4[az][1],prct]
            Predictprct.append(prediction)
            print(g,k,d)
        elif round(pred,2)<1-t-0.1:
            print(Liste4[int(az)])
            prct=(1-pred)*100
            print(prct,"%",Liste4[az][0])
            pro=1
            print(pro)
            prediction=[Liste4[az][0],prct]
            Predictprct.append(prediction)
            print(g,k,d)
        else:
            print("Je ne sais pas")
    Predictprct.sort(key=sortSecond)
    if len(Predictprct)>=2:
        for i in range(1,3):
            PredictGame.append(Predictprct[-1*i][0])
    elif len(Predictprct)==1:
        PredictGame.append(Predictprct[-1][0])
    else:
        pass
    return PredictGame
def PredictDeep(nbGame,t=0.8):
    PredictGame=[]
    Predictprct=[]
    for az in range(0,nbGame):
        prediction=[]
        for i in range(30):
            if Liste2[i][0]==Liste4[az][0]:
                li=i
        for a in range(30):
            if Liste2[a][0]==Liste4[int(az)][1]:
                la=a
        g=Liste2[la][-1][2]-Liste2[li][-1][2]
        k=(Liste2[la][-1][3]-Liste2[la][-1][4])-(Liste2[li][-1][3]-Liste2[li][-1][4])
        d=Liste2[la][-1][-1]
                
        z0=NNDeep(g,k,d,ListeEpochTest[-1][1],ListeEpochTest[-1][2],ListeEpochTest[-1][3])
        z1=NNDeep(g,k,d,ListeEpochTest[-1][4],ListeEpochTest[-1][5],ListeEpochTest[-1][6])
        z2=NNDeep(g,k,d,ListeEpochTest[-1][7],ListeEpochTest[-1][8],ListeEpochTest[-1][9])
        u=NNDeep(z0,z1,z2,ListeEpochTest[-1][10],ListeEpochTest[-1][11],ListeEpochTest[-1][12])
        pred=u
        if round(pred,2)>t:
            print(Liste4[int(az)])
            prct=pred*100
            print(prct,"%",Liste4[az][1])
            pro=0
            print(pro)
            prediction=[Liste4[az][1],prct]
            Predictprct.append(prediction)
            print(g,k,d)
        elif round(pred,2)<1-t:
            print(Liste4[int(az)])
            prct=(1-pred)*100
            print(prct,"%",Liste4[az][0])
            pro=1
            print(pro)
            prediction=[Liste4[az][0],prct]
            Predictprct.append(prediction)
            print(g,k,d)
        else:
            print("Je ne sais pas")
    print(Predictprct)
    Predictprct.sort(key=sortSecond)
    if len(Predictprct)>=2:
        for i in range(1,3):
            PredictGame.append(Predictprct[-1*i][0])
    elif len(Predictprct)==1:
        PredictGame.append(Predictprct[-1][0])
    else:
        pass
    return PredictGame
ListeBest=[]
def sortSecond(val): 
    return val[1] 
nbEpoch=int(input("Number of epochs: "))
nbEpochs=int(input("Number of try: "))
var=0
PronoMatch2=[]
for i in range(nbEpochs):
    print("       EPOCHS NUMBER ",i+1)
    ListeEpochTest=[]
    pct=[]
    epochDeep(nbEpoch,10000,0.00001,0.00001)
    epochT=epochTryDeep(0.8+var*i) 
    pct.sort(key=sortSecond)
    epochTestDeep(0.8+var*i,nbEpoch).sort()
    print(ListeEpochTest[-1][0])
    ListeBest.append(ListeEpochTest[-1])
    print(PredictDeep(nbMatchs,0.6))
if nbEpochs>0:
    print("First pronostic")
    PronoMatch2=PredictDeep(nbMatchs,0.7)
    print(PronoMatch2)
ListeBest=[]
for i in range(nbEpochs):
    print("       EPOCHS NUMBER ",i+1)
    ListeEpochTest=[]
    pct=[]
    epoch(nbEpoch,10000,0.00001,0.00001)
    epochT=epochTry(0.8+var*i) 
    pct.sort(key=sortSecond)
    epochTest(0.8+var*i,nbEpoch).sort()
    print(ListeEpochTest[-1][0])
    ListeBest.append(ListeEpochTest[-1])
    print(Predict(nbMatchs,0.8))
print("ok")
if nbEpochs>0:
    print("Second pronostic")
    PronoMatch4=Predict(nbMatchs,0.8)
ListeBest.sort(key=sortSecond)
for i in range(nbEpochs):
    print(ListeBest[i][0],end=" ")
print("")
print("First list: ",PronoMatch)
print("")
print("Second list: ",PronoMatch2)
print("")
PronoMatch3=[]
for i in range(len(PronoMatch)):
        for b in range(len(PronoMatch2)):
            if PronoMatch[i]==PronoMatch2[b]:
                PronoMatch3.append(PronoMatch[i])
print("Third list:",PronoMatch4)
print("")
print("Fourth list:",PronoMatch3)
print("")
if nbEpochs>0:
    pickle_out=open("PronoMatch","wb")
    pickle.dump(PronoMatch, pickle_out)
    pickle.dump(PronoMatch2,pickle_out)
    pickle.dump(PronoMatch4,pickle_out)
    pickle.dump(PronoMatch3,pickle_out)
    pickle.dump(par,pickle_out)
    pickle.dump(ListeUpdate,pickle_out)
print((Resultat+Resultat2)/((len(ListeProno)/6)+(len(ListePronoExt)/6)))
print(par)