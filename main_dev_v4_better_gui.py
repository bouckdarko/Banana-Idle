import tkinter as tk
import customtkinter as ctk


class JeuBananes:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu des Bananes")
        self.root.geometry("800x600")

        # Initialisation du compteur de bananes
        self.banane_count = 0

        # Initialisation des bonus par clic
        self.bonus_par_clic = 1

        # Création du bouton de collecte
        self.bouton_collecte = ctk.CTkButton(
            self.root, text="Collecter une banane", command=self.collecter_banane
        )
        self.bouton_collecte.pack(pady=20)

        # Création de la boutique
        self.boutique_frame = ctk.CTkFrame(self.root)
        self.boutique_frame.pack(side="right", fill="y")

        # Exemple d'améliorations disponibles à l'achat
        self.ameliorations = {
            "Banane dorée": {"prix": 10, "bonus": 2},
            "Banane géante": {"prix": 20, "bonus": 5},
            "Banane magique": {"prix": 50, "bonus": 10},
        }

        # Création des boutons pour chaque amélioration
        for nom, details in self.ameliorations.items():
            bouton_amelioration = ctk.CTkButton(
                self.boutique_frame,
                text=f"Acheter {nom} ({details['prix']} bananes)",
                command=lambda nom=nom, prix=details["prix"], bonus=details[
                    "bonus"
                ]: self.acheter_amelioration(nom, prix, bonus),
            )
            bouton_amelioration.pack()

            # Bouton pour acheter 10 améliorations
            bouton_acheter_10 = ctk.CTkButton(
                self.boutique_frame,
                text=f"Acheter 10 ({details['prix']*10} bananes)",
                command=lambda nom=nom, prix=details["prix"], bonus=details[
                    "bonus"
                ]: self.acheter_amelioration(nom, prix * 10, bonus * 10),
            )
            bouton_acheter_10.pack()

            # Bouton pour acheter 50 améliorations
            bouton_acheter_50 = ctk.CTkButton(
                self.boutique_frame,
                text=f"Acheter 50 ({details['prix']*50} bananes)",
                command=lambda nom=nom, prix=details["prix"], bonus=details[
                    "bonus"
                ]: self.acheter_amelioration(nom, prix * 50, bonus * 50),
            )
            bouton_acheter_50.pack()

            # Bouton pour acheter 500 améliorations
            bouton_acheter_50 = ctk.CTkButton(
                self.boutique_frame,
                text=f"Acheter 50 ({details['prix']*50} bananes)",
                command=lambda nom=nom, prix=details["prix"], bonus=details[
                    "bonus"
                ]: self.acheter_amelioration(nom, prix * 500, bonus * 500),
            )
            bouton_acheter_500.pack()

        # Création des labels pour chaque amélioration
        for nom, details in self.ameliorations.items():
            label_amelioration = ctk.CTkLabel(
                self.boutique_frame, text=f"{nom} ({details['prix']} bananes)"
            )
            label_amelioration.pack()

        # Affichage du nombre de bananes collectées et du bonus par clic
        self.label_bananes = ctk.CTkLabel(
            self.root, text=f"Bananes collectées : {self.banane_count}"
        )
        self.label_bananes.pack()
        self.label_bonus = ctk.CTkLabel(
            self.root, text=f"Bonus par clic : {self.bonus_par_clic}"
        )
        self.label_bonus.pack()

    def collecter_banane(self):
        self.banane_count += self.bonus_par_clic
        self.label_bananes.configure(text=f"Bananes collectées : {self.banane_count}")

    def acheter_amelioration(self, nom, prix, bonus):
        if self.banane_count >= prix:
            self.banane_count -= prix
            self.bonus_par_clic += bonus
            self.label_bananes.configure(
                text=f"Bananes collectées : {self.banane_count}"
            )
            self.label_bonus.configure(text=f"Bonus par clic : {self.bonus_par_clic}")
        else:
            print("Pas assez de bananes pour acheter cette amélioration !")

    def calculer_max_achat(self, prix):
        return self.banane_count // prix


if __name__ == "__main__":
    root = tk.Tk()
    app = JeuBananes(root)
    root.mainloop()
