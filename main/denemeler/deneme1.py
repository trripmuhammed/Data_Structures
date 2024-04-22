class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        elemanlar = [str(x) for x in self.items]
        return "\n".join(elemanlar)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def dequeue(self,deger):
        self.items.append(deger)

    def enqueue(self):
        if self.isEmpty():
            print("Bos liste moruq")
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Bos liste moruq")
        else:
            return self.items[0]