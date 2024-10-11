temp = []
n = int(input("enter the length of the temperature list\n"))
for i in range(n):
    temp.append(int(input("Enter the list element\n")))

if not temp:
    print("Temperature Not Entered")
avgTemp, highestTemp,lowestTemp  = sum(temp) / len(temp), max(temp), min(temp)
print("Average Temperature "+str(avgTemp)+"\n Highest Temperature:"+str(highestTemp)+"\n  Lowest Temperature:"+str(lowestTemp))
