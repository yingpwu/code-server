from typing import Callable,Any
from player import Player

player_creation_function : dict[str,Callable[...,Player]]={}
def register(role:str,creation_function:Callable[...,Player]) ->None:
    player_creation_function[role]=creation_function

def unregister(role:str)->None:
    player_creation_function.pop(role,None)

def create(args:dict[str,Any])->Player:
    the_args=args.copy()
    role=the_args['role']

    try:
        create_function=player_creation_function[role]
        return create_function(**the_args)

    except KeyError:
        raise ValueError(f"未知角色 {role!r}")  from None
        
