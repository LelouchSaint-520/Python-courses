from components_structure.boom import Boom
from components_structure.players import Player
from components_structure.map import Map
from components_structure.medicine import Medicine
from components_structure.sweeper import Sweeper

def create_world():
    print("The world is setting up now...")
    # 1. creat map
    area1 = Map("area1","safe area")
    area2 = Map("area2","safety!")
    area3 = Map("area3","rare")
    area4 = Map("area4","Dangerous!")
    area5 = Map("area5","Dangerous!")

    area1.map_to_linked(area2,"south")
    area2.map_to_linked(area1,"north")

    area2.map_to_linked(area3,"south")
    area3.map_to_linked(area2,"north")

    area3.map_to_linked(area4,"south")
    area4.map_to_linked(area3,"north")

    area4.map_to_linked(area5,"south")
    area5.map_to_linked(area4,"north")

    # 2. add boom eg: boom = num
    boom_1 = Boom("boom1",1)
    boom_2 = Boom("boom2",2)
    boom_3 = Boom("boom3",3)
    boom_4 = Boom("boom4",4)
    boom_5 = Boom("boom5",5)

    area1.add_boom(boom_1,5)
    area2.add_boom(boom_2,10)
    area3.add_boom(boom_3,15)
    area4.add_boom(boom_4,20)
    area5.add_boom(boom_5,25)

    # 3. add medicine
    medicine_1 = Medicine("medicine1",5)
    medicine_2 = Medicine("medicine2", 10)
    medicine_3 = Medicine("medicine3", 15)
    medicine_4 = Medicine("medicine4", 20)
    medicine_5 = Medicine("medicine5", 25)

    area1.add_item(medicine_1,10)
    area2.add_item(medicine_2,10)
    area3.add_item(medicine_3,10)
    area4.add_item(medicine_4,10)
    area5.add_item(medicine_5,10)

    # 4. add sweeper and key
    sweeper_1 = Sweeper("sweeper1",5)
    sweeper_2 = Sweeper("sweeper2",10)

    area1.add_item(sweeper_1, 10)
    area3.add_item(sweeper_2, 20)

    print("The world is created!")
    return area1, area5

def game_loop(player,win_map):
    print("Welcome to join game!")
    print("type 'quit' to exit")

    while True:
        print(player.current_area.get_map_info())
        print(f"Your health is {player.health}")

        if player.health <= 0:
            print("You are died!")
            break
        elif player.current_area == win_map:
            print("You win the game!")
            break

        command = input("Please type the command:").lower().strip().split()
        command_distinguish = command[0]

        if command_distinguish == "quit":
            break
        elif command_distinguish == "take":
            player.take_medicine(command[1],int(command[2])) # 通过split()生成的数字格式为str，不能直接使用！
        elif command_distinguish == "collect":
            if len(command) > 2:
                player.collect_item(command[1],int(command[2]))
            else:
                print("Collect what?")
        elif command_distinguish == "i":
            player.display_inventory()
        else:
            player.move_forward(command_distinguish)




if __name__ == "__main__":
    starting_area,w_area = create_world()
    player_1 = Player("FireMan",starting_area)
    game_loop(player_1,w_area)





