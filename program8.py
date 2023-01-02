employees=['Rani','Jani','Kani']
defaults={"designation":'Developer',"salary":20000}

data=dict.fromkeys(employees,defaults)
print(data)
print(data["Kani"])
