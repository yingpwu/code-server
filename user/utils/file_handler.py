from ast import Str


def read_from_file(path:str) -> list[str]:
    with open(path,"r") as f:
        return f.readlines()


def add_to_file(path:str,line:str) -> None:
    with open(path,"a") as f:
        f.write(line)


def write_to_file(path:str,lines:list[Str])->None:
    with open(path,'w') as f:
        f.writelines(lines)