string = input("Enter the string: ")                                   #user input
letterCount, numberCount = 0, 0                                        # variable initialization
for i in string:                                                        
    if i.isalpha():                                                    #if the character is alphabet
        letterCount += 1                                               #increment letter count
    else:
        numberCount += 1                                               #increment number count
print("Alphabets:"+str(letterCount)+" & Number: "+str(numberCount))    #output

