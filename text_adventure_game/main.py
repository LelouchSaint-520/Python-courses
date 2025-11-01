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
    treasure = Room("Treasure","A small, dark room filled with treasure!") #victory condition

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
    garden.link_room(treasure,"south",locked=True,key_name="treasure key")
    treasure.link_room(garden,"north")

    # 3. create item instance
    key = Item("key","A small, rusty key.")
    sword = Item("sword","A short sword, it looks sharp.")
    note = Item("note","A crumpled piece of paper.")
    treasure_key = Item("treasure key","A heavy, ornate golden key.")

    # 4.New: put the items into the rooms
    kitchen.add_item(note)
    garden.add_item(treasure_key)
    living_room.add_item(sword)


    print("World setup complete!")
    return kitchen, treasure #Return the starting room.

def game_loop(player, win_room):
    """The main loop of the game."""
    print("Welcome to the Adventure Game!")
    print("Find the treasure to win!")
    print("Type 'quit' to exit.")
    print("Commands:'quit','inventory','<direction>','take<item>','drop<item>'")
    while True:
        # Print the description of the current room
        print("\n" + player.current_room.get_full_description())

        if player.current_room == win_room:
            print("\n" ,  win_room.get_full_description)
            print("Congratulations! You found the treasury and won the game!")
            break

        # Get user command
        command_input = input("> ").lower().strip()
        parts = command_input.split()
        command = parts[0]

        if command == "quit":
            print("Thanks for playing!")
            break
        elif command in ("inventory","i"):  # command == "inventory" or command =="i":
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
    starting_room, winning_room = setup_world()
    game_player = Player("Hero", starting_room)
    game_loop(game_player,winning_room)
