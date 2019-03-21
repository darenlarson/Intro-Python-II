from room import Room
from player import Player
from item import Item

# Declare all the items
item = {
    "hat": Item("Hat", "A floppy hat that keeps you cool in the sun"),
    "knife": Item("Knife", "A sharp knife with a wooden handle"),
    "bow": Item("Bow", "A long bow to shoot arrows with")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["hat"], item["knife"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["hat"], item["bow"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["hat"], item["knife"], item["bow"]]),

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
player = Player('Daren', room['outside'])

# Write a loop that:
#
# DONE * Prints the current room name
# DONE * Prints the current description (the textwrap module might be useful here).

# DONE * Waits for user input and decides what to do.
#
# DONE If the user enters a cardinal direction, attempt to move to the room there.
# DONE Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print('\n---------------------------------------------------------------------------\n')
    print(f'Current Room: {player.room.name}, Description: {player.room.description}\n')
    user_input = input('What do you want to do? (n/s/e/w to go to another room, list to see items in room): ')
    print('\n')
    parsedInput = user_input.split(' ')

    if len(parsedInput) == 1:
        if user_input == 'n':
            if player.room == room['overlook'] or player.room == room['treasure']:
                print('\nYOU CANNOT GO THIS WAY. Choose another direction.\n')
            else:
                player.room = player.room.n_to
        elif user_input == 's':
            if player.room == room['outside'] or player.room == room['narrow']:
                print('\nYOU CANNOT GO THIS WAY. Choose another direction.\n')
            else:
                player.room = player.room.s_to
        elif user_input == 'e':
            if player.room == room['narrow'] or player.room == room['treasure'] or player.room == room['overlook'] or player.room == room['outside']:
                print('\nYOU CANNOT GO THIS WAY. Choose another direction.\n')
            else:
                player.room = player.room.e_to
        elif user_input == 'w':
            if player.room == room['outside'] or player.room == room['foyer'] or player.room == room['overlook'] or player.room == room['treasure']:
                print('\nYOU CANNOT GO THIS WAY. Choose another direction.\n')
            else:
                player.room = player.room.w_to
        elif user_input == 'list':
            if len(player.room.items) == 0:
                print(f'\nThere are no items in this room')
            else:
                for item in player.room.items:
                    print(f'{item.name}: {item.description}')
        elif user_input == "inventory" or user_input == "i":
            if len(player.items) == 0:
                print('You have no items')
            else:
                for i in player.items:
                    print(f'{i.name}: {i.description}')
        elif user_input == 'q':
            break
    elif len(parsedInput) == 2:
        action = parsedInput[0]
        targetItem = parsedInput[1]

        if action == 'get' or action == 'take':
            player.get_item(targetItem)
        if action == 'drop':
            player.drop_item(targetItem)