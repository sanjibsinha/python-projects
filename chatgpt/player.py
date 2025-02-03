class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = None  # Start with no room
        self.inventory = []  # List of items player has

    def move(self, room):
        """Move the player to a new room."""
        self.current_room = room
        print(f"{self.name} moves to {room.name}.")

    def take(self, item):
        """Pick up an item and add it to inventory."""
        self.inventory.append(item)
        print(f"{self.name} takes the {item.name}.")

    def drop(self, item):
        """Drop an item from inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{self.name} drops the {item.name}.")
        else:
            print(f"{item.name} is not in your inventory.")