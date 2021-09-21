#   05-dars.  String  (Matin)
#  O'quvchi: Jumanazar Shokirov
#  sana: 02_09_2021


ism = "Jumanazar"

# O'zgaruvchilarning qiymati istalgan hariflar bilan yozilishi mumkin!
shahar = "Наманган"
tuman = 'ПОП'






# String ustida amallar

ism = 'Jumanazar'
print("Mening ismim " + ism)

ism = 'Jumanazar'
familya = 'Shokirov'
print(ism + familya) # bu yerda natija ism va familya qo'shilgan xolda chiqdi!
print(ism + ' ' + familya)# bu yerda ism va familya aloxida yozilib chiqdi!

#  f- String

ism = "Jumanazar"
familya = 'shokirov'
ism_familya = f"{ism} {familya}"
print(ism_familya)

ism = "Iskandar"
familya = 'Shokirov'
print(f"Salom, mening ismim {ism}. {ism} {familya}")

#   Mahsus belgilar

print("Salom Dunyo")
print("Salom \tDuno")
print("Salom \nDunyo")


# String metodlari

ism = "Jumanazar"
familya = 'Shokirov'
ism_sharif = f"{ism} {familya}"
#ism_sharif = ism_sharif.upper()# bu yerda o'zgaruvchilarning qiymatiga o'zgartirish kiritildi!
print(ism_sharif.upper())# metodi matndagi har bir harfni katta harfga o'zgartiradi.
print(ism_sharif.lower())# metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
print(ism_sharif.capitalize())#  esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
print(ism_sharif.title())# metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.

meva = "     Olma    "
print(meva)
print("Men " + meva.lstrip() + " yahshi ko'raman") #  matn boshidagi bo'shliqni,olib tashlaydi.
print("Men " + meva.rstrip()+ " yahshi ko'raman") #  matn oxiridagi bo'shliqni,
print("Men " + meva.strip()+ " yahshi ko'raman")  #  matn boshi va oxiridagi bo'shliqlarni olib tashlaydi

#   Input 
# bu funksiy foydalanuvchidan biror bir matin yoki shunga o'xshash talab qiladi

#ism = input("Ismingiz nima?")
#print("Assalomu alaykum," + ism)

ism = input("Ismingiz nima?\n>>>")
print("Assalomu alaykum, " + ism.title())

