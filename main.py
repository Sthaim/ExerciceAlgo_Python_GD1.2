from os import system
import time

def isBissextile(ann):
    test="false"
    if ann%4==0 and ann%100>0:
        test='true'
    return test

def isValidCardNumber(number):
    retur="false"
    finale=[number//1000]
    ver=0
    number=number-(number//1000)*1000
    finale.insert(0,number//100)
    number=number-(number//100)*100
    finale.insert(0,number//10)
    number=number-(number//10)*10
    finale.insert(0,number//1)
    if finale[1]*2>9:
        finale[1]=(finale[1]*2)//10+((finale[1]*2)-(finale[1]*2)//10*10)//1
    if (finale[3]*2)>9:
        print(finale[2])
        finale[3]=(finale[3]*2)//10+((finale[3]*2)-(finale[3]*2)//10*10)//1
        print(finale[2])
    for i in finale:
        ver+=i
    if ver%10==0:
        retur="true"
    return retur
    



def contain(list,numRech):
    test = "false"
    for i in list:
        if numRech == i:
            test="true"
    return test

def moyenne(list):
    moy=0
    for i in list:
        moy+=i
    moy=moy/2
    return moy

def jeuDeLaVie(listCase):
    test=0
    for i in range(10):
        listCase.append([0])
        for o in range(10):
            listCase[i].append(0)
    # while input("Vous voulez ajouté des cases ? O/N")=="O":
    #     ligne=int(input("ligne?"))-1
    #     colonne=int(input("colonne?"))-1
    #     listCase[ligne][colonne]=1
    #     system('cls')
    #     affichage(listCase)
    listCase[0][0]=1
    listCase[1][1]=1
    listCase[1][0]=1
    while test==0:
        update(listCase)
        time.sleep(1)
        affichage(listCase)
    

def update(listCase):
    listCopy=[]
    for i in range(len(listCase)):
        listCopy.append(listCase[i])
        for o in range(len(listCase[i])):
            listCopy[i][o]=listCase[i][o]  
    viem=0
    for i in range(len(listCase)):
        for o in range(len(listCase[i])):
            viem=0
            for e in range(3):
                hor=e-1
                for f in range(3):                    
                    vert=f-1
                    if i+hor!=-1 and o+vert!=-1 and i+hor<len(listCopy) and o+vert<len(listCopy[i]) and listCopy[i+hor][o+vert]==1 and hor!=0 and vert!=0:
                        viem+=1
                        # print(viem)
            if listCopy[i][o]==1:
                if viem<2 or viem>3:
                    listCase[i][o]==0
                else:
                    listCase[i][o]==1
            else:
                if viem==3:
                    listCase[i][o]=1
                else:
                    listCase[i][o]=0

def affichage(list):
    system('cls')
    for i in range(len(list)):
        print(list[i])
listCase=[]
jeuDeLaVie(listCase)