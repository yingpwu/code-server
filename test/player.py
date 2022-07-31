form abc import abstractmethod,ABC

class Player(ABC):
    def __init__(self,name,role):
        self.name=name
        self.role=role

    def action(self):
        '''球员的动作'''
