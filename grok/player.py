class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        if self.inventory:
            return ", ".join(self.inventory)
        else:
            return "Your inventory is empty."