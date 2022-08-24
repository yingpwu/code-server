from abc import ABC

class Player(ABC):
    def __init__(self,name,role):
        self.name=name
        self.role=role
    
    def action(self):
        '''球员动作'''
    
    def __str__(self):
        return f'name={self.name} role={self.role}'

class Forward(Player):
    def action(self):
        print(f"前锋,{self.name}带球过人")

class MiddleFiled(Player):
    def action(self):
        print(f"中场,{self.name} 精通传球")

class DefendShield(Player):
    def action(self):
        print(f"守门员,{self.name}强悍防卫")

class GoalKeeper(Player):
    def action(self):
        print(f"射手,{self.name}抵挡射门")
