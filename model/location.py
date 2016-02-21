'''
Created on 21/2/2016

@author: Johan
'''
from gender import Gender,SingularMale
from direction import Direction
from item import Item

class NotProperParamForLocation(Exception):
    pass

class Location(object):
    '''
    classdocs
    '''

    def __init__(self,name=None,description=None,gender=None,connections=None,content=None,others=None):
        '''
        Constructor
        '''
        if name:
            if not isinstance(name, str) and not isinstance(name, unicode):
                raise NotProperParamForLocation('Name is not a string.')
            self.name = name
        else:
            self.name = self.__class__.__name__
            
        if description:
            if not isinstance(description, str) and not isinstance(description, unicode):
                raise NotProperParamForLocation('Description is not a string.')
            self.description = description
        else:
            self.description = 'Un lugar muy anodino.'            
            
        if gender:
            if isinstance(name,Gender):
                raise NotProperParamForLocation('Gender is not a proper one.')
            self.gender = gender
        else:
            self.gender = SingularMale
            
        if connections:
            if not isinstance(connections,dict):
                raise NotProperParamForLocation('Connections should be a dict.')
            for side in connections:
                if not isinstance(side,Direction):
                    raise NotProperParamForLocation('One of the connections is not a known direction.')
                if not isinstance(connections[side],Location):
                    raise NotProperParamForLocation('In direction %s there is not a proper location.' % side.name)
                setattr(self, side.name, connections[side])
                
        if content:
            self.content = []
            if not isinstance(content,list):
                raise NotProperParamForLocation('Content should be a list.')     
            for element in content:
                if not isinstance(element,Item):
                    raise NotProperParamForLocation('Content should be a list of items.')
                element.set_location(self)
        else:
            self.content = []
            
        if others:
            for a, b in others.items():
                setattr(self,a,b)
            
    def __str__(self):
        return self.gender.with_article(self.name)
    
    def print_content(self):
        if self.content:
            print 'Puede verse:'
            for element in self.content:
                print '\t- %s' % element
                
    def add_content(self,item):
        if not isinstance(item,Item):
            raise NotProperParamForLocation('Item should be a Item.')
        if not self.content:
            self.content = []
        if item not in self.content:
            self.content.append(item)
            item.set_location(self)   
            
    def show(self):
        print self.description
        print
        self.print_content()     
        
            
            
        