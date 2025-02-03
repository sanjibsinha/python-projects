# import statements # (we'll use these later for our modules)
import world
import player
import items

def play():
    # Initialize game
    current_room = "hall"
    player = Player()
    
    while True:
        # Display room description
        room = world.rooms[current_room]
        print(room["description"])
        
        # Get user command
        command = input("What do you want to do? ").lower().split(maxsplit=1)
        
        # Process command
        action = command[0]
        
        if action == "go" and len(command) > 1:
            direction = command[1]
            next_room = room["exits"].get(direction)
            if next_room:
                current_room = next_room
            else:
                print("You can't go that way!")
        elif action == "look":
            if len(command) > 1:
                item = room["items"].get(command[1])
                if item:
                    print(item["description"])
                else:
                    print("You don't see that here.")
            else:
                print(room["description"])
        elif action == "quit":
            break
        else:
            print("I don't understand that command.")

class Player:
    def __init__(self):
        self.inventory = []

# Main execution
if __name__ == "__main__":
    play()