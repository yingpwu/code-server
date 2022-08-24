from player import Player,Forward,MiddleFielf,DefenseField

def main():
    data={
        "players":[
            {
                "name":"Eric Cantona",
                "role":"FW"
            },{
                "name":"David Beckham",
                "role":"MF"
            },{
                "name":"Steve Bruce",
                "role":"DF"
            }
        ]
    }
    players=[]
    for player in data["players"]:
        role=player["role"]
        if role == "FW":
            players.append(Forward(**player))
        elif role == "MF":
            players.append(MiddleFielf(**player))
        elif role == "DF":
            players.append(DefenseField(**player))
    
    for player in players:
        print(player)
        player.action()

if __name__=='__main__':
    main()
