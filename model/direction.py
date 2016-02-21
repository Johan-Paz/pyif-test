'''
Created on 21/2/2016

@author: Johan
'''
from gender import Gender,SingularMale

class NotProperParamForDirection(Exception):
    pass

class Direction(object):
    '''
    classdocs
    '''
    
    def __init__(self,name=None,gender=None):
        '''
        Constructor
        '''
        if name:
            if not isinstance(name, str) and not isinstance(name, unicode):
                raise NotProperParamForDirection('Name is not a string.')
            self.name = name
        else:
            self.name = self.__class__.__name__
        if gender:
            if not isinstance(gender,Gender):
                raise NotProperParamForDirection('Gender is not a proper one.')
            self.gender = gender
        else:
            self.gender = None
            
    def __str__(self):
        return self.gender.with_article(self.name)


North = Direction(name='norte',gender=SingularMale)
South = Direction(name='sur',gender=SingularMale)
East = Direction(name='este',gender=SingularMale)
West = Direction(name='oeste',gender=SingularMale)
Up = Direction(name='subir')
Down = Direction(name='bajar')
        