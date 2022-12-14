import socket
from sever import *
from streamData import *

class Player:
    def __init__(self) -> None:
        self.id = ""
        self.idroom = ""
        

    def run(self):
        self.received = self.sever.re
        key = self.received[0]
        if key == streamData.LOGIN:
            self.login(self.received)

    def sendData(self,data):
        try:
            if data != "":
                self.sever.sendData(data)
                print("SendData: ", data)
        except:
            print("Error sendData!")

    