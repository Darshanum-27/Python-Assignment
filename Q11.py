inputValue = int(input("Input: "))                  # user input
initialValue = sum(int(i) for i in str(inputValue))     # calculate the initial sum     
while initialValue >= 10:                               # if inital value is greater than 10
        initialValue = sum(int(i) for i in str(initialValue))   # calculate the sum and reduce to number less than 10
print("Final Output: "+str(initialValue))               # output value