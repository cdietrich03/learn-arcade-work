def main():
    print("Welcome to Popeye!")
    print("You, Popeye, have stolen Bluto's camel to make your way across the Mobi desert.")
    print("Bluto wants his camel back and is chasing you down!")
    print("Survive your desert trek and out run Bluto.")

    # All of the variables
    user_total_miles_traveled = 0
    user_thirst = 0
    camel_tired = 0
    distance_bluto_traveled = -20
    cans_of_spinach = 3

    done = False
    while not done:
        print()
        print("A. Eat more spinach.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")

        # import random numbers
        import random

        # Choice of quitting
        if user_choice.upper() == "Q":
            done = True
            print("You have quit the best game ever.")

        # Choice of status check
        elif user_choice.upper() == "E":
            print("Miles traveled:", user_total_miles_traveled)
            print("Cans of spinach:", cans_of_spinach)
            print("Bluto is", user_total_miles_traveled - distance_bluto_traveled, "miles behind you.")

        # Choice of stop for the night
        elif user_choice.upper() == "D":
            camel_tired = 0
            print("Camel is happy!")
            print("Popeye is rested!")
            bluto_traveled_at_night = random.randrange(7, 15)
            distance_bluto_traveled = distance_bluto_traveled + bluto_traveled_at_night

        # Choice of full speed
        elif user_choice.upper() == "C":
            user_traveled_full_speed = random.randrange(10, 21)
            print("You traveled", user_traveled_full_speed, "miles.")
            user_total_miles_traveled = user_total_miles_traveled + user_traveled_full_speed
            user_thirst = user_thirst + 1
            camel_tired_full_speed = random.randrange(1, 4)
            camel_tired = camel_tired + camel_tired_full_speed
            bluto_traveled_full_speed = random.randrange(7, 18)
            distance_bluto_traveled = distance_bluto_traveled + bluto_traveled_full_speed
            if not done:
                if random.randrange(20) == 0:
                    print("You found a spinach farm!")
                    user_thirst = 0
                    camel_tired = 0
                    cans_of_spinach = 3

        # Choice of moderate speed
        elif user_choice.upper() == "B":
            user_traveled_moderate_speed = random.randrange(7, 13)
            print("You traveled", user_traveled_moderate_speed, "miles.")
            camel_tired = camel_tired + 1
            user_thirst = user_thirst + 1
            bluto_traveled_moderate_speed = random.randrange(7, 20)
            user_total_miles_traveled = user_total_miles_traveled + user_traveled_moderate_speed
            distance_bluto_traveled = distance_bluto_traveled + bluto_traveled_moderate_speed
            if not done:
                if random.randrange(20) == 0:
                    print("You found a spinach farm!")
                    user_thirst = 0
                    camel_tired = 0
                    cans_of_spinach = 3

        # Choice of eating spinach
        elif user_choice.upper() == "A":
            if cans_of_spinach > 0:
                cans_of_spinach = cans_of_spinach - 1
                user_thirst = 0
                print("Popeye enjoyed his spinach!")
            elif cans_of_spinach <= 0:
                print("No cans of spinach available!")

        # Bluto is getting close to Popeye
        if not done:
            if distance_bluto_traveled >= user_total_miles_traveled:
                done = True
                print("Bluto caught you and the camel!")
            elif distance_bluto_traveled >= (user_total_miles_traveled - 15):
                print("Bluto is getting close!")

        # The user won the game
        if not done:
            if user_total_miles_traveled >= 200:
                done = True
                print("You successfully stole the camel and won the game!")

        # Popeye is getting hungry
        if not done:
            if user_thirst > 4 and user_thirst <= 6:
                print("You are hungry!")
            elif user_thirst > 6:
                done = True
                print("You died of hunger!")

        # The camel is getting tired
        if not done:
            if camel_tired > 5 and camel_tired <= 8:
                print("Your camel is getting tired!")
            elif camel_tired > 8:
                done = True
                print("Your camel is dead!")


main()
