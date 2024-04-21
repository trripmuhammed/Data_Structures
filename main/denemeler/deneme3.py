class Node:
    def __init__(self,veri):
        self.veri=veri
        self.sonraki=None


class Linked_List:
    def __init__(self):
        self.ilkdugum=None

    def liste_yaz(self):
        dugum=self.ilkdugum
        while dugum is not None:
            print(dugum.veri)
            print(dugum.sonraki)
            dugum = dugum.sonraki

    def basa_ekle(self,yeniveri):
        yenidugum=Node(yeniveri)
        yenidugum.sonraki=self.ilkdugum
        self.ilkdugum=yenidugum


    def sona_ekle(self,yeniveri):
        yenidugum=Node(yeniveri)
        if self.ilkdugum is None:
            self.ilkdugum = yenidugum
            return
        ilk = self.ilkdugum
        while ilk.sonraki:
            ilk = ilk.sonraki
        ilk.sonraki = yenidugum

    def sil(self,dugum):
        ilkdugum = self.ilkdugum
        if ilkdugum is not None:
            if ilkdugum.veri == dugum:
                self.ilkdugum = ilkdugum.sonraki()
                ilkdugum = None
                return
            while (ilkdugum is not None):
                if (ilkdugum.veri == dugum):
                    break
                prev = ilkdugum
                ilkdugum = ilkdugum.sonraki
            if(ilkdugum == None):
                return
            prev.sonraki = ilkdugum.sonraki
            ilkdugum = None

liste = Linked_List()
d1 = Node("Kirmizi")
d2 = Node("Yesil")
d3 = Node("Siyah")
d4 = Node("Mavi")
liste.ilkdugum = d1
d1.sonraki = d2
d2.sonraki = d3
d3.sonraki = d4
liste.basa_ekle("Mor")
liste.sona_ekle("Pembe")
liste.liste_yaz()