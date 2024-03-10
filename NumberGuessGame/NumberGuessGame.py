# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 01:18:38 2024

@author: Lenovo
"""

import random

tahmin_sayisi = 0
girilen_sayi = input("Sayıyı Giriniz: ")


if girilen_sayi.isdigit():
    girilen_sayi = int(girilen_sayi)
    
    if girilen_sayi <= 0:
        print("0 dan farklı sayı giriniz.")
        quit()
else:
    print("Lütfen sayı değeri giriniz.")


rastgele_sayilar = random.randint(0, girilen_sayi)

while True:
    tahmin_sayisi += 1
    
    tahmini_sayi = input("Tahmininiz: ")
    if tahmini_sayi.isdigit():
       tahmini_sayi = int(tahmini_sayi)
       
    else: 
       print("Sayı olarak Tahmin Yapılmalıdır.")
       continue
   
    if tahmini_sayi == rastgele_sayilar:
       print("Bulduk ")
       break
    
    elif tahmini_sayi > rastgele_sayilar:
         print("Daha Düşük Sayı Giriniz: ")
    
    else:
         tahmini_sayi < rastgele_sayilar
         print("Daha Yüksek Sayı Giriniz: ")
       
print("Tahmin sayisi: " + str(tahmin_sayisi))

