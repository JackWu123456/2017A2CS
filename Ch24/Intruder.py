#Jack Wu opt3
print("start")
print("System inactive")
system_active = False
a = int(input("Sir, would you like to press button?"))
if a == 1:
    system_active = True
else:
    system_active = False
    print("system inactive")
if system_active == True:
    b = int(input("Sir, would you like to intrude?"))
    if b==1:
        system_alert= True
        print("alert")
    else:
        system_alert= False
        print("No alert")
        

        
        
        
   
