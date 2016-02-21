'''
Created on 21/2/2016

@author: Johan
'''
from model.item import Item

class NotProperParamForActor(Exception):
    pass  


class UnableToPerform(Exception):
    pass

class Actor(Item):
    '''
    classdocs
    '''

    def __init__(self, inventory=None, actions=None, name=None,gender=None,location=None,limits=None,others=None):
        '''
        Constructor
        '''
        if inventory:
            self.inventory = []
            if not isinstance(inventory,list):
                raise NotProperParamForActor('Inventory should be a list.')     
            for element in inventory:
                if not isinstance(element,Item):
                    raise NotProperParamForActor('Inventory should be a list of items.')
                element.set_location(self)
        else:
            self.inventory = []
            
        if actions:
            for a, b in actions.items():
                setattr(self,a,b)
            
        super(Actor, self).__init__(name=name,gender=gender,location=location,limits=limits,others=others)
        
    def add_to_inventory(self,item):
        if not isinstance(item,Item):
            raise UnableToPerform('Unable to add %s to inventory, it is not an item.' % item)
        self.inventory.append(item)
        