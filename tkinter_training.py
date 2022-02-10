from tkinter import *

root = Tk()      #on crée la fenêtre racine

root.title("Random Mutation Generator")   #choix du titre de la fenêtre root
root.geometry("450x720")      #choix de la taille de la fenêtre root
root.minsize(450,720)          #bloque la taille minimum de root
root.resizable(width=False, height=False)
root.iconbitmap(r"C:\Users\WIN7\Desktop\Code_PC\ADN.ico")   #choix icone fenêtre
root.config(background="#5F0065")      #choix couleur arrière plan 

label_title=Label(root, text="Entrer votre séquence")     #on crée un composant qui permet de mettre du texte et on le place sur root
label_title.pack()  #empacte le widget dans son parent 


root.mainloop()  #afficher la fênetre root
 
