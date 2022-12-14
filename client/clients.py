import pygame
import sys
import socket
import main 
from streamData import *
import time
from threading import Thread

HOST = "127.0.0.1"
PORT = 54321
FORMAT = "utf8"

class Client:

    def __init__(self) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        # th = Thread(target=self.recvData,args=(self.s,))
        # th.setDaemon = True
        # th.start()
        # th.join()

    def connect(self):
        try:
            
            self.s.connect((HOST,PORT))
            print("NAME: ",self.s.getsockname())
            # self.sendData("Hello")
        except socket.error as e:
            print("Error: ",e)

    # def handle_client(self,s):
    #     while True:
    #         data = self.recvData()
    #         re = data.split(';')

            

    # def run(self):
    #     self.connect()
    #     th = Thread(target=self.handle_client,args=(self.s,))
    #     th.setDaemon = True
    #     th.start()
    #     self.stop()
        # main.run()
        # self.recv

    def recvData(self):
        data = self.s.recv(1024).decode(FORMAT)
        print("Recv: ",data)
        return data
    

    def sendData(self,data):
        
        try:
            self.s.send(data.encode(FORMAT))
            print("Send: ",data)
        except socket.error as e:
            print(e)

    def stop(self):
        self.s.close()

    def check_ok(self):
        recvdata = self.s.recv(1024).decode(FORMAT)
        print("Recv: ",recvdata)
        re = recvdata.split(';')
        while True:
            if getTypefromData(re[0]) == streamData.TRANGTHAI:
                if re[1] == "YES":
                    return True
                else:
                    return False

    def login(self,user,password):
        self.sendData("0;"+user+";"+password+";")
        recvdata = self.s.recv(1024).decode(FORMAT)
        print("Recv: ",recvdata)
        re = recvdata.split(';')
        while True:
            if getTypefromData(re[0]) == streamData.TRANGTHAI:
                if re[1] == "YES":
                    return True
                else:
                    return False
    
    def singin(self,user,password):
        self.sendData("1;"+user+";"+password+";")
        recvdata = self.s.recv(1024).decode(FORMAT)
        print("Recv: ",recvdata)
        re = recvdata.split(';')
        while True:
            if getTypefromData(re[0]) == streamData.TRANGTHAI:
                if re[1] == "YES":
                    return True
                else:
                    return False

    def create_room(self,roomid):
        self.sendData("5;"+str(roomid)+";")
        recvdata = self.s.recv(1024).decode(FORMAT)
        print("Recv: ",recvdata)
        re = recvdata.split(';')
        while True:
            if getTypefromData(re[0]) == streamData.TRANGTHAI:
                if re[1] == "YES":
                    return True
                else:
                    return False

    def join_room(self,roomid):
        self.sendData("6;"+str(roomid)+";")
        recvdata = self.s.recv(1024).decode(FORMAT)
        print("Recv: ",recvdata)
        re = recvdata.split(';')
        while True:
            if getTypefromData(re[0]) == streamData.TRANGTHAI:
                if re[1] == "YES":
                    return True
                else:
                    return False

    def show_room(self):
        self.sendData("4;OK;")
        recvdata = self.recvData()
        print(recvdata)
        re = recvdata.split(';')
        return re[1]
    
    def start(self,roomid):
        data = self.s.recv(1024).decode(FORMAT)
        print(data)
        re = data.split(';')
        if getTypefromData(re[0]) == streamData.START:
            if re[1] == roomid:
                return True
            else:
                return False
            

    def ready_room(self,roomid):
        self.sendData("14;"+str(roomid)+";")


    def leave_room(self,roomid,status):
        self.sendData("11;"+str(roomid)+";"+str(status)+";")
        recvdata = self.recvData()
        re = recvdata.split(';')
        if getTypefromData(re[0]) == streamData.CLOSE_ROOM:
            if re[1] =="YES":
                return True
            return False
        

    def move(self,roomid,X0,x,y):
        self.sendData("15;"+str(roomid)+';'+str(X0)+";"+str(x)+";"+str(y)+";")
    
    def recv_move(self):
        while True:
            recv = self.s.recv(1024).decode(FORMAT)
            print(recv)
            re = recv.split(';')
            if getTypefromData(re[0]) == streamData.MOVE:
                # if re[3] != x:
                return (re[2],re[3],re[4])
                # else:
                #     for i in range(len(re)):
                #         if getTypefromData(re[i]) == streamData.MOVE:
                #             return re[i+2],re[i+3],re[i+4]

    def win(self,roomid):
        while True:
            self.sendData("17;"+str(roomid)+";")
            recv = self.s.recv(1024).decode(FORMAT)
            print(recv)
            re = recv.split(';')
            if getTypefromData(re[0]) == streamData.WIN:
                return re[1]