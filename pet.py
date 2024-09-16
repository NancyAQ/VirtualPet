import random as rnd
class Virtual_Pet():
    
    def __init__(self,name='Alb'):
        self.name=name
        self.hunger=7
        self.mood=7
        self.happy_sound='yay'
        self.sad_sound='hmmph'
        self.hunger_sounds='brrrr'
    def clock_tik(self):
        self.hunger+=1
        if self.hunger>5:
            self.mood-=1
    def introduction(self):
        intro='Hi I am your lovely pet, my name is '+self.name+' '
        if(self.mood<5):
            intro=intro+' I am sad'
        else:
            intro=intro+' I am Happyyy'
        return intro
    
    def greeting(self):
        if(self.mood<5):
            print (self.sad_sound)
        else:
            print (self.happy_sound)
            
    def food(self):
        self.hunger-=1
        
    def play(self):
        self.mood+=1
            
           
            
        
        
        
    
        