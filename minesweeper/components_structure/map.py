# from .boom import Boom
class Map:
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = {}
        self.booms = {}


    def map_to_linked(self,area,direction:str):
        self.exits[direction] = area

    def add_item(self,item_obj,amount):
        self.items[item_obj] = amount

    def add_boom(self,boom_obj,amount):

        self.booms[boom_obj] = amount


    def get_map_info(self):
        """Title of description"""
        aa = len(self.description)-len(self.name) // 2
        _map_info = f"{aa*"-"} {self.name} {aa*"-"} \n"
        _map_info += f" {self.description} \n"

        """Boom information"""
        _map_info += "Boom:\n"
        for key, value in self.booms.items():
            _map_info += f"     {key.name} : {value}\n"

        """description of exits:"""
        exits_list = []
        for key,value in self.exits.items():
            exits_list.append(key)
        exits_desc = ",".join(exits_list)
        _map_info += f"{exits_desc}\n"

        """description of items"""

        if self.items:
            for key,value in self.items.items():
                _map_info += f"{key.name} : {value}\n"
        return _map_info




