class Item:
    """
    Represent an item that can be found in a room or carried by the player.
    """
    def __init__(self,name,description,is_takable = True):
        """
        Initialize an Item
        :param name: The name of the item (e.g.:"key")
        :param description: A short description of the item.
        """
        self.name = name
        self.description = description
        self.is_takable = is_takable