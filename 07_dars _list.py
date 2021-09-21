#  Jumanazar Shokirov
"""
#   07- DARS   LIST (RO'YXAT)
#  Sana: 06.09.2021

"""

# List quyidagicha yoziladi:

mevalar = ['olma', 'anjir','shaftoli']
narhlar = [12000,18000,10900,22000]
sonlar = ["bir","ikki",3,4,5,6]
ismlar = [] # bo'sh holat qoldirish

# list elementlari
# Dasturlash olamida indeks 0 dan boshlanadi!!! Ya'ni Listning birinchi elementing tartib raqami (indeksi) 0 ga, ikkinchi elementning indeksi 1 ga teng va hokazo. 

mevalar = ['olma', 'anjir', 'shaftoli'] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])


# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llashimiz mumkin:

mevalar = ['olma','anjir','shaftoli']
print("Birinchi meva:", mevalar[0].title())# Bosh harif katta ko'rinishda
print("Ikkinchi meva:", mevalar[1].upper())# Hamma harif katta ko'rinishda

#Pythonda Listning eng oxirgi elementiga -1 indeksi orqali ham murojat qilish mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

#ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)

# Yangi elemen qo'shish
mevalar = ['olama', 'anjir']
mevalar.append("tarvuz")# ohriga element qo'shish
mevalar.insert(0, 'behi')#istalgan joyga 

cars = []
cars.append('Damas')
cars.append("Cobalt")
cars.append('Jip')

# Elementlarni o'chirish
cars = ['Damas','Cobalt','Jip']
del cars[0]

# REMOVE metodi yordamida element qiymatini o'chirish

mevalar = ['olma','anjir','behi','anor','anjir']
mevalar.remove('anjir')

# Elementni sug'urib olish

bozorlik = ['un','pioz',"yog'",'non']
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot + " sotib oldim")
print("Olinmadi:",bozorlik)










