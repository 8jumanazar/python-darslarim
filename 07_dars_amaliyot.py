# 07_dars_List Amaliyot

# Mualif:Jumanazar Shokirov
#  Quyidagi mashqlarni bajaring:
#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
#isimlar = ['Iskandar','Jumanazar','Job','husan']
#print("Salom ", isimlar[0]," ishlar yahshimi")
#print(isimlar[1], " bugun birglikda dars qilamizmi?")
#print (f"{isimlar[1]}, {isimlar[-2]} ni  ham chaqir!")
#print(isimlar[-1].title()," sen ham bizga qo'shilasanmi?")
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik)
#sonlar = [12,-4,10,22,1,6.7]
#print(sonlar)
#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
#sonlar[0] = sonlar[0], + sonlar[1]
#sonlar[2] = -6 
#sonlar[4] = sonlar[4],+ 45
#del sonlar[5]
#print(sonlar)
#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
#t_shaxis = ["Al Horazmiy","Al Termiziy","Alisher Navoiy"]
#z_shaxis = ["Jumanazar","Iskandar","Bobur"]
#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
#hohish = t_shaxis.pop(0)
#istak = z_shaxis.pop(1)   
#print("Men tarixiy shahislardan ", hohish," bilan,")
#print("Zamonaviy shaxislardan ",  istak, " bilan suhbatlashishni xoxlayman!" )
#friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friends =[]
friends.append("Jumanazar")
friends.append("Iskandar")
friends.append("Otam")
friends.append("Onam")
friends.append("singlim")
friends.append("Bobur")
#print(friends)
#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove("Bobur")
friends.remove("Jumanazar")
#print(friends)
#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing
friends.append("Donyor")
friends.insert(-2,"Doston")
#print(friends)
#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
print("\nKelgan mehmonlar: ", mehmonlar)

























