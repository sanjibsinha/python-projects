class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []  # List of items in the room

    def describe(self):
        """Print the room description."""
        print(f"You are in {self.name}. {self.description}")

    def add_item(self, item):
        """Add an item to the room."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the room."""
        if item in self.items:
            self.items.remove(item)
        else:
            print(f"{item.name} is not in this room.")