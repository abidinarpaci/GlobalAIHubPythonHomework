#Ödev 4 Öğrenci Yönetim Sistemi

#Hazırlayan: Abidin ARPACI
#İletişim: abidinarpaci@gmail.com

import sys

sayac=0
while sayac<3:
    
    ad=input("Adınız ?:")
    soyad=input("Soyadınız ?:")

    if ad.isalpha()==True and soyad.isalpha()==True:
        print("Merhaba ",ad,"",soyad)
        print("----------------------------------")
        print("")
        sayac=-1
        break
    else:
        sayac+=1

if sayac!=-1:
    print("Please Try Again Later")
    sys.exit(0)

    
kurssayisi=0

kurslar=[]

print("Kurs Ekleme Ekranından Çıkmak İçin Kursa Adı Olarak")
print("q")
print("Yazınız")
print("")

kursadi=""

while kursadi!="q":
    
    kursadi=input("Eklenecek Kurs Adını Giriniz:")
    if kursadi.lower()!="q":
        kurslar.append(kursadi)
    else:
        if len(kurslar)<3:
            print("You Failed In Class")
        else:
            break

print("")
print("Ders Seçim Ekranına Hoş Geldiniz")
print("---------------------------------")
for i,dersadi in enumerate(kurslar):
    print("Ders No: ",i,"- ",dersadi)
print("")
dersno=int(input("Seçilen Ders No:"))
print("")
print(kurslar[dersno],"Dersi Not Giriş Ekranına Hoş Geldiniz")
print("---------------------------------")

midtermpuan=int(input("Midterm Notu:"))
finalpuan=int(input("Final Notu:"))
projectpuan=int(input("Proje Notu:"))

notlarsozluk = {"midterm":midtermpuan, "final":finalpuan,"project":projectpuan}

dersnotu=(midtermpuan*0.3)+(finalpuan*0.5)+(projectpuan*0.2)
print("")
print("Puanınız:",dersnotu)
print("Not Karşılığı:")
if dersnotu>90:
    print("Puanınız","AA")
elif dersnotu>70:
    print("Puanınız","BB")
elif dersnotu>50:
    print("Puanınız","CC")
elif dersnotu>30:
    print("Puanınız","DD")
elif dersnotu>0:
    print("Puanınız","FF")
    print("Maalesef Kaldınız")
    


