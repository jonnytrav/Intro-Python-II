from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("player1", room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(new_player.__str__())

    user_input = input(
        # MAY HAVE TO USE SPLIT() BELOW LIKE THE OTHER FUNCTIONS THAT USED INPUT
        "Press 'q' to quit and 'n', 's', 'e', or 'w' to move north, south, east, and west.  ".lower())

    if user_input[0] == "q":
        break
    elif user_input[0] == "n":
        if new_player.location.n_to != "":
            new_player.location = new_player.location.n_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "s":
        if new_player.location.s_to != "":
            new_player.location = new_player.location.s_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "e":
        if new_player.location.e_to != "":
            new_player.location = new_player.location.e_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "w":
        if new_player.location.w_to != "":
            new_player.location = new_player.location.w_to
        else:
            print("There is nothing in that direction! Try again.")
    else:
        print("Invalid input! 'n', 's', 'e', 'w' and 'q' are all valid commands. Try once more. ")
