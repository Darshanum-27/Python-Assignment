studs,subs, OutputDictionary = ["Sam", "Alice", "Mona"], ["Commerce", "Science", "Computer"], {}

print("For Loops Methods")
for i in range(len(studs)):
    OutputDictionary[studs[i]] = subs[i]
print(OutputDictionary)

print("\n Dictionary Comprehension Method")
print({student: subject for student, subject in zip(studs, subs)})