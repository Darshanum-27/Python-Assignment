def power(i):
    if i == 1:
        return True
    if i < 1:
        return False
    if i % 2 == 0:
        return power(i // 2)
    return False

l = []
n = int(input("enter the length of the temperature list\n"))
for i in range(n):
    l.append(int(input("Enter the list element\n")))
for i in l:
    print("Is "+str(i)+" a power of two? \n"+str(power(i)))