"""def printSeriesIncreasing(ch,n):
    for i in range(1,n+1,1):
        print(ch*i)
    return None
inpCh=input("enter a character:")
inpNum=input("enter a no:")
printSeriesIncreasing(inpCh,inpNum)
print('-'*40)
printSeriesDecreasing(inpCh,inpNum) """   


"""def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),'first argument shouldnbe string'
    assert isinstance(n,int),'second argument shouldnbe integer'
    for i in range(n,0,-1):
        print(ch*i)
    return None"""
"""
def printSeries(n):
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end=' ')
            num+=1
    return None
inpNum=int(input())
printSeries(inpNum)"""
def printMonth(dn):
    mn=''
    if(dn==1):
        return "january"
    elif(dn==2):
        mn= "february"
    elif(dn==3):
        mn= "march"
    elif(dn==4):
        mn= "april"
    elif(dn==5):
        mn= "may"
    elif(dn==6):
        mn= "june"
    elif(dn==7):
        mn= "july"
    elif(dn==8):
        mn= "august"
    elif(dn==9):
        mn= "september"
    elif(dn==10):
        mn= "october"
    elif(dn==11):
        mn= "november"
    elif(dn==12):
        mn= "december"
    else:
        mn="invalid"
  
for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
            



    






















































































































































    
