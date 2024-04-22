class Stack:
    def __init__(self,boyut): #self: burdaki elemanlara disardan erisim saglayabilmek icin
        self.list = []
        self.boyut = boyut
        print("Stack initialised")

    def __str__(self):
        elemanlar = self.list.reverse()
        elemanlar = [str(x) for x in elemanlar]
        return "\n".join(elemanlar)

    def is_empty(self):
        return len(self.list) == 0

    def isfull(self):
        if len(self.list) == self.boyut:
            return True
        return False

    def push(self,veri):
        self.list.append(veri)

    def pop(self):
        if self.is_empty():
            print("Stack empty")
        else:
            self.list.reverse()
            self.list.pop()

    def peek(self):
        if self.is_empty():
            print("Stack empty")
        else:
            self.list.reverse()
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None


