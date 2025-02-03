class Location:
    def __init__(self, name, description, connections, items=None):
        self.name = name
        self.description = description
        self.connections = connections  # Dictionary: direction -> location name
        self.items = items if items is not None else [] # Initialize items list

    def add_item(self, item_name):
        self.items.append(item_name)

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
        else:
            print(f"Item '{item_name}' not found in this location.")


# Example locations (you'll expand this)
locations = {
    "start": Location("The Crossroads", "You stand at a crossroads. Paths lead north, east, and west.",
                       {"north": "forest", "east": "village", "west": "cave"}, ["rusty_key"]),
    "forest": Location("The Dark Forest", "The trees are thick and the air is still.",
                        {"south": "start"}, ["potion"]),
    "village": Location("Quiet Village", "A peaceful village with friendly inhabitants.",
                         {"west": "start", "north":"shop"},[]),
    "cave": Location("Gloomy Cave", "A dark and damp cave. You hear dripping water.",
                     {"east": "start"}, ["torch"]),
    "shop": Location("General Store", "Welcome to the General Store, what would you like to buy?",
                     {"south": "village"}, [])
}

# Function to get a location object by name
def get_location(location_name):
  return locations.get(location_name) # .get() is safer than [] if key might not exist