class Vendor:
    #insert doc strings

    def __init__(self, inventory = None):
        '''
        Constructs attributes for Vendor object, default inventory value is empty list.
        '''
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''
        Adds item to attribute inventory, returns item.
        '''
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        '''
        Removes item from attribute inventory if item in list, returns item; else returns False.
        ''' 
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
