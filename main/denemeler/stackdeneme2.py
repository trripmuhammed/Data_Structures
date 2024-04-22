#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Yığın ve Kuyruk Yapıkları

yığın LİFO --> son giren ilk çıkar

kuyruk FİFO --> ilk giren ilk çıkar

"""
## YIĞIN YAPILARI
#class Stack:
#    def _init_(self):#self elemanlara dışarıdan eriişimi sağlamak için kullanılır
#        self.list=[]
#        print('stack oluşturuldu')
#
#    def _str_(self):
#        elemanlar=self.list.reverse()
#        elemanlar=[str(x) for x in self.list]
#        return '\n'.join(elemanlar)
#
#    def isEmpty(self):
#        if self.list==[]:
#            return True
#        else:
#            return False
#
#    def push(self,deger):
#        self.list.append(deger)
#        return "Eleman yığına eklendi"
#
#    def pop(self):
#        if self.isEmpty():
#            return "yiğin boş"
#        else:
#            self.list.reverse()
#            return self.list.pop()#en son eklenen degeri silecek o yüzden parametre vermememiz gerekiyor
#    def peek(self):
#        if self.isEmpty():
#            return "Stack boş"
#        else:
#            self.list.reverse()
#            return self.list[len(self.list)-1]
#
#    def delete(self):#ddelete ile tüm listeyi veya buyruğu silebiliyoruz
#        print("yığın silindi")
#        self.list=None
#
#
#
#yigin = Stack()
#print(yigin.isEmpty())
#
#yigin.push(16)
#yigin.push(21)
#yigin.push(69)
#yigin.push("Trabzon")
#print(yigin)
#
#yigin.pop()#parametre kanbul etmiyor sadece son elemano siliyor
#print(yigin)
#
#print('peek metodu ile öprenilen değer',yigin.peek())
#yigin.delete()

#"""
#class Stack:
#    def _init_(self,boyut):#self elemanlara dışarıdan eriişimi sağlamak için kullanılır
#        self.list=[]
#        self.boyut=boyut
#        print('stack oluşturuldu')
#
#    def _str_(self):
#        deger=self.list.reverse()
#        deger=[str(x) for x in self.list]
#        return '\n'.join(elemanlar)
#
#    def isFull(self):
#        if len(self.list)==self.boyut:
#            return True
#        else:
#            return False
#
#    def push(self,eleman):#eleman yeni parametre
#        if self.isFull():
#            return "yığın dolu"
#        else:
#            self.list.append(eleman)
#            return "eleman yığına eklendi"
#
#
#yigin.Stack(4)
#yigin.push('trabzon')

#"""
#----------------------------------------------------------------------------------------------
## KUYRUK YAPILARI
#class Queue:
#    def _init_(self):#self elemanlara dışarıdan eriişimi sağlamak için kullanılır
#        self.items=[]
#        print('Kuyruk Yapısı Oluşturuldu')
#
#    def _str_(self):
#        elemanlar=[str(x) for x in self.items]
#        return '\n'.join(elemanlar)
#
#    def isEmpty(self):#Kuyruk boşmu dolumu kontrolünü yapar
#        if self.items==[]:
#            return True
#        else:
#            return False
#
#
#    def enqueue(self,deger):#Kuyruğa eleman ekler
#        self.items.append(deger)
#        return "Eleman kuyruğa eklendi"
#
#
#    def denqueue(self):#Kuyruğa eleman ekler
#        if self.isEmpty():
#            return "Kuyruk boş"
#        else:
#            return self.items.pop()
#
#    def peek(self):#Yığındaki ilk elemana erişim sağllıyabiliyoruz
#        if self.isEmpty():
#            return True
#        else:
#            return self.items[0]
#
#
#
#
#Kuyruk=Queue()
#print(Kuyruk.isEmpty())
#print(Kuyruk)
#Kuyruk.enqueue(6)
#Kuyruk.enqueue(8)
#Kuyruk.enqueue(11)
#print(Kuyruk)
#print("\n")
#print(Kuyruk.peek())
#
##Kuyruk.denqueue()
#

#----------------------------------------------------------------------------
#   Hash Tablosu

#def h_tablo_goster(tablo):
#    for i in range(len(tablo)):
#        print(i,end="")
#        for j in tablo[i]:
#            print("-->",end="")
#            print(j,end="")
#        print()
#        tablo= [[]for _ in range(10)]
#
#def Hashing(anahtar):
#    return anahtar%len(tablo)
#
#def ekle(tablo,anahtar,deger):
#    yer=Hashing(anahtar)
#    tablo[yer].append(deger)
#    ekle(tablo,10,'Ahmet')
#    ekle(tablo,25,'Mehmet')
#    ekle(tablo,20,'Can')
#
#h_tablo_goster(tablo)

#----------------------------------------------------------------------------
#ASCII


#def modASCII(string, tabloBoyut):
#    toplam=0
#    for i in string:
#        toplam+=ord(i)
#    return toplam%tabloBoyut
#print(modASCII("ABC",20))
#----------------------------------------------------------------------------