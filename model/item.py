'''
Created on 21/2/2016

@author: Johan
'''
from gender import Gender,SingularMale
from __builtin__ import setattr

class NotProperParamForItem(Exception):
    pass     

class Item(object):
    '''
    classdocs
    '''


    def __init__(self,name=None,gender=None,location=None,limits=None,others=None):
        '''
        Constructor
        '''
        if name:
            if not isinstance(name, str) and not isinstance(name, unicode):
                raise NotProperParamForItem('Name is not a string.')
            self.name = name
        else:
            self.name = self.__class__.__name__
        if gender:
            if not isinstance(gender,Gender):
                raise NotProperParamForItem('Gender is not a proper one.')
            self.gender = gender
        else:
            self.gender = SingularMale
        if location:
            self.location = location
        else:
            self.location = None
            
        if limits:
            for a, b in limits.items():
                setattr(self,'verify_' + a,b)  
                          
        if others:
            for a, b in others.items():
                setattr(self,a,b)
            
    def __str__(self):
        return self.gender.with_article(self.name)
    
    def set_location(self,location):
        if self.location != location:
            self.location = location
            location.add_content(self)
            
if __name__ == '__main__':
    from gender import SingularFemale
    cosa = Item(name='cosa',gender=SingularFemale,others={'color':'azul'})
    print cosa

        
        