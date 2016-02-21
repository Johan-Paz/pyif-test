#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21/2/2016

@author: Johan
'''
from model import item, gender, location, actor, action

def demasiado_caliente(actor):
    return 'está demasiado caliente para cogerla'

vela = item.Item(name='vela atómica',gender=gender.SingularFemale,limits={'coger':demasiado_caliente})
espada = item.Item(name='espada',gender=gender.SingularFemale)

def jugador_coger(item):
    print 'Coges %s.' % item

jugador= actor.Actor(name='jugador',actions={'coger':jugador_coger})
patio = location.Location(name='patio',gender=gender.SingularMale,content=[espada,vela])

if __name__ == '__main__':
    patio.show()
    print '\n>> coger vela\n'
    action.Coger.execute_player(jugador, vela)
    print '\n>> coger espada\n'
    action.Coger.execute_player(jugador, espada)
    