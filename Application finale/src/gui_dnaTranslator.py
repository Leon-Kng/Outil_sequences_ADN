import tkinter as tk
from dnaTranslator import Translation
from gui_dnaConRev import *

class WDnaTranslator(tk.Frame):
    dico={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    def __init__(self, racine=None):
        "Affiche la séquence protéique en tenant compte de 3 radios pour le cadre de lecture et 2 pour le code"
        tk.Frame.__init__(self, racine)
        self.racine=racine
        self.source=None
        self.createWidget()

    def createWidget(self):
        self.top=tk.Frame()
        w=self.top
        w.pack(fill=tk.BOTH, expand=1)
        LabelSeq=tk.Label(w, text="Séquence")
        LabelSeq.grid(column=1, row=2, padx=20)
        LabelProt=tk.Label(w, text="protéique")
        LabelProt.grid(column=1, row=3, padx=20)
        self.OptionCadre=tk.StringVar()
        self.textLbl=tk.Label(w, text="Cadre de lecture : ")
        self.textLbl.grid(column=2, row=2)
        self.optionCadre1 = tk.Radiobutton(w, text="1", var=self.OptionCadre, value=1, command=self.translatedna)
        self.optionCadre1.grid(column=3, row=1, padx=10)
        self.optionCadre2 = tk.Radiobutton(w, text="2", var=self.OptionCadre, value=2, command=self.translatedna)
        self.optionCadre2.grid(column=3, row=2, padx=10)
        self.optionCadre3= tk.Radiobutton(w, text="3", var=self.OptionCadre, value=3, command=self.translatedna)
        self.optionCadre3.grid(column=3, row=3, padx=10)
        self.OptionCode=tk.StringVar()
        self.textLbl=tk.Label(w, text="Code à : ")
        self.textLbl.grid(column=4, row=1, rowspan=4)
        self.optionCode1 = tk.Radiobutton(w, text="1 lettre", var=self.OptionCode, value=1, command=self.translatedna)
        self.optionCode1.grid(column=5, row=1)
        self.optionCode2 = tk.Radiobutton(w, text="3 lettres ", var=self.OptionCode, value=3, command=self.translatedna)
        self.optionCode2.grid(column=5, row=3)

        self.bottom=tk.Frame()
        w=self.bottom
        w.pack(fill=tk.BOTH, expand=1)
        self.vsb=tk.Scrollbar(w, orient=tk.VERTICAL)
        self.vsb.pack(fill=tk.Y, side=tk.RIGHT)
        
        self.textDna2=tk.Text(w, width=60, height=10)
        self.textDna2['yscrollcommand']=self.vsb.set
        self.textDna2.config(state=tk.DISABLED)
        
        self.vsb.config(command=self.textDna2.yview)

        self.textDna2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


    def translatedna(self):
        print("translatedna")
        if self.source != None :
            TypeCadre=int(self.OptionCadre.get())
            TypeCode=int(self.OptionCode.get())
            brin=self.source.getDNA()                           # trouver comment extraire la séquence pour la traduire 
            protein=Translation(brin,TypeCode,TypeCadre)               
            self.textDna2.config(state=tk.NORMAL)
            self.textDna2.delete("0.0",tk.END)
            self.textDna2.insert(tk.END, protein)   
            self.textDna2.config(state=tk.DISABLED)
            print("<<UpdateProt>>")
            print(protein)


    def onUpdateProtEvent(self, event):
        print("onUpdateProtEvent")
        self.source=event.widget
        self.translatedna()

# fonctionne !!

if __name__ == '__main__':
    import dnagen as dna
    class Appli(tk.Tk):
        def __init__(self):
            tk.Tk.__init__(self)                            

        def getDNA(self):
            brin=dna.genereDNA(50)
            brin="".join(brin)
            print("brin de root:<",brin,">",sep="")
            return brin

    def sendUpdateProtEvent():
        print("update prot event")
        root.event_generate("<<UpdateProt>>")
        root.after(5000, sendUpdateProtEvent )


    print("in main")
    root=Appli()
    w=WDnaTranslator(root)
    w.pack()
    w.bind_all("<<UpdateDNA>>", w.onUpdateProtSequenceEvent)
    root.bind_all("<<UpdateProt>>", onUpdateProtEvent)
    print("In loop")
    root.after(5000, sendUpdateProtEvent)
    
    root.mainloop()
