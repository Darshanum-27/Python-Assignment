with open('/Users/darshanum/Desktop/Python-Assignment/Level3/doc.txt', 'r') as file: #change path while running
    wordLine, evenStrings = file.readlines(), []
    for i in wordLine:
        for word in i.split():
            processedKey = ''.join(j for j in word if j.isalnum())
            if len(processedKey) % 2 == 0:
                evenStrings.append(word)

print("Following Even length Strings were found")
for string in evenStrings:
    print(string)