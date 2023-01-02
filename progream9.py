sample_dict={
    "name":"Mikki",
    "age":25,
     "salary":70000,
     "city":"Bangulore"}
keys=["name","salary"]
newDict={}
for i in keys:
    newDict[i]=sample_dict[i]
print(newDict)

newDict={ i:sample_dict[i] for i in keys }
print(newDict)

    
