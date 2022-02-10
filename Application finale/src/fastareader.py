def fastaReader(name):
    with open(name, "r") as f:  # with permet de simplifier
        line=f.readline()       # saute 1ère ligne car juste infos séquence
        seq=f.readline()[:-1]   # initialize with the first sequence line
                                # and remove <cr>
        for line in f:
            seq+=line[:-1]       # concatenate without the <cr> character

    return seq

if __name__ == '__main__' :
    seq=fastaReader("./test.fasta")
    print(len(seq), " <", seq, ">", sep="")
