numheads = 6
numlegs = 28
l1=()

def solve(numheads, numlegs):
    for numspiders in range(0,numheads):
	for numchicks in range(0,numheads):
		numpigs = numheads - numchicks - numspiders
		totlegs = 4*numpigs + 2*numchicks + 8*numspiders
	#        print totlegs
		if totlegs == numlegs:
		   return(numchicks,numpigs,numspiders)
    return(None,None,None)

l1 = solve(numheads,numlegs)
#solve(numheads,numlegs)
print l1
