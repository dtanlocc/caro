from enum import Enum

class streamData(Enum):
    LOGIN = 0
    SIGNUP = 1
    TRANGTHAI = 3

    LIST_ROOM = 4
    CREATE_ROOM = 5
    JOIN_ROOM = 6

    FIND_MATCH = 7
    # CANCEL_FIND_MATCH = 8

    DATA_ROOM = 9
    # CHAT_ROOM = 10
    LEAVE_ROOM = 11
    CLOSE_ROOM = 12

    GAME_EVENT = 13 
    
    START = 14
    MOVE = 15 #DANH 1 NUOC

    SURRENDER = 16 # /FF
    WIN = 17
    UNKNOW_TYPE = 18

    EXIT = 19

def getType(data):
    result = streamData.UNKNOW_TYPE
    try:
        data = int(data)
        if streamData(data) in streamData:
            result = streamData(data)
    except:
        print("UNKNOW_TYPE: " , data)
    return result

def getTypefromData(data):
    tp = data.split(';')[0]
    return getType(tp)
