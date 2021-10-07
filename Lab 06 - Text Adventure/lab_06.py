class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []
    # Greenhouse
    room = Room("You are in the greenhouse!\nHere we grow beautiful tropical trees!\nThere are rooms to the north and east.", 1, None, 8, None)
    room_list.append(room)
    # Living Room
    room = Room("You are in the living room!\nThere is a nice TV in here!\nThere are rooms to the north, east, and west.", 7, None, 2, 0)
    room_list.append(room)
    # Grand Entrance
    room = Room("You are now in the grand entrance of the house!\nThere is a beautiful chandelier above!\nThere are rooms to the north, east, and west.", 6, None, 3, 1)
    room_list.append(room)
    # Piano Room
    room = Room("You are now in the piano room!\nMusic is played here all throughout the day!\nThere are rooms to the north, east, and west.", 5, None, 18, 2)
    room_list.append(room)
    # Bonsai Room
    room = Room("You are now in the bonsai room!\nTrees are sculpted to perfection in here!\nThere are rooms to the north and west.", 4, None, 3, None)
    room_list.append(room)
    # Bedroom 1
    room = Room("You are now in the first bedroom!\nThis room is space themed!\nThere are rooms to the west and south, and a passage to the north. ", 20, 18, None, 5)
    room_list.append(room)
    # Bathroom 1
    room = Room("You are now in the first bathroom!\nThis is a full bath with a rain shower!\nThere are rooms to the east, west, and south, and a passage to the north.", 19, 3, 4, 6)
    room_list.append(room)
    # Family Room
    room = Room("You are now in the family room!\nThis room is full of laughter and couches!\nThere are rooms to the east, west, and south, and a passage to the north.", 11, 2, 5, 7)
    room_list.append(room)
    # Bedroom 2
    room = Room("You are now in the second bedroom!\nThis room is covered head-to-toe in pink!\nThere are rooms to the north, south, east, and west", 10, 1, 6, 8)
    room_list.append(room)
    # Master Bedroom
    room = Room("You are now in the master bedroom!\nThis is the biggest room in the house!\nThere are rooms to the north east, and south and a surprise to the west.", 21, 0, 7, 9)
    room_list.append(room)
    # Balcony
    room = Room("You are now on the Balcony!\nThere is a beautiful view of the Rocky Mountains!\nThere is only a room to the east.", None, None, 8, None)
    room_list.append(room)
    # Master Bathroom
    room = Room("You are now in the master bathroom!\nThis is the biggest bathroom in the house!\nThere are rooms to the north east, and south.", 17, 8, 10, None)
    room_list.append(room)
    # Library
    room = Room("You are now in the library!\nThere are almost 2000 books located here!\nThere are rooms to the north, south, and west and a passage to the east.", 16, 11, 10, 21)
    room_list.append(room)
    # Hall 1
    room = Room("You have now entered the first hall!\nThere are rooms to the north, west, and south and a passage to the east.", 12, 6, 19, 10)
    room_list.append(room)
    # Hall 2
    room = Room("You have now entered the second hall!\nThere are rooms to the north, and south and passages to the east and west.", 13, 5, 20, 11)
    room_list.append(room)
    # Hall 3
    room = Room("You have now entered the third hall!\nThere are rooms to the north and south and a passage to the west.", 14, 4, None, 19)
    room_list.append(room)
    # Patio
    room = Room("You are now on the patio!\nThere are chairs and plants located out here!\nThere is a room to the west and a passage to the south.", None, 20, None, 13)
    room_list.append(room)
    # Dining Room
    room = Room("You are now in the dining room!\nAll meals are served in this room!\nThere are rooms to the north, east and west and a passage to the south.", 15, 19, 14, 12)
    room_list.append(room)
    # Kitchen
    room = Room("You are now in the kitchen!\nAll meals are cooked in this room!\nThere are rooms to the east and west and a passage to the south.", None, 11, 13, 16)
    room_list.append(room)
    # Hammock
    room = Room("You are now in the room with hammocks!\nThis is a room for relaxing and book reading!\nThere are rooms to the south, east and west.", None, 10, 12, 17)
    room_list.append(room)
    # Hot tub
    room = Room("You are now in the hot tub area!\nThe perfect room for a spa day and relaxation!\nThere are rooms to the south and east.", None, 21, 16, None)
    room_list.append(room)
    # Outdoor grill
    room = Room("You are now outside at the grill!\nThe perfect summer meal is awaiting the use of this grill!\nThere is only a room to the south.", None, 13, None, None)
    room_list.append(room)

    current_room = 0


    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("What direction? ")

        if user_choice.upper() == "north" or user_choice.upper() == "n":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You can't go that way!")
            else:
                current_room = next_room










main()


