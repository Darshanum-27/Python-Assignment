n = int(input("enter the number\n"))
stones = []
val = 2 if n % 2 == 0 else 1
for i in range(n):
    stones.append(val + 2 * i)
print("Stones in single pile :", stones)