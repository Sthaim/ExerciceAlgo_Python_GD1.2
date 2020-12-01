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


listTest=[0,5,1,8,9]
# print(isBissextile(2020))
# print(20//4)
print(isValidCardNumber(8763))