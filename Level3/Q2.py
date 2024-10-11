with open('/Users/darshanum/Desktop/Python-Assignment/Level3/demo.txt', 'r') as file:
    count = sum(1 for line in file)

if count>0:
    print("'Demo.txt' has "+str(count)+" lines")