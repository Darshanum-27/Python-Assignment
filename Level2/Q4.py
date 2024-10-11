l = []
n = int(input("enter the length of the input list\n"))
for i in range(n):
    l.append(int(input("Enter the list element\n")))
d = int(input("enter the value of d\n"))
d = d % len(l)
print("Array after rotation:", l[-d:] + l[:-d])