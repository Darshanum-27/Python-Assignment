inputNumber = int(input("Input Num = "))            #user input
outputNumber = 0
while inputNumber > 0:                              # logic for reversing the number
    outputNumber = outputNumber * 10 + (inputNumber % 10) # fetch last digit using mod and add to outputNumber
    inputNumber //= 10                              # divide number by 10
print("revnum = "+str(outputNumber))                # output
