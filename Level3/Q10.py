def computers(N, S):
    l,outPeople = [], 0
    for i in S:
        if i not in l:
            if len(l) < N:
                l.append(i)
            else:
                outPeople += 1
        else:
            l.remove(i)
    return outPeople

print(computers(3, "GACCBDDBAGEE"))
print(computers(1, "ABCBAC"))