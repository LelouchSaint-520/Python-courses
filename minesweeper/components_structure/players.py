#from .boom import Boom
from .map import Map
#from .medicine import Medicine

class Player:
    def __init__(self,name,starting_area:Map,health = 100):
        self.name = name
        self.current_area = starting_area
        self.health = health
        self.inventory= {} #{"name":amount}

    """
    def _is_in_inventory(self,item_name):
        for item_obj in self.inventory.keys():
            if item_obj.name.lower() == item_name.lower():
                return item_obj
        return None
    """

    def _is_in_area(self,item_name):
        for item_obj in self.current_area.items.keys():
            if item_obj.name.lower() == item_name.lower():
                return item_obj
        return None

    def _has_goods(self,item_name):
        for item_obj in self.inventory.keys():
            if item_obj.name.lower() == item_name.lower():
                return item_obj
        return None

    def display_inventory(self):
        if self.inventory:
            inventory_dis = []
            for key,value in self.inventory.items():
                inventory_dis.append([key.name,value])
            print(f"Your inventory has {inventory_dis}")
        else:
            print(" Your inventory is empty!")

    def take_medicine(self,pill_name,num:int = 1):
        pill_obj = self._has_goods(pill_name)
        if pill_obj is None:
            print(f"You don't have any {pill_name} in your inventory! \n")
            return
        elif self.inventory[pill_obj] >= num:
                self.health += pill_obj.cure * num
                self.inventory[pill_obj] -= num
        else:
            print(f"the amount of {pill_name} is not enough!\n")
            return
    # To remember: The type of variable must be consistent! pill_name is a string,so it cannot to index a dict in a father dict.


    def collect_item(self,collect_name,num = 1):
        item_obj = self._is_in_area(collect_name)
        if not item_obj:
            print(f"There is no {collect_name} in {self.current_area.name}") # 不要忘了area的属性，他是一个对象，不是字符串
        elif self.current_area.items[item_obj] < num:
            print(f"The amount of {collect_name} is not enough! \n")

        elif not self._has_goods(collect_name):
            self.inventory[item_obj] = num
            self.current_area.items[item_obj] -= num
        else:
            self.inventory[item_obj] += num
            self.current_area.items[item_obj] -= num


    def move_forward(self,direction):
        if direction in self.current_area.exits:
            self.current_area = self.current_area.exits[direction]
            print(f"You have moved {direction}\n")
            if self.current_area.booms:
                for key, value in self.current_area.booms.items():
                    self.health -= value * key.damage
        else:
            print(f"You can't go {direction}\n")















