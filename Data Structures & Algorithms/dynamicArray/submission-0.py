class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None for i in range(capacity)]
        self.capacity = capacity
        self.length = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()

        # insert at next empty position
        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        if self.length > 0:
            # soft delete the last element
            self.length -= 1
        # return the popped element
        return self.array[self.length]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        self.array.extend([None for i in range(self.capacity)])


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity

