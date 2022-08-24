from abc import abstractmethod,ABC

class Player(ABC):
    def __init__(self,name,role):
        self.name=name
        self.role=role

    @abstractmethod
    def action(self):
        '''球员的动作'''

    def __str__(self):
        return f'name={self.name}, role={self.role}'

class Forward(Player):
    def action(self):
        print(f'{self.name} 带球突破,过了后卫,凌空抽射!')


class MiddleFielf(Player):
    def action(self):
        print(f'{self.name} 控球在脚,假动作晃过对方10号,精准长传')


class DefenseField(Player):
    def action(self):
        print(f'{self.name} 用强悍的神曲,挡住对方的进攻')


class GoalKeeper(Player):
    def action(self):
        print(f'{self.name} 接住对方的射门')
