#opt 3 Jack Wu
hashTable = [0]*10
Max = 10


def key(newItem):
    b = newItem % 10
    return b
        
        
def insert(newItem):
    index = key(newItem)
    while hashTable[index] != 0:
        
        index = index + 1
        if index >= Max:
            index=0
    hashTable[index] = newItem

def findRecord(searchNumber):
    index = key(searchNumber)
    while hashTable[index] != searchNumber:
        
        index = index + 1
        if index >= Max:
            index=0
        else:
            return index
    if hashTable[index] != 0:
        return index

insert(25)
a=findRecord(25)
print(a)



