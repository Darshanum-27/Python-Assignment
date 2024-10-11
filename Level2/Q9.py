l = []
n = int(input("enter the length of the Elements list\n"))
for i in range(n):
    l.append(int(input("Enter the list element\n")))
index = int(input("Enter the index\n"))
try:
    print("Element is at index "+str(index)+":"+l[index])
except IndexError:
    print("IndexError Exception: "+str(index)+" is out of range")
