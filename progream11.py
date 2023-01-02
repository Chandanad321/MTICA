sample_dict={
    "name":"Chandrakala",
    "age":27,
     "salary":90000,
     "city":"Krishna rajpuram"
}
keys=["name","salary"]
#newDict={}
d=dict()
for i in sample_dict.keys()-keys:
    d[i]=sample_dict[i]
print(d)
    
