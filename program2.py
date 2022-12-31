"""def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero at MTICA!"
   reS=((Temperature-273)*1.8)+32
   return res
try:
    print(KelvinToFahrenheit(-50))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenheit(273))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenheit(505.78))
except Exception as ob:
    print(ob)
try:
    print(KelvinToFahrenheit(-5))
except Exception as ob:
    print(ob)
print("thank you")"""
def Factorial(num):
    assert(num>=0),"Factorial of negative number is not defined!"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-45))
except Exception as obj:
    print(obj)

try:
    print(Factorial(45))
except Exception as obj:
    print(obj)
        
