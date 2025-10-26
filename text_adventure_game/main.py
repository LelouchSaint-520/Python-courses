from game_components.room import Room
from game_components.player import Player

def setup_world():
    """Creates all the rooms and links them together."""
    print("Setting up the world...")

    #1. Create room instances
    kitchen = Room("Kitchen","A cluttered kitchen with dirty dishes piled up.")
    living_room = Room("Living Room","A dusty living room with flickering TV.")
    garden = Room("Garden","An overgrown garden with a mysterious-looking statue.")
    bedroom = Room("Bedroom","A small bedroom with an unmade bed.")
    dining_room = Room("dining_room","A small room filled with table and chairs for meals")
    shack = Room("shack","A broken shack beside garden that is abandoned")
    attic = Room("attic","A loft upon the bedroom")

    # 2. Link the rooms together
    kitchen.link_room(living_room,"south")
    living_room.link_room(kitchen,"north")
    living_room.link_room(garden,"east")
    garden.link_room(living_room, "west")
    bedroom.link_room(living_room, "down")
    living_room.link_room(bedroom,"up")
    dining_room.link_room(kitchen,"west")
    kitchen.link_room(dining_room,"east")
    shack.link_room(garden,"east")
    garden.link_room(shack,"west")
    attic.link_room(bedroom,"upstairs")
    bedroom.link_room(attic,"downstairs")

    print("World setup complete!")
    return kitchen #Return the starting room.

def game_loop(player):
    """The main loop of the game."""
    print("Welcome to the Adventure Game!")
    print("Type 'quit' to exit.")
    while True:
        # Print the description of the current room
        print("\n" + player.current_room.get_full_description())

        # Get user command
        command = input("> ").lower().strip()


        match command:
            case "look":
                print("\n" + player.current_room.get_full_description()) # the method of class should be added () after its name.
                break
            case "quit":
                print("Thanks for playing!")
                break
            case _:
                player.move(command)


        """
        if command == "look":
            print("\n" + player.current_room.get_full_description()) # the method of class should be add () after its name.
            break

        # For today, we only implement a 'quit' command
        if command == "quit":
            print("Thanks for playing!")
            break

        # --- core change:  the command to the player object to implement.
        player.move(command)
        """

# --- Main execution ---
if __name__ == "__main__":
    starting_room = setup_world()
    player = Player("Hero", starting_room)
    game_loop(player)
