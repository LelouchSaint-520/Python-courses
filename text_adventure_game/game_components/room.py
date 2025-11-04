class Room:
    """
    represent a single location in the game world.
    """
    def __init__(self,name,description):
        """
        Initializes a Room
        :param name: The name of a room.
        :param description: A long description of the room.
        """
        self.name = name
        self.description = description
        # exits is dictionary mapping direction (str) to another Room object.
        self.exits = {} # {key:{value}}
        self.items = [] # <<< add an item object into the list

    def link_room(self,room_to_link,direction,locked = False,key_name = None):
        """
        link this room to another one in a specific direction
        :param key_name: the name of key
        :param locked: the state of door
        :param room_to_link: The room object to link to
        :param direction: the direction of exits (e.g.: "north")
        """
        self.exits[direction] = {'destination':room_to_link,
                                 'locked':locked,
                                 'key_name':key_name # The Name of key is required
                                 }

    def add_item(self,item):
        self.items.append(item)

    def get_full_description(self):
        """
        :return: a full formatted description of a room
        """
        # started with the basic info
        full_desc = f"---{self.name}---\n"
        full_desc += f"{self.description}\n"
        # <<<update the items you add into the room>>>
        if self.items:
            full_desc += "You see here:"
            # combine the items in the list into a string
            item_names = [item.name for item in self.items]
            full_desc += ",".join(item_names)+ ".\n"

        # List the available exits
        # <<< New : Add door info>>>
        available_exits = self.exits.keys()
        full_desc += "Exits: "
        exit_desc = []
        if available_exits:
            for direction, exit_info in self.exits.items():
                if exit_info["locked"]:
                    exit_desc.append(f"{direction}(locked)")
                else:
                    exit_desc.append(direction)
            full_desc += ", ".join(exit_desc) + "\n"
        else:
            full_desc += "There is no obvious exits. \n"
        return full_desc


