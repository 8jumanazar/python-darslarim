"""
# 08- dars Ro'yxadlar bilan ishlash
       LISTS (Ro'yhadlar')
   sana : 09.09.2021
   Oquvchi ; Jumanazar Shokirov
"""

# Tartiblash
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort()
#print(cars)

# # Katta va kichik harf
#cars = ['Bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort()
#print(cars)

# # Teskari tartib
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.sort(reverse=True)
#print(cars)

# # SORTED 
#mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
#print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
#print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# # SONLI RO'YXADLAR
sonlar = (12,34,45,32,-7,-1,789)
#sonlar.sort()
#print(sorted (sonlar,reverse=Ture))

# # RO'YXADNI ORTIDAN BOSHLAB CHIQARISH 
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#cars.reverse()
#print(cars)

# # RO'YXAD UZUNLIGI
mevalar = ['Olma','Behi','Uzum','Shoftoli','Anor']
#print("Mevalar soni: ", len(mevalar))

# # RANGE()
sonlar = list(range(0,10))
#print(sonlar)

# # RENGE VA QADAM
#juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
#toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
#print("Juft sonlar: ", juft_sonlar)
#print("Toq sonlar: ", toq_sonlar)

# # MIN() , NAX() , SUM(),FUNKSIYALAR
narxlar = [1200,20000,3000,40000,70000,120000]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
#print("Eng arzon narximiz: ", arzon ,'ming, ' " Qimmat narximiz esa: ", qimmat , " Jami eas: ", jami)

# # RO'YXATNI KESISH
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
#my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
#print(my_cars) 
#print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
#print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# # RO'YHADDAN NUSXA OLISH  belgisi >>>[:]<<<
#sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
#sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
#sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
#sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
#print("Bu sonlar ro'yxati:", sonlar)
#print("Bu sonlar2 ro'yxati:", sonlar2)

sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
#print("Bu sonlar ro'yxati:", sonlar)
#print("Bu sonlar2 ro'yxati:", sonlar2)

my_cars = cars[:]
#print(my_cars)
my_cars.remove('bmw')
#print(my_cars)
#print(cars)

# # TUPLE
tomonlar = (20, 30, 55.2)
#print(tomonlar)

toys = ('bus','car','bear','dino','snake','lizard')
#print(toys[0])
#print(toys[-1])
#print(toys[2:5])

# # tuple ni list ga almashtirish
toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# Ro'yxatga o'zgartirishlar kiritamiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
print(toys)
