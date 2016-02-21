'''
Created on 21/2/2016

@author: Johan
'''
class NotProperParamForGender(Exception):
    pass

class Gender(object):    
    SINGULAR_MALE = 0
    SINGULAR_FEMALE = 1
    PLURAL_MALE = 2
    PLURAL_FEMALE = 3
    
    valid_genders = [SINGULAR_MALE,SINGULAR_FEMALE,PLURAL_MALE,PLURAL_FEMALE]
    
    def __init__(self,gender):
        if gender not in self.valid_genders:
            raise NotProperParamForGender('Incorrect value for gender')
        self.gender = gender
        
    def with_article(self,name):
        if self.gender == self.SINGULAR_MALE:
            return 'el %s' % name
        elif self.gender == self.SINGULAR_FEMALE:
            return 'la %s' % name
        elif self.gender == self.PLURAL_MALE:
            return 'los %s' % name
        elif self.gender == self.PLURAL_FEMALE:
            return 'las %s' % name
        else:
            return name   
        
SingularMale = Gender(Gender.SINGULAR_MALE)
SingularFemale = Gender(Gender.SINGULAR_FEMALE)
PluralMale = Gender(Gender.PLURAL_MALE)
PluralFemale = Gender(Gender.PLURAL_FEMALE) 


    
