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
    # for i in range(10):
    #     listCase.append([0])
    #     for o in range(10):
    #         listCase[i].append(0)
    # while input("Vous voulez ajouté des cases ? O/N")=="O":
    #     ligne=int(input("ligne?"))-1
    #     colonne=int(input("colonne?"))-1
    #     listCase[ligne][colonne]=1
    #     system('cls')
    #     affichage(listCase)
    listCase=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    while test==0:
        affichage(listCase)
        update(listCase)
        time.sleep(0.010)
        
    

def update(listCase):
    listCopy=[]
    for i in range(len(listCase)):
        listCopy.append(listCase[i])
        for o in range(len(listCase[i])):
            listCopy[i][o]=listCase[i][o]  
    for i in range(len(listCase)):
        for o in range(len(listCase[i])):
            viem=0
            for e in range(3):
                hor=e-1
                for f in range(3):                    
                    vert=f-1
                    if i+hor>-1 and o+vert>-1 and i+hor<len(listCopy) and o+vert<len(listCopy[i]) and (hor!=0 or vert!=0) and listCopy[i+hor][o+vert]==1:
                        viem+=1
                        # print(viem)
            if listCopy[i][o]==1:
                if viem<2 or viem>3:
                    listCase[i][o]=0
                else:
                    listCase[i][o]=1
            elif listCopy[i][o]==0:
                if viem==3:
                    listCase[i][o]=1
                else:
                    listCase[i][o]=0

def affichage(list):
    system('cls')
    print("refresh")
    print(oui)
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j]==1:
                if j!=len(list[i])-1:
                    print("\033[0;32;47m ",end=' ')
                else:
                    print("\033[0;32;47m"," ")
            else:
                if j!=len(list[i])-1:
                    print("\033[0;32;40m ", end = ' ')
                else:
                    print("\033[0;32;40m "," ")
    print("\033[0;32;40m"," ")

oui=0
listCase=[]
jeuDeLaVie(listCase)