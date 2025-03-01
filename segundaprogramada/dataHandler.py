import os
import pickle

INFO_DAT_FILENAME = "info.dat"
infoFileChecked = False

def createInfoDatIfNotExists(directoryPath):
    """
    If 'info.dat' does not exist in 'directoryPath', create it with 750 empty slots.
    Each slot will initially be None to indicate it's empty.
    """
    global infoFileChecked

    if infoFileChecked:
        return
    filePath = os.path.join(directoryPath, INFO_DAT_FILENAME)
    if not os.path.exists(filePath):
        print("Creating 'info.dat' with 750 empty records...")
        emptySlots = [None] * 750
        with open(filePath, "wb") as f:
            pickle.dump(emptySlots, f)
    else:
        print(f"The file '{INFO_DAT_FILENAME}' already exists. No new file created.")

    infoFileChecked = True

def loadInfoDat(directoryPath):
    """
    Loads the list of 750 records from 'info.dat' in 'directoryPath' and returns it.
    If the file doesn't exist, it calls createInfoDatIfNotExists first.
    """
    createInfoDatIfNotExists(directoryPath)
    filePath = os.path.join(directoryPath, INFO_DAT_FILENAME)
    with open(filePath, "rb") as f:
        dataList = pickle.load(f)
    return dataList

def saveInfoDat(directoryPath, dataList):
    """
    Overwrites the entire list of 750 records into 'info.dat'.
    """
    filePath = os.path.join(directoryPath, INFO_DAT_FILENAME)
    with open(filePath, "wb") as f:
        pickle.dump(dataList, f)

def insertRecord(directoryPath, position, puntPlayObj):
    """
    Inserts a PuntPlay object into 'info.dat' at the given 'position' or 
    into a collision file if the slot is already occupied.
    """
    dataList = loadInfoDat(directoryPath)

    if dataList[position] is None:
        dataList[position] = puntPlayObj
        saveInfoDat(directoryPath, dataList)
    else:
        collisionFilename = f"{position}-col.dat"
        collisionPath = os.path.join(directoryPath, collisionFilename)
        with open(collisionPath, "ab") as f:
            pickle.dump(puntPlayObj, f)

def readCollisionFile(directoryPath, position):
    """
    Reads ALL PuntPlay objects stored in <position>-col.dat and returns them in a list.
    If the file doesn't exist, returns an empty list.
    """
    collisionFilename = f"{position}-col.dat"
    collisionPath = os.path.join(directoryPath, collisionFilename)
    if not os.path.exists(collisionPath):
        return []
    
    collisionRecords = []
    with open(collisionPath, "rb") as f:
        while True:
            try:
                obj = pickle.load(f)
                collisionRecords.append(obj)
            except EOFError:
                break
    return collisionRecords

def findRecords(directoryPath, position):
    """
    Returns a list of all PuntPlay records for the given 'position':
    - The primary record from 'info.dat' (if any).
    - Any collision records from <position>-col.dat (if it exists).
    """
    dataList = loadInfoDat(directoryPath)
    mainRecord = dataList[position]  

    collisionList = readCollisionFile(directoryPath, position)
    
    results = []
    if mainRecord is not None:
        results.append(mainRecord)
    results.extend(collisionList)
    return results
