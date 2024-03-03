from tkinter import *
import tkinter.messagebox as tkMessageBox

class GestionStock:
    def __init__(self, parent):
        self.parent = parent
        
        self.label = Label(parent, text="GESTION DE STOCK Du MAGASIN", font=("Helvetica", 20, "bold"), bg="white")
        self.label.grid(row=0, column=0, padx=80, pady=10)
        
        btn_ajouter = Button(parent, text="Ajouter produit", font=("Helvetica", 13, "bold"), command=self.ajouter_produit_interface, width=20, height=2, bg='lightgreen')
        btn_ajouter.grid(row=1, column=0, padx=20, pady=10)
        
        btn_modifier = Button(parent, text="Modifier produit", font=("Helvetica", 13, "bold"), command=self.modifier_produit_interface, width=20, height=2, bg='lightblue')
        btn_modifier.grid(row=2, column=0, padx=20, pady=10)
        
        btn_supprimer = Button(parent, text="Supprimer produit", font=("Helvetica", 13, "bold"), command=self.supprimer_produit_interface, width=20, height=2, bg='red')
        btn_supprimer.grid(row=3, column=0, padx=20, pady=10)
        
        btn_afficher = Button(parent, text="Afficher stock", font=("Helvetica", 13, "bold"), command=self.afficher_stock_produits, width=20, height=2, bg='lightcoral')
        btn_afficher.grid(row=4, column=0, padx=20, pady=10)
    
    def ajouter_produit_interface(self):
        self.new_window = Toplevel(self.parent)
        self.new_window.title("Ajouter produit")
        self.new_window.geometry('400x300')
        self.new_window.configure(bg="white")
        
        self.label = Label(self.new_window, text="Ajouter Produit", font=("Helvetica", 15, "bold"), bg="white")
        self.label.grid(row=0, column=0, columnspan=2, sticky="nsew")


        self.label_reference = Label(self.new_window, text="Référence:", font=("Helvetica", 12, "bold"), bg="white")
        self.label_reference.grid(row=1, column=0, padx=10, pady=5)
        self.entry_reference = Entry(self.new_window, font=("Helvetica", 12))
        self.entry_reference.grid(row=1, column=1, padx=10, pady=5)
        
        self.label_nom = Label(self.new_window, text="Nom:", font=("Helvetica", 12, "bold"), bg="white")
        self.label_nom.grid(row=2, column=0, padx=10, pady=5)
        self.entry_nom = Entry(self.new_window, font=("Helvetica", 12))
        self.entry_nom.grid(row=2, column=1, padx=10, pady=5)
        
        self.label_prix = Label(self.new_window, text="Prix:", font=("Helvetica", 12, "bold"), bg="white")
        self.label_prix.grid(row=3, column=0, padx=10, pady=5)
        self.entry_prix = Entry(self.new_window, font=("Helvetica", 12))
        self.entry_prix.grid(row=3, column=1, padx=10, pady=5)
        
        self.label_quantite = Label(self.new_window, text="Quantité:", font=("Helvetica", 12, "bold"), bg="white")
        self.label_quantite.grid(row=4, column=0, padx=10, pady=5)
        self.entry_quantite = Entry(self.new_window, font=("Helvetica", 12))
        self.entry_quantite.grid(row=4, column=1, padx=10, pady=5)
        
        btn_ajouter = Button(self.new_window, text="Ajouter", font=("Helvetica", 12, "bold"), command=self.ajouter_produit, width=10, height=1, bg='lightgreen')
        btn_ajouter.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    def ajouter_produit(self):
        reference = self.entry_reference.get()
        nom = self.entry_nom.get()
        prix = self.entry_prix.get()
        quantite = self.entry_quantite.get()
        
        if not (reference and nom and prix and quantite):
            tkMessageBox.showwarning("Erreur", "Veuillez remplir toutes les informations du produit.")
            return
        
        produit = f"{reference};{nom};{prix};{quantite}\n"
        
        with open('produits.txt', 'a') as file:
            file.write(produit)
        
        tkMessageBox.showinfo("Succès", "Le produit a été ajouté avec succès.")
        self.new_window.destroy()
        
    def modifier_produit_interface(self):
        self.new_window = Toplevel(self.parent)
        self.new_window.title("Modifier produit")
        self.new_window.geometry('500x150')
        self.new_window.configure(bg="white")
        
        self.label_reference = Label(self.new_window, text="Référence du produit à modifier:", font=("Helvetica", 12, "bold"), bg="white")
        self.label_reference.grid(row=0, column=0, padx=10, pady=5)
        self.entry_reference = Entry(self.new_window, font=("Helvetica", 12))
        self.entry_reference.grid(row=0, column=1, padx=10, pady=5)
        
        btn_verifier = Button(self.new_window, text="Vérifier", font=("Helvetica", 12, "bold"), command=self.verifier_reference, width=10, height=1, bg='lightgreen')
        btn_verifier.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    
    def verifier_reference(self):
        reference = self.entry_reference.get()
    
        with open('produits.txt', 'r') as file:
            lignes = file.readlines()
    
        for ligne in lignes:
            if ligne.split(';')[0] == reference:
                produit_details = ligne.split(';')
                nom = produit_details[1]
                prix = produit_details[2]
                quantite = produit_details[3]
            
                self.new_window.destroy()
            
                self.new_window = Toplevel(self.parent)
                self.new_window.title(f"Modifier produit {reference}")
                self.new_window.geometry('400x300')
                self.new_window.configure(bg="white")
            
                self.label_nom = Label(self.new_window, text="Nom:", font=("Helvetica", 12, "bold"), bg="white")
                self.label_nom.grid(row=0, column=0, padx=10, pady=5)
                self.entry_nom = Entry(self.new_window, font=("Helvetica", 12))
                self.entry_nom.grid(row=0, column=1, padx=10, pady=5)
            
                self.label_prix = Label(self.new_window, text="Prix:", font=("Helvetica", 12, "bold"), bg="white")
                self.label_prix.grid(row=1, column=0, padx=10, pady=5)
                self.entry_prix = Entry(self.new_window, font=("Helvetica", 12))
                self.entry_prix.grid(row=1, column=1, padx=10, pady=5)
            
                self.label_quantite = Label(self.new_window, text="Quantité:", font=("Helvetica", 12, "bold"), bg="white")
                self.label_quantite.grid(row=2, column=0, padx=10, pady=5)
                self.entry_quantite = Entry(self.new_window, font=("Helvetica", 12))
                self.entry_quantite.grid(row=2, column=1, padx=10, pady=5)
            
                self.entry_nom.delete(0, END)
                self.entry_nom.insert(0, nom)
            
                self.entry_prix.delete(0, END)
                self.entry_prix.insert(0, prix)
            
                self.entry_quantite.delete(0, END)
                self.entry_quantite.insert(0, quantite)
            
                btn_modifier = Button(self.new_window, text="Modifier", font=("Helvetica", 12, "bold"), command=lambda: self.modifier_produit(reference), width=10, height=1, bg='lightgreen')
                btn_modifier.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
            
                break
        else:
            tkMessageBox.showerror("Erreur", "Produit non trouvé.")

    def modifier_produit(self, reference):
        nom = self.entry_nom.get()
        prix = self.entry_prix.get()
        quantite = self.entry_quantite.get()
        
        with open('produits.txt', 'r') as file:
            lignes = file.readlines()
        
        for index, ligne in enumerate(lignes):
            if ligne.split(';')[0] == reference:
                lignes[index] = f"{reference};{nom};{prix};{quantite}"
                break
        
        with open('produits.txt', 'w') as file:
            file.writelines(lignes)
        
        tkMessageBox.showinfo("Succès", "Le produit a été modifié avec succès.")
        self.new_window.destroy()

    def supprimer_produit_interface(self):
        self.new_window = Toplevel(self.parent)
        self.new_window.title("Supprimer produit")
        self.new_window.geometry('500x150')
        self.new_window.configure(bg="white")
        
        self.label_reference = Label(self.new_window, text="Référence du produit à supprimer:", font=("Helvetica", 12, "bold"), bg="white")
        self.label_reference.grid(row=0, column=0, padx=10, pady=5)
        self.entry_reference = Entry(self.new_window, font=("Helvetica", 12))
        self.entry_reference.grid(row=0, column=1, padx=10, pady=5)
        
        btn_verifier = Button(self.new_window, text="Vérifier", font=("Helvetica", 12, "bold"), command=self.supprimer_produit, width=10, height=1, bg='lightgreen')
        btn_verifier.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def supprimer_produit(self):
        reference = self.entry_reference.get()

        # Vérifier si la référence existe dans le fichier
        with open('produits.txt', 'r') as file:
            lignes = file.readlines()

        reference_existe = False

        for index, ligne in enumerate(lignes):
            if ligne.split(';')[0] == reference:
                # Produit trouvé, supprimer de la liste
                del lignes[index]
                reference_existe = True
                break

        if reference_existe:
            # Réécrire le fichier sans le produit supprimé
            with open('produits.txt', 'w') as file:
                file.writelines(lignes)
        
            # Afficher un message de succès
            tkMessageBox.showinfo("Succès", f"Le produit {reference} a été supprimé avec succès.")
            self.new_window.destroy()
        else:
            # Produit non trouvé, afficher une erreur
            tkMessageBox.showerror("Erreur", "Le produit spécifié n'a pas été trouvé.")

    def afficher_stock_produits(self):
        with open('produits.txt', 'r') as file:
            contenu = file.read()
        self.afficher_fenetre_stock(contenu)
        
    def afficher_fenetre_stock(self, contenu):
        self.fenetre_stock = Toplevel(self.parent)
        self.fenetre_stock.title("Stock")
        self.fenetre_stock.geometry('300x300')
        self.fenetre_stock.configure(bg="white")
        
        self.label = Label(self.fenetre_stock, text="Liste des produits disponibles", font=("Helvetica", 12, "bold"), bg="white")
        self.label.grid(row=0, column=0, padx=10, pady=5)


        stock_label = Label(self.fenetre_stock, text=contenu, font=("Helvetica", 14), bg="white")
        stock_label.grid(padx=10, pady=20)

if __name__ == "__main__":
    root = Tk()
    root.title("Gestion de stock")
    root.geometry('600x400')
    root.configure(bg="white")
    
    gestion_stock = GestionStock(root)
    
    root.mainloop()
