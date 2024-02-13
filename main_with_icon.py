import customtkinter as ctk
import tkinter as tk
import time


class BananaGame:
    def __init__(self):
        self.bananas = 0
        self.special_bananas = {
            "Étoilée": {"price": 50, "bonus": 5},
            "Turbo": {"price": 100, "bonus": 10},
            "Cristallisée": {"price": 150, "bonus": 15},
            "Arc-en-ciel": {"price": 200, "bonus": 20},
        }

        self.root = tk.Tk()
        self.root.title("Idle Banana Collector")
        self.root.geometry("400x300")

        # Chargement de l'icône de banane
        self.banana_icon = tk.PhotoImage(file="banana_icon.png")

        self.label = ctk.CTkLabel(
            self.root, text=f"Vous avez {self.bananas} bananes.", font=("Helvetica", 14)
        )
        self.label.pack(pady=20)

        self.collect_button = ctk.CTkButton(
            self.root,
            text="Collecter une banane",
            command=self.collect_banana,
            image=self.banana_icon,
            compound="left",
        )
        self.collect_button.pack()

        self.store_button = ctk.CTkButton(
            self.root, text="Aller au magasin", command=self.open_store
        )
        self.store_button.pack()

        self.root.mainloop()

    def collect_banana(self):
        self.bananas += 1
        self.label.configure(text=f"Vous avez {self.bananas} bananes.")

    def open_store(self):
        store_window = tk.Toplevel(self.root)
        store_window.title("Magasin de bananes")

        for banana_type, details in self.special_bananas.items():
            price = details["price"]
            bonus = details["bonus"]
            button_text = f"Acheter {banana_type} ({price} bananes) (+{bonus} par clic)"
            ctk.CTkButton(
                store_window,
                text=button_text,
                command=lambda t=banana_type: self.buy_special_banana(t),
            ).pack()

    def buy_special_banana(self, banana_type):
        if banana_type in self.special_bananas:
            price = self.special_bananas[banana_type]["price"]
            if self.bananas >= price:
                self.bananas -= price
                bonus = self.special_bananas[banana_type]["bonus"]
                self.bananas += bonus
                self.label.configure(text=f"Vous avez acheté une banane {banana_type} !")
            else:
                self.label.configure(text="Pas assez de bananes pour acheter cela.")
        else:
            self.label.configure(text="Type de banane spécial invalide.")


if __name__ == "__main__":
    BananaGame()
