class Stack:
    def __init__(self): #self: burdaki elemanlara disardan erisim saglayabilmek icin
        self.liste = []
        print("Stack initialised")

    def __str__(self):
        deger = [str(x) for x in self.liste[::-1]]  # Liste son eklenenden başlayarak yazdırılıyor
        return '\n'.join(deger)
    def isEmpty(self):
        return len(self.liste)==0

    def push(self,x):
        self.liste.append(x)
        print("Eleman yigina eklendi")

    def pop(self):#son elemani siler(sadece sona erisimimiz var)
        if self.isEmpty():
            print("Yigin bos")
        else:
            print(self.liste)
            self.liste.reverse()
            print("Eleman yigindan silindi")
            print(self.liste)
            return self.liste.pop() #(yigindan bagimsiz)listenin son elemanini silmek icin normalde pop kullanilir

    def peek(self):#son elemani silmeden gosterir
        print("peek cagrildi")
        if self.isEmpty():
            print("Stack bos")
        else:
            self.liste.reverse()
            return self.liste[len(self.liste)-1]

    def delete(self):#tum yapiyi silmek icin
        print("Yigin silindi.")
        self.liste=None

yigin=Stack()
print(yigin.isEmpty())

yigin.push(16)
yigin.push(21)
yigin.push(72)
yigin.push('Ali')

print(yigin)
print()

yigin.pop() #en son eklenen elemana erisebildigimiz icin onu siler

print(yigin)
print()

print('peek metodu ile ogrenilen deger: ',yigin.peek())
print()

yigin=Stack()
print(yigin.isEmpty())

yigin.push(16)
yigin.push(21)
yigin.push(72)
yigin.push('Ali')

print(yigin)


yigin.pop() #en son eklenen elemana erisebildigimiz icin onu siler

print(yigin)


print('peek metodu ile ogrenilen deger: ',yigin.peek())


yigin.delete()

"""
def __str__(self):
        elemanlar = self.list.reverse()
        elemanlar=[str(x) for x in self.liste]
        return "\n".join(elemanlar)
"""