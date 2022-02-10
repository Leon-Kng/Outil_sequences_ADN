from random import *
nuc=["C","G","T","A"]
def genereDNA(x):
	seq=[]
	while x>0:
		x-=1
		seq.append(choice(nuc))
	return(seq)

genereDNA(50)
