# coding: utf-8

def randmutADN(seq,n):
    import random as rdm
    nuc = ["C","G","T","A"]
    long = len(seq)
    seqList = list(seq)
    mutseq = seqList.copy()
    tempseq = seqList.copy()
    lastindex = []
    temp_index = rdm.randint(0,(long-1))  
    while n>0:
        while temp_index in lastindex:
            temp_index=rdm.randint(0,(long-1))
        while mutseq == tempseq:   
            tempseq[temp_index] = rdm.choice(nuc)         
        lastindex.append(temp_index)     
        mutseq = tempseq.copy()    
        n-= 1
    strmutseq = "".join(mutseq)  
    return strmutseq


def randmutARN(seq,n):
    import random as rdm
    nuc = ["C","G","U","A"]
    long = len(seq)
    seqList = list(seq)
    mutseq = seqList.copy()
    tempseq = seqList.copy()
    lastindex = []
    temp_index = rdm.randint(0,(long-1))   
    while n>0:
        while temp_index in lastindex:
            temp_index=rdm.randint(0,(long-1))
        while mutseq == tempseq:   
            tempseq[temp_index] = rdm.choice(nuc)         
        lastindex.append(temp_index)     
        mutseq = tempseq.copy()    
        n-= 1
    strmutseq = "".join(mutseq)  
    return strmutseq

ARNorDNA=input("Quel type d'acide nucléique s'agit-il ? (ADN ou ARN ?) ")
if ARNorDNA not in ["ARN","arn","Arn","ADN","adn","Adn"]:
    print("Erreur dans le type d'acide nucléique !!!")

else:
    séquence = input("Insérer votre séquence : ")
    nbmutations = int(input("Combien de mutation(s) désirez vous ? "))
    if ARNorDNA in ["ARN","arn","Arn"]:
            print("Votre séquence mutée : ", randmutARN(séquence , nbmutations))

    if ARNorDNA in ["ADN","adn","Adn"]:
            print("Votre séquence mutée : ", randmutADN(séquence , nbmutations))


#souligner ou mettre en couleur le ou les nucléotides modifiés 
#tester si erreur dans la séquence ou si bien composé uniquement des nucléotides possibles CGTA ou CGUA 
