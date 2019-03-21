from room import Room
from player import Player
from item import Item
from item import LightSource

# Declare all the items
item = {
    "hat": Item("Hat", "A floppy hat that keeps you cool in the sun."),
    "knife": Item("Knife", "A sharp knife with a wooden handle."),
    "bow": Item("Bow", "A long bow to shoot arrows with."),
    "gold": Item("Gold", "Shiny goooooooold."),
    "silver": Item("Silver", "Shiny silverrrrrr. Worth 1/8 gold oz."),
    "hammer": Item("Heavy Hammer", "Steel hammer is very heavy."),
    "shovel": Item("Shovel", "For digging..."),
    "lantern": LightSource("Lantern", "Gives you unlimited light where there is none."),
}

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", True),
    'foyer': Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east.", True),
    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", True),
    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air.", False),
    'treasure': Room("Treasure Chamber", "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.", True),
    'beach': Room("Ocean View Beach", "You've made it to the ocean and see ships on the horizon.", True),
    'forest': Room("Hidden Forest", "The forest is dark and quiet. It seems as if you are being watched.", False),
    'desert': Room("Hot Desert", "Nothing but sand dunes.", True),
    'mountains': Room("Rocky Mountain Mile", "Mountains as far as you can see. You notice some paths through some of the peaks.", True),
    'city': Room("New York City", "The city is busy. There is a market place to trade for goods nearby.", True),
    'hyrule': Room("Hyrule", "Welcome Link.", True),
    'volcano': Room("Active Volcano", "It is hot and looks like hell. Demons are everywhere.", False),
}

# Add items to rooms
room['outside'].items = [item['silver'], item['gold'], item['lantern']]
room['foyer'].items = [item['silver'], item['hammer']]
room['overlook'].items = [item['gold'], item['hat']]
room['narrow'].items = [item['knife'], item['bow']]
room['treasure'].items = [item['gold'], item['silver']]
room['beach'].items = [item['shovel'], item['lantern']]
room['forest'].items = [item['bow'], item['knife']]
room['desert'].items = [item['hat'], item['shovel']]
room['mountains'].items = [item['hat'], item['knife']]
room['city'].items = [item['gold'], item['knife']]
room['hyrule'].items = [item['bow'], item['knife']]


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].e_to = room['forest']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['overlook'].w_to = room['beach']
room['beach'].e_to = room['overlook']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].s_to = room['forest']
room['treasure'].s_to = room['narrow']
room['forest'].e_to = room['volcano']
room['forest'].s_to = room['desert']
room['forest'].n_to = room['narrow']
room['forest'].w_to = room['outside']
room['desert'].n_to = room['forest']
room['desert'].e_to = room['hyrule']
room['desert'].s_to = room['mountains']
room['mountains'].n_to = room['desert']
room['volcano'].w_to = room['forest']
room['volcano'].s_to = room['hyrule']
room['hyrule'].n_to = room['volcano']
room['hyrule'].e_to = room['desert']
room['hyrule'].s_to = room['city']
room['city'].n_to = room['hyrule']
room['city'].w_to = room['mountains']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Daren', room['outside'])

# Loop to play the game
while True:
    print('---------------------------------------------------------------------------')
    print(f'Current Room: {player.room.name}, Description: {player.room.description}, Light: {"Yes" if player.room.is_light == True else "No"}\n')
    print("'n/e/s/w' to move. 'list' to view items in the room. 'inventory/i' to view your items.\n")
    user_input = input('What do you want to do: ')
    print('\n')
    parsedInput = user_input.split(' ')

    if len(parsedInput) == 1:
        if user_input == 'n' or user_input == 'e' or user_input == 's' or user_input == 'w':
            direction = user_input
            next_room = player.room.get_next_room(direction)
            if next_room == None:
                print('\nYOU CANNOT GO THIS WAY. Choose another direction.\n')
            else:
                player.room = next_room

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
        else:
            print("Invalid Input")
    
    elif len(parsedInput) == 2:
        action = parsedInput[0]
        targetItem = parsedInput[1]

        if action == 'get' or action == 'take':
            player.get_item(targetItem)
        elif action == 'drop':
            player.drop_item(targetItem)
        else:
            print("Invalid Input")