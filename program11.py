class Number:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
n1=int(input())
n2=int(input())
ob=Number(n1,n2)
print(n1,'+',n2,'=',ob.add(),sep='')
