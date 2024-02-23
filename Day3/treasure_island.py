print("Welcome to Treasure island. Your mission is to find the treasure.")
direction = input("Where you want to go left or right?")
if direction == "right":
    print("Game Over.")
else:
    swim_wait = input("You wanna swim or wait?")
    if swim_wait == "swim":
        print("Game Over.")
    else:
        door = input("Pick a door red, blue or red?")
        if door == "red" or door == "blue":
            print("Game Over.")
        else:
            print("You Win!")


