# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room, items=[]):
        self.name = name
        self.current_room = current_room
        self.items = items

    def __str__(self):
        return "{self.name} is located in {self.current_room.name}.".format(self=self)

    def print_items(self):

        if len(self.items) > 0:
            print("Your inventory contains: \n")
            for item in self.items:
                return f"{item.name} \n"
        else:
            return "Your inventory is empty... \n"

    def add_item(self, item):
        if item in self.current_room.items:
            self.items.append(item)
        else:
            print("That item is located elsewhere. Keep looking.")

    def drop_item(self, item):
        self.items.remove(item)
