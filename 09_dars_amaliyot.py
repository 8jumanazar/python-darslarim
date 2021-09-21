# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:49:43 2021

@author: ASUS
"""

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

#ismlar = ['Ali','Vali','Hasan','Husan','Olim']
#for ism in ismlar:
 #   print(f"Salom , {ism}, ishga hush kelibsiz!")
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

#print("Kod ", len(ismlar), " marta takrorlandi")
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring

#toq_sonlar = list(range(11,100,2))
#for kub in toq_sonlar:
   # print(f"{kub},{kub**3}")
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring

# kinolar =[]
# print("5 ta eng sevimli kinolaringizni kiriting:")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-kinoyingizni nomini kiritin:"))
# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
royxat =[]
suhbat =int(input("Siz bugun nechta odam bilan suhbat qldingiz:"))
for n in range(suhbat):
    royxat.append(input(f"{n+1}-Ularning isimlarini kiriting:"))
print(royxat)





















