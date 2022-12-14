import sys
import socket
from threading import Thread
from _thread import *
from socketserver import ThreadingMixIn
from database.database import *
from streamData import *
from room import *
import random
from roomManager import *

HOST = "127.0.0.1"
PORT = 54321
FORMAT = "utf8"
rownum = 21
colnum = 21
            
class Sever:

    def __init__(self) -> None:

        self.data = Database()
        global HOST
        global PORT
        global FORMAT
        global rownum
        global colnum

        self.grid = []
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST,PORT))
        self.roomManager = RoomManager()

        

        self.clients = {"conn":[], "roomid":[]}
    def create_grid(self):
        self.grid = []
        for row in range(rownum):
            self.grid.append([])
            for column in range(colnum):
                self.grid[row].append(0)
        # return self.grid
    # def accept(self):
    #     try:
    #         print("Client connecting....")
    #         (conn, addr) = self.s.accept()
    #         return  (conn,addr)
    #     except socket.error as e:
    #         print("Error: ",e)

    def login(self,id,passw,conn):
        if self.data.login(id,passw):
            self.sendData("3;YES;",conn)
            print("Dang nhap thanh cong!")       
        else:
            print("That bai")
            self.sendData("3;NO;",conn)

    def signin(self,id,passw,conn):
        if self.data.signin(id,passw):
            self.sendData("3;YES;",conn)
            print("Dang ki thanh cong!")       
        else:
            print("That bai")
            self.sendData("3;NO;",conn)

    def create_room(self,roomid,conn):
        try:
            self.roomManager.create_room(roomid,conn,"")
            self.sendData("3;YES;",conn)
            index = self.clients["conn"].index(conn)
            self.clients["roomid"][index] = roomid
            self.create_grid()
            print(self.clients)
        except:
            self.sendData("3;NO;",conn)

    def join_room(self,roomid,conn):
        try:
            self.roomManager.add_player(roomid,conn)
            index = self.clients["conn"].index(conn)
            self.clients["roomid"][index] = roomid
            self.sendData("3;YES;",conn)
            print(self.clients)
        except:
            # self.sendData("3;NO;")
            self.sendData("3;NO;",conn)
        
    def show_room(self,conn):
        try:
            listroom = self.roomManager.show_list()
            print("7;"+listroom+";")
            self.sendData("7;"+listroom+";",conn)
        except:
            # self.sendData("3;NO;")
            self.sendData("3;NO;")

    def win(self,roomid):
        status = self.checkwin(self.grid)
        for i in range(len(self.clients["roomid"])):
            if self.clients['roomid'][i] == roomid:
                conn1 = self.clients['conn'][i]
                self.sendData("17;" + str(status)+";",conn1)
               

    # def ready_room(self,roomid):
    #     self.roomManager.show_list()
    #     # for i in range(len(self.clients["conn"])):
    #     #     self.sendData("Hello!!",self.clients["conn"][i])
        
    #     if self.roomManager.room_ready(roomid):
    #         for i in range(len(self.clients)):
    #             if self.clients["roomid"][i] == roomid:
    #                 conn = self.clients["conn"][i]
    #                 self.sendData("3;YES;",conn)
    #     else:
    #         for i in range(len(self.clients)):
    #             if self.clients["roomid"][i] == roomid:
    #                 conn = self.clients["conn"][i]
    #             self.sendData("3;NO;",conn)

    def ready_room(self,roomid,conn):
        for i in range(len(self.clients["roomid"])):
            if self.clients['roomid'][i] == roomid:
                self.sendData("14;"+str(roomid)+";",conn)

    def leave_room(self,roomid,status,conn):
        if status == "1" or status == "2":
            for i in range(len(self.clients)):
                if self.clients["roomid"][i] == roomid:
                    conn1 = self.clients["conn"][i]
                    if conn1 == conn:
                        self.sendData("12;YES;",conn)
        self.sendData("12;NO;",conn)

    def move(self,roomid,X0,row,col,conn):
        # print(row,col)
        if self.grid[row][col] == 0 or self.grid[row][col] == "0":
            self.grid[row][col] = X0
        # print(self.grid)
        # room = self.roomManager.find_room(roomid)
        for i in range(len(self.clients["roomid"])):
            if self.clients['roomid'][i] == roomid:
                conn1 = self.clients['conn'][i]
                if conn != conn1:
                # print(conn)
                    self.sendData("15;"+str(roomid)+";"+str(X0)+";"+str(row)+";"+str(col)+";",conn1)
        # print(2)
        # self.sendData("15;"+str(roomid)+str(X0)+";"+str(row)+";"+str(col)+";",conn2)

    def handle_client(self,conn,addr):
        # print(conn.getsockname()," connect")
        while True:
            try:
                data = self.recvData(conn,addr)
                re = data.split(';')
                
                if getTypefromData(data) == streamData.LOGIN:
                    self.login(re[1],re[2],conn)
                
                if getTypefromData(data) == streamData.SIGNUP:
                    self.signin(re[1],re[2],conn)

                if getTypefromData(data) == streamData.CREATE_ROOM:
                    self.create_room(re[1],conn)
                
                if getTypefromData(data) == streamData.JOIN_ROOM:
                    self.join_room(re[1],conn)

                if getTypefromData(data) == streamData.LIST_ROOM:
                    self.show_room(conn)

                if getTypefromData(data) == streamData.START:
                    self.ready_room(re[1],conn)

                if getTypefromData(data) == streamData.LEAVE_ROOM:
                    self.leave_room(re[1],re[2],conn)

                if getTypefromData(data) == streamData.MOVE:
                    self.move(re[1],re[2],int(re[3]),int(re[4]),conn)
                if getTypefromData(data) == streamData.WIN:    
                    self.win(re[1])

            except:
                break
            
        print(conn.getsockname()," finished!")
        conn.close()
        

    def run(self):
        # threads = []
        print("SEVER CONNECTING-----")
        self.s.listen()
        while True:
            try:
                (conn, addr) = self.s.accept()
                # print(self.conn.getsockname())
                self.clients["conn"].append(conn)
                self.clients["roomid"].append("")
                
            except socket.error as e:
                print("Error: ",e)

            th = Thread(target= self.handle_client,args=(conn, addr))
            th.setDaemon = False
            th.start()
            # th.join()
            

        self.stop()

    def sendData(self,data,conn):
        try:
            conn.send(data.encode(FORMAT))
            print("Sever send : ", data)
            return data
        except socket.error as e:
            print("ERROR: ",e)

    def recvData(self,conn,addr):
        try:
            data = conn.recv(1024).decode(FORMAT)
            print(addr," recv: ",data)
            return data
        except socket.error as e:
            print("Error: ",e)

    def stop(self):
        self.s.close()

    def checkwin(self,board):
        indices = [i for i,x in enumerate(board) if 'x' in x]
        for index in indices:
            xrowindices = [i for i, x in enumerate(board[index]) if x == "x"]
            for xs in xrowindices:
                if xs<=len(board[0])-5:
                    if board[index][xs] == board[index][xs+1] == board[index][xs+2] == board[index][xs+3] == board[index][xs+4]:
                        return 1
                if index<=len(board)-5:
                    if board[index][xs] == board[index+1][xs] == board[index+2][xs] == board[index+3][xs] == board[index+4][xs]:
                        return 1
                    if xs<=len(board[0])-5:
                        if board[index][xs] == board[index+1][xs+1] == board[index+2][xs+2] == board[index+3][xs+3] == board[index+4][xs+4]:
                            return 1
                        if board[index][xs] == board[index+1][xs-1] == board[index+2][xs-2] == board[index+3][xs-3] == board[index+4][xs-4]:
                            return 1
        indices1 = [i for i,x in enumerate(board) if 'o' in x]
        for index1 in indices1:
            orowindices = [i for i, x in enumerate(board[index1]) if x == "o"]
            for os in orowindices:
                if os<=len(board[0])-5:
                    if board[index1][os] == board[index1][os+1] == board[index1][os+2] == board[index1][os+3] == board[index1][os+4]:
                        return 2
                if index1<=len(board)-5:
                    if board[index1][os] == board[index1+1][os] == board[index1+2][os] == board[index1+3][os] == board[index1+4][os]:
                        return 2
                    if os<=len(board[0])-5:
                        if board[index1][os] == board[index1+1][os+1] == board[index1+2][os+2] == board[index1+3][os+3] == board[index1+4][os+4]:
                            return 2
                        if board[index1][os] == board[index1+1][os-1] == board[index1+2][os-2] == board[index1+3][os-3] == board[index1+4][os-4]:
                            return 2
        count = 0
        for rows in board:
            for cells in rows:
                if cells == 'x' or cells == 'o':
                    count+=1
                if count == rownum*colnum:
                    return 3
        return 0