input, output, count = "wwwwaaadebbbbbw", "",1

for i in range(0, len(input)-1):
    if input[i] != input[i+1]:
        output += input[i] + str(count)
        count = 1
    else:
        count += 1
output=output+input[-1]+str(count)
print(output)