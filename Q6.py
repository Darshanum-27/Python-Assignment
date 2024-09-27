inputValue = int(input("Input: "))      #user input
if inputValue>1:                        # value should be greater than 1
    output = 0
    for i in range(1, inputValue):      
        if inputValue % i == 0:
            output += i
    print('Yes' if(output == inputValue) else 'No') # if value is equal then perfect Number
else:
    print('False')                  #number less than 1