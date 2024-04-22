class Node:
    def __init__(self, veri=None):
        self.veri = veri
        self.sonraki = None
        self.onceki = None


class SLinked_List:
    def __init__(self):
        self.ilkdugum = None

    def liste_yaz(self,dugum):
        while dugum is not None:
            print(dugum.veri)
            dugum = dugum.sonraki

    def ekle(self,yeniveri):
        yeni_dugum = Node(yeniveri)
        yeni_dugum.sonraki = self.ilkdugum
        if self.ilkdugum is not None:
            self.ilkdugum.onceki = yeni_dugum
        self.ilkdugum = yeni_dugum


