rooms = {
    "hall": {
        "description": "You're in a dark hall. There are doors to the north and east.",
        "exits": {"north": "kitchen", "east": "living_room"},
        "items": {
            "key": {"description": "A rusty key lies on the floor."}
        }
    },
    "kitchen": {
        "description": "A clean kitchen with an exit to the south.",
        "exits": {"south": "hall"},
        "items": {}
    },
    # Add more rooms here
}