# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room, items=None):
        self.name = name
        self.room = room
        if items is None:  
            self.items = []
        else:
            self.items = items

    def get_item(self, item):
        for i in self.room.items:
            if item == i.name:        
                self.items.append(i)
                print(f'You picked up the {i.name}.')
                self.room.items.remove(i)

    def drop_item(self, item):
        for i in self.items:
            if item == i.name:
                self.items.remove(i)
                self.room.items.append(i)