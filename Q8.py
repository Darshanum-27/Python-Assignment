number1,number2  = int(input("Enter Number1 = ")), int(input("Enter Number2 = ")) # user input
HigherNumber = max(number1, number2)                                              # higher number among the 2 
while True:                                                                       # infinite loop
    if HigherNumber % number1 == 0 and HigherNumber% number2 == 0:                  # check if number greater than higher number divides both the numbers
        outputValue = HigherNumber                                              # change output LCM to higher value
        break
    HigherNumber += 1
print("LCM of "+str(number1)+" and "+str(number2)+" is: "+str(outputValue))     # output