#Botirov Davron
import os
os.system('cls')
os.system('color 2')

n = input()
def max_son(n):
    if max_son(n)<2:
        raise ValueError()
    sonlar = list(set(sonlar))
    if len(sonlar)<2:
        raise ValueError()
    sonlar.sort(reverse=True)
    return sonlar[1]
n1 =max_son(n)
print (n) 
