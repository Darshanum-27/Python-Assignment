startValue, stopValue = int(input("Start: ")), int(input("Stop: "))         #user input
s = 0                                                                           
output = [s+i for i in range(startValue, stopValue + 1) if i % 2 != 0 ]     #calculating odd number in intervals and add to list
print("Sum of odd numbers: "+str(sum(output)))                              # returning the output