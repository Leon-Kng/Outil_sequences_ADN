import tkinter as tk
from os import *
from sys import *
path.insert(0,"..\Projet_final\src")    # on ajoute le chemin de nos modules(du package)
from gui_dnagenerator import *
from gui_dnamenu import *
from gui_dnapresenter import *
from gui_nucleotidecounter import *
from gui_dnaConRev import *
from gui_dnaTranslator import *


def test(event):
    print("==================TEST=================")

if __name__ == '__main__':      # on lance que si utilisation du code principal
    print("in main")
    root=tk.Tk()
    root.title("Programme de transcription")   #choix du titre de la fenêtre root
    root.iconbitmap(r"..\Projet_final\src\picture\icon_dna.ico")    # ajout d'une icone à côté du titre
# le menu
    wmen=WDnaMenu(root)
    wmen.pack()


#le menu du haut
    ftop=tk.Frame()
    ftop.pack(side=tk.TOP, fill=tk.X)

    wgen=WDnaGenerator(ftop)
    wcnt=WNucleotideCounter(ftop)
    
    wgen.pack(side=tk.LEFT)
    wcnt.pack(side=tk.RIGHT)

    wpres=WDnaPresenter(root)
    wpres.pack(fill=tk.BOTH, expand=1)

wcr=WDnaConRev(root)
wcr.pack(fill=tk.BOTH, expand=1)
    
wtranslator=WDnaTranslator(root)
wtranslator.pack(fill=tk.BOTH, expand=1)
    
root.bind_all("<<NewDNA>>", wpres.onNewDnaSequenceEvent)
root.bind_all("<<UpdateDNA>>", wcnt.onUpdateDnaSequenceEvent)

root.bind_all("<<UpdateDNA>>", wcr.onUpdateDnaSequenceEvent, add="+")
root.bind_all("<<UpdateProt>>", wtranslator.onUpdateProtEvent)

root.mainloop()
