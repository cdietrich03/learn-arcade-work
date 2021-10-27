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
    room = Room("You are in the greenhouse!\n"
                "Here we grow beautiful tropical trees!\n"
                "There are rooms to the north and east.",
                8, None, 1, None)
    room_list.append(room)

    # Living Room
    room = Room("You are in the living room!\n"
                "There is a nice TV in here!\n"
                "There are rooms to the north, east, and west.",
                7, None, 2, 0)
    room_list.append(room)

    # Grand Entrance
    room = Room("You are now in the grand entrance of the house!\n"
                "There is a beautiful chandelier above!\n"
                "There are rooms to the north, east, and west.",
                6, None, 3, 1)
    room_list.append(room)

    # Piano Room
    room = Room("You are now in the piano room!\n"
                "Music is played here all throughout the day!\n"
                "There are rooms to the north, east, and west.",
                5, None, 18, 2)
    room_list.append(room)

    # Bedroom 1
    room = Room("You are now in the first bedroom!\n"
                "This room is space themed!\n"
                "There are rooms to the west and south, and a passage to the north. ",
                20, 18, None, 5)
    room_list.append(room)

    # Bathroom 1
    room = Room("You are now in the first bathroom!\n"
                "This is a full bath with a rain shower!\n"
                "There are rooms to the east, west, and south, and a passage to the north.",
                19, 3, 4, 6)
    room_list.append(room)

    # Family Room
    room = Room("You are now in the family room!\n"
                "This room is full of laughter and couches!\n"
                "There are rooms to the east, west, and south, and a passage to the north.",
                11, 2, 5, 7)
    room_list.append(room)

    # Bedroom 2
    room = Room("You are now in the second bedroom!\n"
                "This room is covered head-to-toe in pink!\n"
                "There are rooms to the north, south, east, and west",
                10, 1, 6, 8)
    room_list.append(room)

    # Master Bedroom
    room = Room("You are now in the master bedroom!\n"
                "This is the biggest room in the house!\n"
                "There are rooms to the north east, and south and a surprise to the west.",
                21, 0, 7, 9)
    room_list.append(room)

    # Balcony
    room = Room("You are now on the Balcony!\n"
                "There is a beautiful view of the Rocky Mountains!\n"
                "There is only a room to the east.",
                None, None, 8, None)
    room_list.append(room)

    # Library
    room = Room("You are now in the library!\n"
                "There are almost 2000 books located here!\n"
                "There are rooms to the north, south, and west and a passage to the east.",
                16, 7, 11, 21)
    room_list.append(room)

    # Hall 1
    room = Room("You have now entered the first hall!\n"
                "There are rooms to the north, west, and south and a passage to the east.",
                12, 6, 19, 10)
    room_list.append(room)

    # Kitchen
    room = Room("You are now in the kitchen!\n"
                "All meals are cooked in this room!\n"
                "There are rooms to the east and west and a passage to the south.",
                None, 11, 13, 16)
    room_list.append(room)

    # Dining Room
    room = Room("You are now in the dining room!\n"
                "All meals are served in this room!\n"
                "There are rooms to the north, east and west and a passage to the south.",
                15, 19, 14, 12)
    room_list.append(room)

    # Patio
    room = Room("You are now on the patio!\n"
                "There are chairs and plants located out here!\n"
                "There is a room to the west and a passage to the south.",
                None, 20, None, 13)
    room_list.append(room)

    # Outdoor grill
    room = Room("You are now outside at the grill!\n"
                "The perfect summer meal is awaiting the use of this grill!\n"
                "There is only a room to the south.",
                None, 13, None, None)
    room_list.append(room)

    # Hammock
    room = Room("You are now in the room with hammocks!\n"
                "This is a room for relaxing and book reading!\n"
                "There are rooms to the south, east and west.",
                None, 10, 12, 17)
    room_list.append(room)

    # Hot tub
    room = Room("You are now in the hot tub area!\n"
                "The perfect room for a spa day and relaxation!\n"
                "There are rooms to the south and east.",
                None, 21, 16, None)
    room_list.append(room)

    # Bonsai Room
    room = Room("You are now in the bonsai room!\n"
                "Trees are sculpted to perfection in here!\n"
                "There are rooms to the north and west.",
                4, None, None, 3)
    room_list.append(room)

    # Hall 2
    room = Room("You have now entered the second hall!\n"
                "There are rooms to the north, and south and passages to the east and west.",
                13, 5, 20, 11)
    room_list.append(room)

    # Hall 3
    room = Room("You have now entered the third hall!\n"
                "There are rooms to the north and south and a passage to the west.",
                14, 4, None, 19)
    room_list.append(room)

    # Master Bathroom
    room = Room("You are now in the master bathroom!\n"
                "This is the biggest bathroom in the house!\n"
                "There are rooms to the north east, and south.",
                17, 8, 10, None)
    room_list.append(room)

    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("What direction? ")

        # Go north
        if user_choice.lower() == "north" or user_choice.lower() == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        # Go south
        elif user_choice.lower() == "south" or user_choice.lower() == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        # Go east
        elif user_choice.lower() == "east" or user_choice.lower() == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        # Go west
        elif user_choice.lower() == "west" or user_choice.lower() == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way!")
            else:
                current_room = next_room

        # Quit the game
        elif user_choice.lower() == "quit" or user_choice.lower() == "q":
            done = True
            print("You have quit the best game ever!")

        # The computer will not take this direction
        else:
            print()
            print("Try a different direction!")

main()
