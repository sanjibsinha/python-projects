# game.py
from player import Player
from room import Room
from items import Item

def main():
    # Create items
    sword = Item("sword", "A shiny sword with a sharp edge.")
    shield = Item("shield", "A sturdy shield made of iron.")

    # Create rooms
    kitchen = Room("Kitchen", "This is a cozy kitchen with a warm stove.")
    living_room = Room("Living Room", "A spacious living room with a fireplace.")

    # Add items to rooms
    kitchen.add_item(sword)
    living_room.add_item(shield)

    # Create player
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # Start in the kitchen
    player.move(kitchen)

    # Game loop
    while True:
        player.current_room.describe()

        # Show items in the current room
        if player.current_room.items:
            print("Items here:")
            for item in player.current_room.items:
                print(f"- {item.name}: {item.description}")

        action = input("\nWhat do you want to do? (move, take, drop, quit): ").lower()

        if action == "quit":
            print("Goodbye!")
            break

        elif action == "move":
            if player.current_room == kitchen:
                player.move(living_room)
            else:
                player.move(kitchen)

        elif action == "take":
            item_name = input("Enter the name of the item you want to take: ").lower()
            item_found = False
            for item in player.current_room.items:
                if item.name.lower() == item_name:
                    player.take(item)
                    player.current_room.remove_item(item)
                    item_found = True
                    break
            if not item_found:
                print(f"There is no {item_name} here.")

        elif action == "drop":
            item_name = input("Enter the name of the item you want to drop: ").lower()
            item_found = False
            for item in player.inventory:
                if item.name.lower() == item_name:
                    player.drop(item)
                    player.current_room.add_item(item)
                    item_found = True
                    break
            if not item_found:
                print(f"You don't have {item_name} in your inventory.")

        else:
            print("Invalid action. Try again.")

if __name__ == "__main__":
    main()