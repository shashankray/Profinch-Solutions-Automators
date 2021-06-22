#nPr = 665280 = 6 lac 65 thousand 280

from itertools import permutations
perm = permutations([1,1,1,1,1,1,0,0,0,0,0,0], 6)
file = open('data.csv', "a")
for i in list(perm):
    file.write(str(i))

file.close()