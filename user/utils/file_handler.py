def read_from_file(path:str) -> list[str]:
    with open(path,"r") as f:
        return f.readlines()


def add_to_file(path:str,line:str) -> None:
    with open(path,"a") as f:
        f.write(line)

