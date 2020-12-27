#Ödev 2

#Hazırlayan: Abidin ARPACI
#İletişim: abidinarpaci@gmail.com

ad=input("Adınız ?:")
soyad=input("Soyadınız ?:")
dyil=int(input("Doğum Yılınız ?:"))
yas=2020-dyil
kisibilgileri=[ad,soyad,dyil,yas]

print("---------------------------")

for bilgi in kisibilgileri:
    print(bilgi)

if yas<18:
    print("Dışarı çıkamazsın çok tehlikeli")
else:
    print("Sokağa Çıkabilirsin. Maske takmayı unutma!")

print("")
print("Program Sona Erdi")
