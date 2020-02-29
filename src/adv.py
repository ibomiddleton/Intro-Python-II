from room import Room
from player import Player
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
to north. Te smell of gold permeates the air."""),

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

# # Main
# #

# Make a new player object that is currently in the 'outside' room.
player = Player('Isaac')
location = player.getLocation()
currentRoom = room[player.getLocation()]
choice = ''
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

print("""\nWelcome to Adventure Game!\n""")

while choice != 'q':
    print(f'Your Location: {currentRoom}\n')
    choice = input(
        f'Choose your path, {player}\nOr enter q to leave the game.\n')
    if len(choice) == 1:
        if choice == 'n'  and dir(currentRoom).count('n_to') > 0:
            newRoom = currentRoom.n_to
            currentRoom = newRoom
            continue
        elif choice == 's' and dir(currentRoom).count('s_to') > 0:
            newRoom = currentRoom.s_to
            currentRoom = newRoom
            continue
        elif choice == 'e' and dir(currentRoom).count('e_to') > 0:
            newRoom = currentRoom.e_to
            currentRoom = newRoom
            continue
        elif choice == 'w' and dir(currentRoom).count('w_to') > 0:
            newRoom = currentRoom.w_to
            currentRoom = newRoom
            continue
        elif choice == 'q':
            print('Goodbye,', player.name)
            exit
        else:
            print(f'{room[location]}')
            choice = input(
                f'\nSorry, that choice is invalid.\n \nChoose your path, {player}\n \nEnter q to leave the game.\n')
    else:
        choice = input('Try Again')