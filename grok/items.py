class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# Example items - you can add more or load from a file
items = {
    "key": Item("key", "A rusty key you found in the hall."),
    # Add more items here
}