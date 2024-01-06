#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 22:44:31 2024

@author: Solih
"""

davlatlar = ["Turkiya","Koreya","Iroq","Germaniya","Yaponiya"]
tur = []

for o in range(3):
    tur.append(input(f"Qayerga sayohat qilishni xohlaysiz? {o+1} "))
    
mavjud =[]
mavjudemas= []

for davlat in tur:
    if davlat in davlatlar:
        mavjud.append(davlat)
    else:
        mavjudemas.append(davlat)
        
if mavjudemas:
    print("Hozirda bu davlatga tur yo'q: ")
    for davlat in mavjudemas:
        print(davlat)
else:
    print("Barcha davlatlarga borishingiz mumkin🛶")