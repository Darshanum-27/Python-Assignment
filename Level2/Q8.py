# Sample Input
string, count = input("Enter the input string to count the number of Vowels\n").lower(), 0
for i in string:
    if i in ['a','e','i','o','u']:
        count += 1

print("Number of vowels:", count)