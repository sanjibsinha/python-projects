# items.py
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        """Print the item's description."""
        print(f"The {self.name} is here. {self.description}")