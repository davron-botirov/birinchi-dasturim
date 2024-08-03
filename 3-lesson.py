#Botirov Davron
import os
import random
os.system('cls')
os.system('color 2')

list = [2, 4, 6, 8, 10]
input = int(input("1 dan 10 gacha bo'lgan son kiriting: "))
if input in list:
    index = list.index(input)
    print(f"{input} sonining ro'yxatdagi indeksi: {index}")
else:
    print(f"Ro'yxatda {input} soni mavjud emas.")