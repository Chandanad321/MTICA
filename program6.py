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
def printSeries(ch,n):
    sp='.'
    for i in range(0,n):
        print(sp*(n-i-1) +ch*(2*i+1)+sp*(n-i-1))
    return None
inpCh=input()
inpNum=int(input())
printSeries(inpCh,inpNum)
            



    






















































































































































    
