"""def add(*n):
    temp=0
    for i in n:
        temp+=i
    return temp
print("add():",add())
print("add(5):",add(5))
print("add(5,7):",add(5,7))
print("add(5,7,2):",add(5,7,2))
print("add(5,7,2,11,55,77,22):",add(5,7,2,11,55,77,22))"""

fo1=open(r"D:\31-12-22\day10.txt","r")
fo2=open(r"D:\31-12-22\day10a.txt","w+")

temp=fo1.read()
fo2.write(temp)

fo1.close()
fo2.close()
print("File copied")
              

