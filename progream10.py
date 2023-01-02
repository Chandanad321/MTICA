sample_dict={
    "name":"Chandrakala",
    "age":27,
     "salary":90000,
     "city":"Krishna rajpuram"
}
keys=["name","salary"]
#newDict={}
res=dict()
for k in keys:
    sample_dict.pop(k)
print(sample_dict)

    
