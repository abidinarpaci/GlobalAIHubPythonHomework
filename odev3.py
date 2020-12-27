#Ödev 3 - Hangman

#Hazırlayan: Abidin ARPACI
#İletişim: abidinarpaci@gmail.com

"""
Önce oyunda kullanıcıya sorulacak kelimlerin yer aldığı bir kelime listesi oluşturulur
Kullanıcı hatalı harf tahmin hakkı 5 harftir
"""

import random

print("Hangman Oyununa Hoş Geldiniz")
ad=input("Lüften İsminizi Giriniz:")

print("Merhaba {}".format(ad))
print("")

kelimeler=["elma","armut","domates","lahana","havuç","mantar","patates","soğan","sarmısak","turp"]
secilenkelimeno=random.randint(0, len(kelimeler)-1) #listedeki eleman sayısına göre rastgele bir sayı belirlenir
secilenkelime=kelimeler[secilenkelimeno]#listeden sıra nosu belirlenen sayi olan kelime aktarılır

ysecilenkelime=secilenkelime #işlem yapılırken kullanılacak

toplam_hs=len(secilenkelime) #seçilen kelimenin toplam harf sayısı
hatali_hs=0 #kullanıcın hatalı tahmin ettiği harf sayısı
dogru_hs=0 #kullanıcın doğru tahmin ettiği harf sayısı

print("Seçilen Kelime",len(secilenkelime)," Harflidir")

while hatali_hs<5:
    print("Kalan Hatalı Harf Girme Hakkı:",5-hatali_hs)
        
    harf=input("Lütfen Bir Harf Tahmin Edin:")
    harf=harf.lower()#Listede yer alan tüm kelimeler küçük harf olduğu için alınan harf önce küçük harfe çevrilir
  

    if harf in secilenkelime:
        print("Tebrikler Doğru Harf Girdiiniz")
        ysecilenkelime=ysecilenkelime.replace(harf,"*")
        
        cikti=""
        dogru_hs=0
        for i,harf in enumerate(secilenkelime):
            if ysecilenkelime[i]=="*":
                cikti=cikti+harf
                dogru_hs+=1
            else:
                cikti=cikti+"-"
        print(cikti)
       
        if toplam_hs==dogru_hs:#Doğru Harf Sayısı Toplam Harf Sayısına Eşitse
            print("Tebrikler Kelimeyi Doğru Tahmin Ettiniz")
            hatali_hs=-1
            break
      
    else:
        print("Yanlış Harf Girdiiniz")
        cikti=""
        dogru_hs=0
        for i,harf in enumerate(secilenkelime):
            if ysecilenkelime[i]=="*":
                cikti=cikti+harf
                dogru_hs+=1
            else:
                cikti=cikti+"-"
        print(cikti)
        
        hatali_hs+=1
   
    print("--------------------------------------------------")
if hatali_hs==-1:
    print("Oyunu Başarı İle Tamamladınız")
else:
    print("Maalesef Oyunu Kazanamadınız")
    print("Doğru Cevap")
    print(secilenkelime)
    
    
