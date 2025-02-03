from locations import locations, get_location
from items import get_item
from player import Player

# Initialize the game
player_name = input("Enter your name: ")
player = Player(player_name, locations["start"])

print(f"Welcome, {player.name}!")
print(player.current_location.description)

while True:
    command = input("> ").lower()  # Get player input

    if command == "quit":
        break  # Exit the game

    parts = command.split() # Split the command into words
    action = parts[0] # First word is the action

    if action == "move":
        if len(parts) > 1:
            direction = parts[1]
            player.move(direction, locations)
        else:
            print("Move where?")
    elif action == "pickup":
        if len(parts) > 1:
          item_name = parts[1]
          player.pick_up(item_name, locations)
        else:
          print("Pickup what?")
    elif action == "use":
        if len(parts) > 1:
          item_name = parts[1]
          player.use_item(item_name)
        else:
          print("Use what?")
    elif command == "inventory":
        print("Inventory:", player.inventory)
    elif command == "help":
        print("Available commands: move [direction], pickup [item], use [item], inventory, quit, help")
    else:
        print("I don't understand that command.")

print("Thanks for playing!")