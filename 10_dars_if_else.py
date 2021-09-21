# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:22:41 2021

@author: ASUS
"""




avtolar = ['audi','vovlvo','bmw','cobalt']

for avto in avtolar:#avtolar ichidagi har bir avto ucun
    if avto =='bmw': # agr avto bmw ga teng bo'lsa
        print(avto.upper())# avto nomini hamma hariflarini katta harif bn chiqar
    else: # aks holda
        print(avto.title())# avto nomi faqat birinchi nomi katta bn chiqar

# ism = 'Ali'# matinlarni solishtirganda-
# ism.lower() == 'ali'# matinlarni bir ko'rinishga keltirib olish kerak


# ism = input("Ismingiz nima?\n>>>")# foydalanuvchi ismini so'rash
# if ism.lower() != 'ali': #agar ism aliga teng bo'lmasa
#    print(f"Uzir, {ism.title()} biz Alini kutyabmiz.")# shu qisimni ciqar
# else:#agr teng bo'lsa 
#    print("Salom AliALI")#shu qisimni chiqar

# javob = float(input("12*6 nechiga teng?>>>"))# unlik songa aylantirib javob degan o;zgaruvchiga yuklaymiz
# if javob !=72:# agar javob 72 ga teng bo'lmasa
#    print("Javob xato")#shu xabarni chiqar
# bu kodimizda (else)funksiyasini tashlab ketdik yani kodning davomi yo'q

# yosh = int(input("Yoshingiz nechida?:"))# butun songa aylantiramiz
# if yosh >=18:# agar yosh 18 ga teng yoki katta bo'lsa 
#    print("Hush kelibsiz!")
# else:# aks holda 
#    print("Sizga kirish mumkin emas!")# shu kodni chiqar

# login = input("Yangi login kiriting:")
# if len(login)<=5:
#      print("Login 5 ta harifdan ko'proq bo'lishi shart!")


# yil = int(input("Tug'ulgan yilingizni kiriting:"))
# if 2021-yil<18:#foydalanuvchining yoshini hisoblaymiz
#    print(f"Yoshingiz {2021-yil} da ekan")
#    print("kirish mumkin emaas!")
# else:# aks holda
#    print(f"Yoshingiz {2021-yil} da ekan")
#    print("Xush kelibsiz")
   
# shart bilan badanini bir qatorga yozish ham mumkin
# yosh = int(input("Yosjingiz nechida?:"))
# if yosh>65: print("Siz COVID-19 risk gurihida ekansiz")

x,y = 25,40#x=25 y=40
print("x>y") if x>y else print("x<y")# if ning badani if dan oldin else ning badabi elsedan keyin











