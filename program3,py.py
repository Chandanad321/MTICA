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

def printSeries(n):
    num=1
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(num,end=' ')
            num+=1
    return None
inpNum=int(input())
printSeries(inpNum)
            



    






















































































































































    
