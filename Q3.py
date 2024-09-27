subjects = {'physics':0.0,'chemistry':0.0,'biology':0.0,'mathematics':0.0,'computer':0.0,}  #preinitialized dictionary
for i in subjects.keys():                                                                   #user input for the subject
    subjects[i] = float(input("Enter "+i+" marks (out of 100): "))
average = sum(subjects.values())/5                                                          # calculating average
print(" Percentage:"+str(average))  
if average >= 90:                                                                           #output based on value
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
elif average >= 40:
    print("Grade: E")
elif average < 40:
    print("Grade: F")