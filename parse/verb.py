'''
Created on 21/2/2016

@author: Johan
'''

class NotProperParamForVerb(Exception):
    pass

class Verb(object):
    '''
    classdocs
    '''

    def __init__(self, player, npc, infinitive):
        '''
        Constructor
        '''
        if not isinstance(player, str) and not isinstance(player, unicode):
            raise NotProperParamForVerb('Player is not a string.')
        self.player = player 
        
        if not isinstance(npc, str) and not isinstance(npc, unicode):
            raise NotProperParamForVerb('Npc is not a string.')
        self.npc = npc   
        
        if not isinstance(infinitive, str) and not isinstance(infinitive, unicode):
            raise NotProperParamForVerb('Infinitive is not a string.')
        self.infinitive = infinitive   
        
COGER = Verb('coges','coge','coger')     
        