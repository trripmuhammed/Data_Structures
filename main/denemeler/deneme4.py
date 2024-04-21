class Node:
    def __init__(self,veri=None):
        self.veri = veri
        self.onceki = None
        self.sonraki = None

class ciftyonlu:
    def __init__(self):
        self.ilkdugum=None

    def ekle(self,deger):
        yenidugum = Node(deger)
        yenidugum.sonraki = self.ilkdugum
        if self.ilkdugum is not None:
            self.ilkdugum.onceki = yenidugum
        self.ilkdugum = yenidugum

    def listeyaz(self,dugum):
        while dugum is not None:
            print(dugum.veri)
            son=dugum
            dugum=dugum.sonraki
