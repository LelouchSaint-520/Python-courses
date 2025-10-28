from .room import Room
# Use relative import, import Room class from room module
# from .item import Item


class Player:
    """
    Represent the player in the game.
    """
    def __init__(self,name,starting_room:Room):
        """
        Initialize a player
        :param name: The name of the player.
        :param starting_room: The Room object where the player starts.
        """
        self.name = name
        self.current_room = starting_room
        self.inventory = [] # <<< New: inventory of player

    def move(self, direction):
        """
        Moves the player in a given direction, if the exit exists.
        :param direction: The direction to move in (e.g., "north")
        """
        # Check if the requested direction is a valid exit from current room
        if direction in self.current_room.exits: #Notion: exits is a dict! use [] to index and "in exits()" is not a correct method.
            #If it is, update the player's current room to the new room
            self.current_room = self.current_room.exits[direction]
            print(f"You move {direction}.")
        else:
            print("You can't go that way.")

    def take_item(self, item_name):
        """Tries to pick up an item from the current room."""
        # iterate the items in the room
        for item in self.current_room.items:
            if item.name.lower() == item_name.lower():
                self.current_room.items.remove(item)
                self.inventory.append(item)
                print(f"You picked up the {item.name}.")
                return
        print(f"There is no {item_name} here.")

    def drop_item(self,item_name):
        """Tries to drop the items from the inventory of player's"""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                self.current_room.items.append(item)
                print(f"You have dropped the {item.name}.")
                return
        print(f"There is no {item_name} in your inventory here.")

    def show_inventory(self):
        """Prints out the items in the player's inventory."""
        if not self.inventory:
            print("Your inventory is empty")
        else:
            item_names = [item.name for item in self.inventory]
            print(f"You are carrying: \n{','.join(item_names)}")
