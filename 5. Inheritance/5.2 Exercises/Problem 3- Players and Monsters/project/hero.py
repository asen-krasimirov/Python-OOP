

class Hero:
    username: str
    level: int

    def __init__(self, username: str, level: int):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"