import tkinter as tk

class WDnaConRev(tk.Frame):
    dico={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    def __init__(self, racine=None):
        "Affiche la séquence d'ADN en tenant compte de 2 checkbuttons"
        tk.Frame.__init__(self, racine)
        self.racine=racine
        self.source=None
        self.createWidget()

    def createWidget(self):
        self.top=tk.Frame()
        w=self.top
        w.pack(fill=tk.BOTH, expand=1)
        self.vrev = tk.IntVar()
        self.vcomp= tk.IntVar()
        self.titre=tk.Label(w, text="Séquence d'ADN")
        self.titre.pack(side=tk.LEFT)
        self.wrev = tk.Checkbutton(w, text="Réverse", variable=self.vrev, command=self.handleDNA)
        self.wrev.pack(side=tk.LEFT)
        self.wcomp = tk.Checkbutton(w, text="Complément", variable=self.vcomp, command=self.handleDNA)
        self.wcomp.pack(side=tk.LEFT)
        

        self.bottom=tk.Frame()
        w=self.bottom
        w.pack(fill=tk.BOTH, expand=1)
        self.vsb=tk.Scrollbar(w, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.textDna=tk.Text(w, width=60, height=10)
        self.textDna['yscrollcommand']=self.vsb.set
        self.textDna.config(state=tk.DISABLED)
        self.vsb.config(command=self.textDna.yview)
        self.textDna.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
       
    def handleDNA(self):
        print("handleDNA")
        if self.source != None :
            brin=self.source.getDNA()
            print("handleDNA brin:", brin)
            if self.vcomp.get() :
                print("in complement")
                lst=[]
                for c in brin:
                    lst.append(self.dico[c])
                brin=lst
            print("handleDNA brin after comp:", brin)
            if self.vrev.get() :
                print("in reverse")
                brin=brin[::-1]
            print("handleDNA brin after reverse:", brin)
            self.textDna.config(state=tk.NORMAL)
            self.textDna.delete("0.0",tk.END)
            self.textDna.insert(tk.END,"".join(brin))
            self.textDna.config(state=tk.DISABLED)
            self.event_generate("<<UpdateProt>>")


        
    def onUpdateDnaSequenceEvent(self, event):
        print("onUpdateDnaSequenceEvent")
        self.source=event.widget
        self.handleDNA()

    def getDNA(self):
        brin= self.textDna.get(1.0, tk.END)
        brin=brin.strip(" \n")
        return brin

if __name__ == '__main__':
    import dnagen as dna
    class Appli(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)

        def getDNA(self):
            brin=dna.genereDNA(100)
            brin="".join(brin)
            print("brin de root:<",brin,">",sep="")
            return brin

    def sendUpdateDnaEvent():
        print("update DNA event")
        root.event_generate("<<UpdateDNA>>")
        root.after(5000, sendUpdateDnaEvent )

    def onUpdateProtEvent(event):
        brin=event.widget.getDNA()
        print("UpdateProtEvent:<",brin,">", sep="")
        

    print("in main")
    root=Appli()
    w=WDnaConRev(root)
    w.pack()
    w.bind_all("<<UpdateDNA>>", w.onUpdateDnaSequenceEvent)
    root.bind_all("<<UpdateProt>>", onUpdateProtEvent)
    print("In loop")
    root.after(5000, sendUpdateDnaEvent )
    
    root.mainloop()

