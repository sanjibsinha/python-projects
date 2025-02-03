class Item:
    def __init__(self, name, description, properties=None):
        self.name = name
        self.description = description
        self.properties = properties if properties is not None else {} # Dictionary for item properties

# Example items
items = {
    "rusty_key": Item("Rusty Key", "An old, rusty key. It might open something.", {"opens": "cave_door"}),
    "potion": Item("Healing Potion", "A shimmering potion that restores health.", {"heal": 20}),
    "torch": Item("Torch", "A simple torch. It might light up dark places.", {"light": True})
}

def get_item(item_name):
    return items.get(item_name)