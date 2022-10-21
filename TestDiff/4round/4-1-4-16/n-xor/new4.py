from gurobipy import *

import math 

env = Env("best-diff-new-future-4.log")
filename = 'new_best_diff_future_4.lp'
m = read(filename,env)  
obj = m.getObjective()
m.optimize()
time = int(m.Runtime)
time = math.floor(time)
textfile = 'future-new-best-4.txt'
file = open(textfile,'w+')
file.write(str(time) + " seconds \n")
for v in m.getVars():
    if v.x == 1:
        print(v)
        file.write(str(v) + "\n")
file.close()