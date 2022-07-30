

class UserAuthenticationRequest:
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password

    def __eq__(self, other) -> bool:
        if not isinstance(other,UserAuthenticationRequest):
            return False
        
        return self.username==other.username and self.password==other.password