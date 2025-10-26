from .room import Room
# Use relative import, import Room class from room module

class Player:
    """
    Represent the player in the game.
    """
    def __init__(self,name,starting_room):
        """
        Initialize a player
        :param name: The name of the player.
        :param starting_room: The Room object where the player starts.
        """
        self.name = name
        self.current_room = starting_room

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

