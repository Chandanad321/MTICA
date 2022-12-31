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

fo=open(r"D:\31-12-22\day10.txt","a")
for i in range(5):
    inpstr=input("Enter astring:")
    fo.write(inpstr+'\n')
fo.close()
print("Written to file")



