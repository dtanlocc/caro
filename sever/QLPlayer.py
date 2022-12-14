from player import *
from sever import *

class MultiPlayer:
    def __init__(self) -> None:
        self.sever = Sever()
        self.listPlayer = []

    def add(self):
        player = Player()
        self.listPlayer.append(player)
