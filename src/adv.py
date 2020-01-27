from player import Player
from room import Room
from item import Item

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

# DECLARE ALL OF THE ITEM INSTANCES
inventory = {
    "shovel": Item("shovel", "Three feet long with a metal handle."),
    "lantern": Item("lantern", "Antique and fragile. Still works perfectly."),
    "sword": Item("sword", "Heavy and slightly rusted. Belonged to King Arthur."),
    "keychain": Item("keychain", "One of these will open the treasure chamber..."),
    "goblet": Item("goblet", "Large and nearly covered in gold.")
}


# ADD ITEMS TO THE GAME THE USER MAY CARRY AROUND
outside_item = [inventory["shovel"]]
room['outside'].items = outside_item

foyer_item = [inventory["lantern"]]
room['foyer'].items = foyer_item

overlook_item = [inventory["sword"]]
room['overlook'].items = overlook_item

narrow_item = [inventory["keychain"]]
room['narrow'].items = narrow_item

treasure_item = [inventory["goblet"]]
room['treasure'].items = treasure_item

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
    print(new_player)
    new_player.current_room.print_items()

    user_input = input(
        # MAY HAVE TO USE SPLIT() BELOW LIKE THE OTHER FUNCTIONS THAT USED INPUT
        "Press 'q' to quit and 'n', 's', 'e', or 'w' to move north, south, east, and west. 'h' for additional commands. ".lower()).split(" ")

    if user_input[0] == "q":
        break
    elif user_input[0] == "h":
        print("The command 'get' followed by the desired item will pick it up for you. The command 'drop' works in the same way.")
    elif user_input[0] == "i":
        print(new_player.print_items())
    elif user_input[0] == "n":
        if new_player.current_room.n_to != None:
            new_player.current_room = new_player.current_room.n_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "s":
        if new_player.current_room.s_to != None:
            new_player.current_room = new_player.current_room.s_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "e":
        if new_player.current_room.e_to != None:
            new_player.current_room = new_player.current_room.e_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "w":
        if new_player.current_room.w_to != None:
            new_player.current_room = new_player.current_room.w_to
        else:
            print("There is nothing in that direction! Try again.")
    elif user_input[0] == "get":
        # print(user_input[1])
        new_player.add_item(inventory[user_input[1]])
        new_player.current_room.remove_item(inventory[user_input[1]])
        inventory[user_input[1]].on_take()
    elif user_input[0] == "drop":
        # print(user_input[1])
        new_player.current_room.add_item(inventory[user_input[1]])
        new_player.drop_item(inventory[user_input[1]])
        inventory[user_input[1]].on_drop()
    else:
        print("Invalid input! 'n', 's', 'e', 'w' and 'q' are all valid commands. Try once more. ")
