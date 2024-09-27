inputValue, output = int(input("Enter a number: ")), 1      #user input
for i in range(1, inputValue + 1):                          #using for loops to calculat factorial
    output *= i
print("Factorial of Number "+str(inputValue)+" is "+str(output))    #output 