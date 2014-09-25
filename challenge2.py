import itertools
import time

solutions = [['O', 'B', 'P', 'B'], ['O', 'B', 'P', 'O'], ['O', 'B', 'P', 'P'], ['O', 'O', 'P', 'W'], ['O', 'P', 'P', 'W'], ['O', 'B', 'B', 'R'], ['O', 'B', 'R', 'R']]

perms = list(itertools.product("BORYPW", repeat=4))

for perm in perms:
  newPerm = list(perm)

  for sol in solutions:

    tmp = []
    for i in range(0,4):
      
      if sol[i] == newPerm[i]:
        tmp.append(newPerm[i])

    if tmp == sol: print tmp
