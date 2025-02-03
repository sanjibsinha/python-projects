from items import get_item
class Player:
    def __init__(self, name, current_location, inventory=None, health = 100):
        self.name = name
        self.current_location = current_location
        self.inventory = inventory if inventory is not None else []
        self.health = health

    def move(self, direction, locations):
        if direction in self.current_location.connections:
            new_location_name = self.current_location.connections[direction]
            self.current_location = locations[new_location_name] # Update current location
            print(f"You move {direction}.")
            print(self.current_location.description) # Describe the new location
        else:
            print("You can't go that way.")

    def pick_up(self, item_name, locations):
        item = get_item(item_name)
        if item:
          if item_name in self.current_location.items:
              self.inventory.append(item_name)
              self.current_location.remove_item(item_name)
              print(f"You picked up the {item_name}.")
          else:
            print(f"Item '{item_name}' not found in this location.")
        else:
          print(f"Item '{item_name}' does not exist.")


    def use_item(self, item_name):
        item = get_item(item_name)
        if item and item_name in self.inventory:
          if "heal" in item.properties:
            self.health += item.properties["heal"]
            print(f"You used the {item_name} and healed for {item.properties['heal']}. Your health is now {self.health}.")
            self.inventory.remove(item_name) # Item is consumed
          elif "opens" in item.properties:
              # Add logic for opening doors etc.
              print(f"You used the {item_name}.")
          else:
            print(f"You can't use the {item_name} that way.")
        else:
            print(f"You don't have a {item_name} in your inventory.")

# Example player creation (in main.py later)
# player = Player("Adventurer", locations["start"])