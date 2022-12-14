from room import *
import random

class RoomManager:
    def __init__(self) -> None:
        self.listRoom = []

    def create_room(self,roomid,player1,player2=""):
        room = Room(roomid,player1,player2)
        self.listRoom.append(room)

    def find_room(self,roomid):
        for i in range(len(self.listRoom)):
            if self.listRoom[i].get_roomid() == roomid:
                return self.listRoom[i]
    
    def show_list(self):
        listroom_2 = []
        for i in range(len(self.listRoom)):
            listroom_2.append(self.listRoom[i].get_roomid())
        print(listroom_2)
        return listroom_2
        # return self.listRoom

    def find_room_1_player(self):
        listroom_1 = []
        for i in range(len(self.listRoom)):
            if self.listRoom[i].number_player == 0:
                self.listRoom.pop(i)
        for i in range(len(self.listRoom)):
            if self.listRoom[i].ready:
                listroom_1.append(self.listRoom[i].get_roomid())
        
        return listroom_1[0]
    
    def add_player(self,roomid,player2):
        room = self.find_room(roomid)
        room.add_player(player2)
        room.set_number_players(2)

    def join_room_1(self,player2):
        listroom_1 = []
        for i in range(len(self.listRoom)):
            if self.listRoom[i].ready:
                listroom_1.append(self.listRoom[i])
        room = listroom_1[0]
        room.add_player(player2)
        room.set_number_players(2)
        return room.get_roomid()

    def room_ready(self,roomid):
        for i in range(len(self.listRoom)):
            if self.listRoom[i].get_roomid() == roomid:
                print(self.listRoom[i].ready())
                return self.listRoom[i].ready()