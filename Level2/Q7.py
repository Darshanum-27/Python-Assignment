# Sample Input
l = []
n = int(input("enter the length of the Elements list\n"))
for i in range(n):
    l.append(int(input("Enter the list element\n")))

output,n = sorted(l), len(l)
if n % 2 != 0:
    median = output[n // 2]
else:
    median = (output[n // 2] + output[n // 2 - 1]) / 2
print("Median:", median)