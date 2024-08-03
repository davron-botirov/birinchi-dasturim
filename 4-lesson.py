#Botirov Davron
import os
os.system('cls')
os.system('color 2')
son1 = {"key1": 1, "key2": 3, "key3": 2}
son2 = {"key1": 1, "key2": 3 }
for key in son1:
    if key in son2:
        if son1[key] == son2[key]:
            print(key, son1[key])
