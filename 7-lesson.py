#Botirov Davron
import os
os.system('cls')
os.system('color 2')

class Country:
    def __init__(self, name, code, population, area):
        self.name = name
        self.code = code
        self.population = population
        self.area = area

    def density(self):
        return self.population / self.area

    def __str__(self):
        return f"Davlat: {self.name}\nKod: {self.code}\nAholisi: {self.population}\nYer maydoni: {self.area} km²\nZichligi: {self.density():.2f} kishi/km²"

countries = [
    Country("Ozbekiston", "UZ", 34636000, 448978),
    Country("Qozogiston", "KZ", 19233000, 2724900),
    Country("Qirgiziston", "KG", 6601000, 199951),
    Country("Tojikiston", "TJ", 10021000, 143100),
    Country("Turkmaniston", "TM", 6317000, 491210)
]
fayl = open ("davlatlar.txt","w")

for country in countries:
    print(country)
    print('-' * 30)
