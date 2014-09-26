import itertools
import time
import pdb

#count = 0
# solutions is the list of possible answers based off the three hints from the probelm
solutions = [['O', 'B', 'P', 'B'], ['O', 'B', 'P', 'O'], ['O', 'B', 'P', 'P'], ['O', 'O', 'P', 'W'], ['O', 'P', 'P', 'W'], ['O', 'B', 'B', 'R'], ['O', 'B', 'R', 'R']]

#solutions = [['O', 'B', 'P', 'B']]

# create every possible permutation for this game
perms = list(itertools.product("BORYPW", repeat=4))
#perms = [['O', 'B', 'P', 'P'], ['O', 'B', 'P', 'O']]

# Iterate through every permutation
for perm in perms:

  results = []

  # Iterate through every potential solution
  for sol in solutions:

    tmpPerm = list(perm)
    tmpSol  = list(sol)
    tmpResult = ''

    # Iterate through once to check for x matches
    for y in range(0,4):
      #pdb.set_trace()
      if tmpPerm[y] == tmpSol[y]:
        tmpResult = 'x'+tmpResult
        tmpPerm[y] = 'X'
        tmpSol[y]  = 'X'

    # Compare characters to return proper x's and o's
    for i in range(0,4):

      #pdb.set_trace()
      for j in range(0,4):
        # Next, check if it is an o match, and change tmpPerm inedex to a default non-match
        if tmpPerm[i] == tmpSol[j] and tmpPerm[i] != 'X':
          tmpResult += 'o'
          tmpPerm[i] = 'X'
          tmpSol[j]  = 'X'

    # add the result to a list
    results.append(tmpResult)

  #print results
  #print len(solutions)

  #print perm

  # count the number of unique answers, and if each solution has a unique answer, show that permutation
  if len(list(set(results))) == 7:
    print perm
    #print tmpPerm
    #print sol
    #print tmpSol
    #print list(set(results))
    print results
    print ''
#    count += 1
#print count
