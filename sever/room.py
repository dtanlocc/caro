class Room:
    def __init__(self,roomid,playerkey,player2="") -> None:
        self.roomid = roomid
        self.player_1 = playerkey
        self.player_2 = player2
        self.number_players = 1

    def set_player2(self,playerid):
        self.player_2 = playerid

    def get_player(self):
        return (self.player_1,self.player_2)

    def get_roomid(self):
        return self.roomid

    def number_player(self):
        if self.player_1 == "":
            return 0
        if self.player_2 == "" :
            return 1
        return 2

    def find_room(self,id):
        if id == self.roomid:
            return Room(self.roomid,self.player_1,self.player_2)

    def add_player(self,playerid = ""):
        if self.number_player == 1:
            self.set_player2(playerid)
            self.set_number_players(2)

    def set_number_players(self,n):
        self.number_players = n

    def ready(self):
        if self.number_players == 2:
            return True
        return False

    

