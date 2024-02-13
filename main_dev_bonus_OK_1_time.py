import tkinter as tk
import random


class BananaIdleGame:
    def __init__(self):
        self.banana_count = 0
        self.banana_types = ["Yellow", "Red", "Green", "Blue"]
        self.root = tk.Tk()
        self.root.title("Banana Idle Game")
        self.root.configure(bg="black")

        # Inventory display
        self.inventory_frame = tk.Frame(self.root, bg="black")
        self.inventory_frame.pack(side="right", padx=20, pady=20)
        self.inventory_label = tk.Label(
            self.inventory_frame,
            text="Inventory:",
            fg="white",
            bg="black",
            font=("Helvetica", 12),
        )
        self.inventory_label.pack()
        self.inventory_display = tk.Label(
            self.inventory_frame,
            text="",
            fg="white",
            bg="black",
            font=("Helvetica", 10),
        )
        self.inventory_display.pack()

        # Banana collection button
        self.banana_button = tk.Button(
            self.root,
            text="Collect Banana",
            command=self.collect_banana,
            bg="green",
            fg="white",
        )
        self.banana_button.pack(pady=10)

        # Shop button
        self.shop_button = tk.Button(
            self.root, text="Open Shop", command=self.open_shop, bg="blue", fg="white"
        )
        self.shop_button.pack(pady=10)

        # Initialize shop items
        self.shop_items = {
            "Banana Farm": {"cost": 10, "bonus": 1},
            "Golden Banana": {"cost": 50, "bonus": 5},
            "Banana Boost": {"cost": 100, "bonus": 10},
        }

        # Start the main event loop
        self.root.mainloop()

    def collect_banana(self):
        collected_banana = random.choice(self.banana_types)
        self.banana_count += 1
        self.update_inventory_display(collected_banana)

    def update_inventory_display(self, collected_banana):
        self.inventory_display.config(
            text=f"Bananas: {self.banana_count} ({collected_banana})"
        )

    def open_shop(self):
        # Crée une fenêtre de magasin
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Banana Shop")
        shop_window.configure(bg="white")

        # Affiche les articles disponibles dans le magasin
        for item_name, item_info in self.shop_items.items():
            item_cost = item_info["cost"]
            item_bonus = item_info["bonus"]

            # Crée un bouton pour chaque article
            item_button = tk.Button(
                shop_window,
                text=f"{item_name} ({item_cost} bananas)",
                command=lambda name=item_name, cost=item_cost: self.buy_item(name, cost),
                bg="yellow",
                fg="black",
            )
            item_button.pack(pady=10)

        # Ajoute un bouton pour fermer la fenêtre du magasin
        close_button = tk.Button(
            shop_window,
            text="Close",
            command=shop_window.destroy,
            bg="red",
            fg="white",
        )
        close_button.pack(pady=20)

    def buy_item(self, item_name, item_cost):
        # Vérifie si le joueur a suffisamment de bananes pour acheter l'article
        if self.banana_count >= item_cost:
            # Déduit le coût de l'article du total de bananes
            self.banana_count -= item_cost
            # Augmente le taux de collecte de bananes par clic
            self.banana_button.config(command=self.collect_banana_with_bonus)
            # Met à jour l'affichage de l'inventaire
            self.update_inventory_display(f"Purchased {item_name}!")
        else:
            # Affiche un message si le joueur n'a pas assez de bananes
            self.update_inventory_display("Not enough bananas!")

    def collect_banana_with_bonus(self):
        # Fonction appelée lorsque le joueur clique sur le bouton de collecte
        # Ajoute le bonus d'amélioration au nombre de bananes collectées
        collected_banana = random.choice(self.banana_types)
        self.banana_count += self.shop_items["Banana Boost"]["bonus"]
        self.update_inventory_display(collected_banana)



if __name__ == "__main__":
    game = BananaIdleGame()
