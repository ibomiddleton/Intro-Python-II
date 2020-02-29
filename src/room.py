# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.linked_rooms = []

    def __str__(self):
        output = f"{self.name}\n{self.description}"
        return output


