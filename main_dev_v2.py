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

    def collect_banana(self):
        collected_banana = random.choice(self.banana_types)
        self.banana_count += 1
        self.update_inventory_display(collected_banana)

    def update_inventory_display(self, collected_banana):
        self.inventory_display.config(
            text=f"Bananas: {self.banana_count} ({collected_banana})"
        )

    def open_shop(self):
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Banana Shop")
        shop_window.configure(bg="black")

        for item, details in self.shop_items.items():
            item_frame = tk.Frame(shop_window, bg="black")
            item_frame.pack(pady=10)
            item_label = tk.Label(
                item_frame,
                text=f"{item} (+{details['bonus']} per click) - ${details['cost']}",
                fg="white",
                bg="black",
                font=("Helvetica", 10),
            )
            item_label.pack()
            buy_button = tk.Button(
                item_frame,
                text="Buy",
                command=lambda i=item: self.buy_item(i),
                bg="orange",
                fg="white",
            )
            buy_button.pack()

    def buy_item(self, item):
        if item in self.shop_items:
            cost = self.shop_items[item]["cost"]
            if self.banana_count >= cost:
                self.banana_count -= cost
                bonus = self.shop_items[item]["bonus"]
                self.update_inventory_display(f"{item} (+{bonus} per click)")
            else:
                print("Not enough bananas!")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = BananaIdleGame()
    game.run()
