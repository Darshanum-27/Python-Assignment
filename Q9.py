inputList = input('Enter elements of a list with spaces').split()  # user input list with spaces    
freq_dict = dict()                                                  # empty dictionary
for i in inputList:                                                 
    # if elment in dictionary just increment its value 
    if i in freq_dict.keys():
        freq_dict[i]= freq_dict[i]+1
    else:
        # if elment not in dictionary initialize its value to 0 and then increment its value
        freq_dict[i]= freq_dict.get(i,0)+1 
print('Frequency count: '+str(freq_dict)) # output