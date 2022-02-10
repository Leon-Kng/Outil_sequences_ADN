
def Translation(DnaSeq,code,cadre): # code prend la valeur 1 ou 3 pour le type de codage des acides aminés et cadre prend la valeur 1, 2 et 3 pour choisir avec quel acide aminé commencer le cadre de lecture


    TableCodons = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',}

    CodeTranslator={"A":"Ala ", "R":"Arg ", "N":"Asn ", "D":"Asp ", "C":"Cys ", "E":"Glu ",
    "Q":"Gln ", "G":"Gly ", "H":"Hys ", "I":"Ile ", "L":"Leu ", "K":"Lys ", "M":"Met ", 
    "F":"Phe ", "P":"Pro ", "S":"Ser ", "T":"Thr ", "W":"Trp ", "Y":"Tyr ", "V":"Val ", "*":"STOP "} 

    SeqProt=""  # séquence en code à 1 lettre   
    SeqProtCode3="" # séquence en code à 3 lettres 


    if len(DnaSeq)>=9:   # vérification que la séquence soit de taille minimum
        if cadre == 1:
            LastCodon=(len(DnaSeq)%3)                       #permet de traduire même si pas un multiple de 3
            for i in range(0,(len(DnaSeq)-LastCodon),3):
                codon=DnaSeq[i:i+3]
                SeqProt+=TableCodons[codon]    

        if cadre == 2:
            LastCodon=(len(DnaSeq)%3)
            for i in range(1,(len(DnaSeq)-LastCodon-2),3):
                codon=DnaSeq[i:i+3]
                SeqProt+=TableCodons[codon]

        if cadre == 3:
            LastCodon=(len(DnaSeq)%3)  
            for i in range(2,(len(DnaSeq)-LastCodon-1),3):
                codon=DnaSeq[i:i+3]
                SeqProt+=TableCodons[codon]
   

        # on renvoie la séquence de la prot en fonction du codage choisi
        if code==1:
            return SeqProt

        if code==3:
            for n in SeqProt :
                SeqProtCode3+=CodeTranslator[n]
            return SeqProtCode3
            
        else:
            print("Erreur : Valeur autre que 1 ou 3 pour le code des acides aminés !!")
    else :
        print("Erreur : Séquence trop courte pour être traduite !!")

