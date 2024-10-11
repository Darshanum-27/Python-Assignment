l = []
n = int(input("enter the length of the input list\n"))
for i in range(n):
    l.append(int(input("Enter the list element\n")))
print(list(dict.fromkeys(l)))