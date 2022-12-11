# Delani Murphy


rooms = {
        'Bedroom': {'East': 'Bathroom', 'North': 'Hallway', 'Item': 'Pistol'},
        'Bathroom': {'West': 'Bedroom', 'Item': 'Ritual Dagger'},
        'Hallway': {'North': 'Living Room', 'South': 'Bedroom', 'East': 'Study', 'West': 'Kitchen'},
        'Study': {'West': 'Hallway', 'Item': 'Silver Bullets'},
        'Kitchen': {'North': 'Dining Room', 'South': 'Garage', 'East': 'Hallway', 'Item': 'Salt'},
        'Garage': {'North': 'Kitchen', 'Item': 'Lighter'},
        'Dining Room': {'South': 'Kitchen', 'East': 'Living Room', 'Item': 'Flashlight'},
        'Living Room': {'South': 'Hallway', 'West': 'Dining Room', 'Item': 'Monster'} #Villian Room

    }

startingRoom = 'Bedroom' #player will start in bedroom


def instructions(): #show instructions to player
    print('*' * 40)
    print('*' * 5, "Monster Hunter Survival Game", '*' * 5)
    print('*' * 40)
    print(">> Collect all 6 items before encountering the monster, or you die! <<")
    print(">> Use commands 'go [North, South, East, West]' to navigate rooms. (example: go north) <<")
    print(">> Use command [X] to exit. <<")
    print(">> Add item to inventory: get 'item name' (example: get pistol) <<")


instructions()

def get_new_room(startingRoom, direction):
    newRoom = startingRoom
    for i in rooms:
        if i == startingRoom:
            if direction in rooms[i]:
                newRoom = rooms[i][direction]
    return newRoom


Inventory = []
current_room = startingRoom
while True:
    print('You are in the', current_room)
    print('Inventory:', Inventory)

    try:
        print('You see an item: ', rooms[current_room]["Item"])
    except:
        print("There are no items here.")

    prompt = input(">> What would you like to do?: ").split(' ')
    direction = prompt[0].lower()
    action = " ".join(prompt[1:]).lower()


    if direction == 'x':
        print("Thanks for playing!") #end program
        break
    elif direction == "get":
        if "Item" in rooms[current_room].keys() and action == rooms[current_room]["Item"].lower():
            Inventory.append(rooms[current_room]["Item"])
            rooms[current_room].pop("Item")
        else:
            print("You can't do that!")
    elif direction == "go":
        new_room = get_new_room(current_room, action.capitalize())
        if new_room == current_room:
            print("You can't go that way!")
        try:
            if rooms[new_room]["Item"] == "Monster":
                has_all_items = True
                for i in rooms:
                    if "Item" in rooms[i].keys():
                        if rooms[i]["Item"] != "Monster":
                            has_all_items = False
                            break
                if has_all_items == True:
                    print("Congratulations! You have defeated the monster!")
                else:
                    print("You did not have the required items to fight the monster.")
                    print("You are dead!")
                print("Thank you for playing!")
                break
        except KeyError:
            pass
        current_room = new_room
    else:
        print("That is not a valid command.")




