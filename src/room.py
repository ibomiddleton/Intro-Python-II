# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def get_name(self):
        return self.name
    
    def describe(self):
        print( self.description )
    


