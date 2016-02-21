'''
Created on 21/2/2016

@author: Johan
'''
from parse.verb import Verb,COGER

class NotProperParamForAction(Exception):
    pass

class UnableToExecute(Exception):
    pass

class Action(object):
    '''
    classdocs
    '''


    def __init__(self, verb,method,default_action=None):
        '''
        Constructor
        '''
        if not isinstance(verb, Verb):
            raise NotProperParamForAction('Verb is not of a proper class.')
        self.verb = verb   
        
        if not isinstance(method, str) and not isinstance(method, unicode):
            raise NotProperParamForAction('method is not a string.')
        self.method = method  
        
        self.default_action = default_action
        
    def execute_player(self,actor,one=None):
        if not actor:
            raise UnableToExecute('Not player provided.')
        if one:
            if hasattr(one, 'verify_' + self.method) and callable(getattr(one,'verify_' + self.method)):
                result = getattr(one, 'verify_' + self.method)(actor)
                if result:
                    print 'Intentas %s %s, pero %s.' %(self.verb.infinitive,one,result)
                    return
        if hasattr(actor, self.method) and callable(getattr(actor,self.method)):
            getattr(actor, self.method)(one)
        elif self.default_action:
            self.default_action(actor,one)
            
            
def default_coger(actor,one):
    actor.add_to_inventory(one)
    print ('%s coge %s.' % (actor,one)).capitalize()
    
Coger = Action(COGER,'coger',default_coger)
            
        
        
        