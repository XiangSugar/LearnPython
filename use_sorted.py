# -*- coding : utf-8 -*-
#The use of sorted()

L1 = sorted([12,90,-3,-56,7])
print(L1)

L2 = sorted([12,90,-3,-56,7], key = abs)
print(L2)

#--------------------------------------
L3 = sorted(['haha','Bob','jack','Tom'])
print(L3)

L4 = sorted(['haha','Bob','jack','Tom'], key = str.lower)
print(L4)

#-----------------------------------------
L = [('Bob', 75), ('Adma', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return -t[1]

L5 = sorted(L, key=by_name)
L6 = sorted(L, key=by_score)
print(L5,'\n',L6)







