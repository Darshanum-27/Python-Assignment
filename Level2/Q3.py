l = []
n = int(input("enter the length of the input list\n"))
for i in range(n):
    l.append(int(input("Enter the list element\n")))
k = int(input("enter the value of k\n"))

count,visited = 0, set()
for num in l:
    complement = k - num
    if complement in visited:
        count += 1
    visited.add(num)
print("Pair count:", count)
