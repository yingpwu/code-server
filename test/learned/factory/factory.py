from typing import Callable,Any
from player import Player

players_and_function : dict[str,Callable[...,Player]]={}

def register(role:str,function_name:Callable[...,Player]) -> None:
    players_and_function[role]=function_name

def unregister(role:str)->None:
    players_and_function.pop(role,None)

def create(args:dict[str,Any])->Player:
    the_args=args.copy()
    role=the_args["role"]
    
    try:
        function_name=players_and_function[role]
        return function_name(**the_args)
    except KeyError:
        raise ValueError(f'未知角色{role}') from None
