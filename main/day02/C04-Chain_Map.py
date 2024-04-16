import collections

sozluk1={'renk1':'kirmizi','renk2':'yesil'}
sozluk2={'renk3':'sari','renk4':'mavi'}

CM= collections.ChainMap(sozluk1,sozluk2)
print(CM.maps,'\n')
print("Anahtarlar={}".format(list(CM.keys())))
print("Degerler={}".format(list(CM.values())))
print("Elemanlar:")

for anahtar,deger in CM.items():
    print("{}:{}".format(anahtar,deger))
    print()

print('CM de renk2 var mi?:{}'.format("renk2" in CM))
print('CM de renk5 var mi?:{}'.format("renk5" in CM))

#yeni eleman ekleme
CM["renk5"]="siyah"
print(CM)

#eleman silme
del CM["renk2"]
print(CM)

#anahtar disindaki kelimelere ulasmak icin
# 1.kumeyi direkt parent olarak aldi ve 2.yi verdi
print(CM.parents)
