##def printMonth(dn):
##    if (dn==1):
##       return "January"
##    elif (dn==2):
##       return "February"
##    elif (dn==3):
##       return "March"
##    elif (dn==4):
##       return "April"
##    elif (dn==5):
##       return "May"
##    elif (dn==6):
##       return "June"
##    elif (dn==7):
##       return "July"
##    elif (dn==8):
##       return "August"
##    elif (dn==9):
##       return "September"
##    elif (dn==10):
##       return "October"
##    elif (dn==11):
##       return "November"
##    elif (dn==12):
##       return "December"
##    else:
##        return"Invalid"
##for i in range(3):
##    inpNum=int(input())
##    print(printMonth(inpNum))

months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'Augusst',9:'September',10:'October',11:'November',12:'December',}
n=int(input())
for count in range(n):
    mn=int(input())
    if mn>=1 and mn<=12:
        print(months[mn])
    else:
        print("INVALID")
