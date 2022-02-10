import tkinter as tk
import tkinter.filedialog as tkf # python3
import fastareader as fasta
from PIL import ImageTk,Image
from os import *


class WDnaMenu(tk.Frame):
    def __init__(self, racine=None):
        "Le constructeur de la menubar"
        tk.Frame.__init__(self, racine)
        self.racine=racine
        
        self.menu=tk.Menu(racine)
        
        self.createMenu()
        
        racine.config(menu=self.menu)
        

    def createMenu(self):
        w=self.menu
        w.add_cascade(label="File", menu=self.createFileMenu())
        w.add_cascade(label="Tool", menu=self.createToolMenu())
   
    def createFileMenu(self):
        #=============================================File option
        m=tk.Menu(self, tearoff=0)
        m.add_command(label="Open Fasta", command=self.cmdOpenFasta)
        m.add_separator()
        m.add_command(label="Exit", command=self.racine.quit)
        return m


    def createToolMenu(self):
        #=============================================Tool option
        m = tk.Menu(self, tearoff=0)
        m.add_command(label="Table des codons", command=self.FenTableCodons)
        return m


    def FenTableCodons(self):   # afficher le tableau des codons dans les outils
        FenTable = tk.Toplevel(self) 
        FenTable.geometry("450x447")    
        FenTable.title("Table des codons")
        global img
        img = Image.open("..\Projet_final\src\picture\Table_Codons.png")
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(FenTable, image=img)
        panel.pack()


    def cmdOpenFasta(self):
        opts = {    'filetypes': (('fasta', '.fasta'),
                              ('fsta', '.fsta'),
                              ('Text files', '.txt'),
                              ('All files', '.*'),)}
        opts['title'] = 'Select a file to open...'
        fn = tkf.askopenfilename(**opts)
        if len(fn) > 0 :
            self.seq=fasta.fastaReader(fn)
            print("in cmdOpenFasta", self.bindtags())
            print("length:", len(self.seq))
            self.event_generate("<<NewDNA>>")
            

    def getDNA(self):
        return self.seq
    
        
if __name__ == '__main__':
    
    def affiche(event):
        print("in affiche")
        print(event.widget.getDNA())
        

    print("in main")
    root=tk.Tk()
    fm=WDnaMenu(root)
    fm.pack()
    
    root.bind_all("<<NewDNA>>", affiche)
    
    root.mainloop()
