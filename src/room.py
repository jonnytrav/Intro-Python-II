# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        print(f"name: {self.name}, description: {self.description}")

    def print_items(self):
        if len(self.items) > 0:
            print(f"{self.name}'s obtainable items include: ")
            for i in self.items:
                print(i.name)
        else:
            print("This room contains no valuable items.")

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
