import random

def genereDNA(n):   # générateur de séquence d'ADN
    i=0;
    l=[]
    while i < n :
        l.append(random.choice(['A','G','C','T']))
        i+=1

    return l

ll=genereDNA(100)
#print("".join(ll))
