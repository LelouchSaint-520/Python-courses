from game_components.room import Room
from game_components.player import Player
from game_components.item import Item

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

    # 3. create item instance
    key = Item("key","A small, rusty key.")
    sword = Item("sword","A short sword, it looks sharp.")
    note = Item("note","A crumpled piece of paper.")

    # 4.New: put the items into the rooms
    kitchen.add_item(note)
    garden.add_item(key)
    living_room.add_item(sword)


    print("World setup complete!")
    return kitchen #Return the starting room.

def game_loop(player):
    """The main loop of the game."""
    print("Welcome to the Adventure Game!")
    print("Type 'quit' to exit.")
    print("Commands:'quit','inventory','<direction>','take<item>','drop<item>'")
    while True:
        # Print the description of the current room
        print("\n" + player.current_room.get_full_description())

        # Get user command
        command_input = input("> ").lower().strip()
        parts = command_input.split()
        command = parts[0]

        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "inventory" or command =="i":
            player.show_inventory()
        elif command =="take":
            if len(parts) > 1:
                item_name = " ".join(parts[1:])
                player.take_item(item_name)
            else:
                print("Take what?")
        elif command == "drop":
            if len(parts)>1:
                item_name = " ".join(parts[1:])
                player.drop_item(item_name)
            else:
                print("Drop what?")

        #elif command == "look" :
        #    print("\n" + player.current_room.get_full_description())  # the method of class should be added () after its name.


        else:
            player.move(command)


        """
        # For today, we only implement a 'quit' command
        # --- core change:  the command to the player object to implement.
        player.move(command)  
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

# --- Main execution ---
if __name__ == "__main__":
    starting_room = setup_world()
    player = Player("Hero", starting_room)
    game_loop(player)
