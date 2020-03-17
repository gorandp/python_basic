import csv
import datetime
import constants

def fileManager(date, t):
    try:
        with open(constants.filePath, 'r') as temp:
            pass
    except:
        # Esto lo hago para saber si tengo que grabar o no los headers del csv
        with open(constants.filePath, 'a') as myFile:
            print('File does not exist. Creating new one.')
            csvW = csv.DictWriter(myFile, fieldnames=constants.fieldnames)
            csvW.writeheader()
            csvW.writerow(dataToDict(date, constants.typesOfTurns[t]))
    else:
        with open(constants.filePath, 'a') as myFile:
            csvW = csv.DictWriter(myFile, fieldnames=constants.fieldnames)
            csvW.writerow(dataToDict(date, constants.typesOfTurns[t]))
    print("[OK] ", dictToStr(dataToDict(date, constants.typesOfTurns[t])))

def dictToStr(myDict):
    tempStr = ""
    for key in myDict:
        tempStr += str(myDict[key]) + " "
    return tempStr

def dataToDict(date, t):
    dateData = {
        'date': "{:04d}-{:02d}-{:02d}".format(date.year, date.month, date.day),
        'time': "{:02d}:{:02d}:{:02d}".format(date.hour, date.minute, date.second),
        'type': t
    }
    return dateData

def addTurnNow(opc=None):
    now = datetime.datetime.now()

    if opc is None:
        print("Start or End (s/e): ")
        opc = input()
        if not(opc == 's' or opc == 'e'):
            raise ValueError('r u kiddin me')
    __addTurnGeneric(now, opc)

def addTurnToday(opc=None):
    d = datetime.date.today()
    print("Hour: ")
    hour = int(input())
    print("Minute: ")
    minute = int(input())
    today = datetime.datetime(year=d.year, month=d.month, day=d.day, hour=hour, minute=minute, second=0)

    if opc is None:
        print("Start or End (s/e): ")
        opc = input()
        if not(opc == 's' or opc == 'e'):
            raise ValueError('r u kiddin me')
    __addTurnGeneric(today, opc)

def addTurnOtherDay(opc=None):
    print("Year [YYYY]: ")
    year = int(input())
    print("Month: ")
    month = int(input())
    print("Day: ")
    day = int(input())
    print("Hour: ")
    hour = int(input())
    print("Minute: ")
    minute = int(input())
    date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=0)

    if opc is None:
        print("Start or End (s/e): ")
        opc = input()
        if not(opc == 's' or opc == 'e'):
            raise ValueError('r u kiddin me')
    __addTurnGeneric(date, opc)

def __addTurnGeneric(date, typeOfTurn):
    fileManager(date, typeOfTurn)


if __name__ == "__main__":
    print("1. NOW | 2. Today (other hour) | 3. Another day and hour")
    print("Select:")
    opc = int(input())
    if opc == 1:
        addTurnNow()
    elif opc == 2:
        addTurnToday()
    elif opc == 3:
        addTurnOtherDay()
    else:
        print("Option does not exist boy.")
    print("Finish")
