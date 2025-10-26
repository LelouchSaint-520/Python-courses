class Room:
    def __init__(self,name,description):
        """
        Initializes a Room
        :param name: The name of a room.
        :param description: A long description of the room.
        """
        self.name = name
        self.description = description
        # exits is dictionary mapping direction (str) to another Room object.
        self.exits = {}

    def link_room(self,room_to_link,direction):
        """
        link this room to another one in a specific direction
        :param room_to_link: The room object to link to
        :param direction: the direction of exits (e.g.: "north")
        :return:
        """
        self.exits[direction] = room_to_link

    def get_full_description(self):
        """
        :return: a full formatted description of a room
        """
        # started with the basic info
        full_desc = f"---{self.name}---\n"
        full_desc += f"{self.description}\n"

        # List the available exits
        available_exits = self.exits.keys()
        if available_exits:
            full_desc += f"Exits {",".join(available_exits)}\n "
        else:
            full_desc += "There is no obvious exits. \n"
        return full_desc


