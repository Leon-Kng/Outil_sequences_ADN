from tkinter import *
from random_sequence import *

def genereCmd():
	dnaLen=int(dnaLenStr.get())
	print("dna length : ",dnaLen)
	brin=genereDNA(dnaLen)
	textDna.delete("0.0", END)
	textDna.insert(END,brin)

def validerCmd(s):
	print(s)
	print("dans validerCmd")
	return s.isdigit()

def erreurCmd(s):
	t=Toplevel(racine)
	Label(t, text="Error: Invalide input %s" %s).pack(padx=5,pady=5)
	Button(t, text="Ok", command=t.destroy).pack(padx=5,pady=5)

#====================================================================================

racine=Tk()
racine.title("Générateur de séquence")

GenBut=Button(racine, text="Générer", command=genereCmd)
GenBut.pack(padx=50, pady=20)

cmdValider=(racine.register(validerCmd),"%S")
cmdErreur=(racine.register(validerCmd),"%S")
dnaLenStr=StringVar();
dnaLenStr.set("50")

chiffreEnt=Entry(racine, width=10, justify=RIGHT)
chiffreEnt['textvariable']=dnaLenStr
chiffreEnt['validate']="key",
chiffreEnt['invcmd']=cmdErreur
chiffreEnt['vcmd']=cmdValider
chiffreEnt.pack()

textDna=Text(racine, width=60, height=10)
textDna.pack(side=BOTTOM, padx=10, pady=10)

racine=mainloop()
