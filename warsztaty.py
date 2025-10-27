
# Zadanie 1 — Porównanie wieku
"""
Poproś użytkownika o dwa wieki (liczby całkowite): wiek Michała i wiek Ani.
Wypisz:
1) czy Michał jest starszy od Ani,
2) czy Ania jest młodsza lub równa wiekiem Michałowi,
3) czy mają tyle samo lat.
Użyj operatorów: >, <=, ==.
"""

# age_ania = int(input("podaj wiek ani: "))
# age_michal = int(input("podaj wiek Michała: "))
#
# print(f"czy Michał jest starszy od Ani?: {age_michal > age_ania}")
# print(f"czy Ania jest młodsza lub ma tyle samo lat co Michał: {age_ania <= age_michal}")
# print(f"Czy Ania i Michał maja tyle samo lat? : {age_ania == age_michal}")




# Zadanie 2 — Porównanie cen owoców
"""
Poproś użytkownika o trzy ceny (liczby zmiennoprzecinkowe w zł): jabłka, pomarańczy i banana.
Wypisz:
1) czy jabłko jest tańsze od pomarańczy,
2) czy pomarańcza jest droższa od banana,
3) czy jabłko i banan kosztują tyle samo,
4) czy jabłko jest tańsze od pomarańczy lub równe bananowi,
5) czy pomarańcza jest droższa od jabłka i banana jednocześnie.
"""
#
# banana = float(input("podaj cenę banana: "))
# orange = float(input("podaj cenę pomarańczy: "))
# apple = float(input("podaj cenę jabłka: "))
#
# print(f"czy jabłko jest tańsze od pomarańczy?:{apple < orange} ")
# print(f"czy pomarańcza jest droższa od banana?:{orange > banana} ")
# print(f"czy jabłko i banan kosztuja tyle samo?:{apple == banana} ")
# print(f"czy jabłko jest tańsze od pomarańczy lub równe bananowi?:{banana == apple or apple  < orange } ")
# print(f"czy pomarańcza jest droższa od jabłka i banana :{apple < orange > banana } ")

# Zadanie 3 — Logiczne fakty o pogodzie
"""
Poproś użytkownika o 3 wartości logiczne jako 0 lub 1:
- jest_cieplo
- pada_deszcz
- wieje_wiatr

Wypisz:
1) czy jest dobra pogoda na spacer (ciepło i nie pada),
2) czy lepiej zostać w domu (nie jest ciepło lub pada),
3) czy pada albo wieje,
4) czy nie pada,
5) czy jest ciepło, ale nie pada i nie wieje.
"""
#
#
# print("ODPOWIEDZI WPROWADZAĆ W POSTACI 0/1")
# hot_status = bool(int(input("Czy jest ciepło na dworze?")))
# rain_status = bool(int(input("Czy na dworze pada deszcz?")))
# windy_status = bool(int(input("Czy na dworze wieje wiatr?")))
#
# print(hot_status)
# print(rain_status)
# print(windy_status)
#
# print(f"Czy jest dziś dobra pogoda na spacer?: {hot_status == True and rain_status == False }")
# print(f"Czy lepiej dziś zostać w domu (nie jest ciepło lub pada)?: {hot_status == False or rain_status == True}")
# print(f"Czy dziś pada lub wieje?: {rain_status == True or windy_status == True }")
# print(f"Czy nie pada?: {not rain_status}")
# print(f"Czy jest dziś ciepło nie pada i nie wieje?: {hot_status == True and rain_status == False and windy_status == False}")
#



# Zadanie 4 — Typy i konwersje z wejścia
"""
Poproś użytkownika o wiek (tekst) i wagę (tekst, np. '72.5').
Następnie:
- skonwertuj wiek na int, wagę na float,
- dodaj 5 do wieku,
- dodaj 2.3 do wagi,
- wypisz nowe wartości oraz ich typy.
"""
#
# age = input("proszę podaj swój wiek: ")
# weight = input("prosze podaj swoją wage: ")
#
# print(type(age), type(weight))
#
# age = int(age)
# weight = float(weight)
#
# print(type(age), type(weight))
#
# age += 5
# weight += 2.3
#
# print(type(age), type(weight))
# print(age,weight)
#

# Zadanie 5 — Cukierki dla dzieci
"""
Poproś użytkownika o liczbę cukierków i liczbę dzieci.
Policz i wypisz:
- ile cukierków dostanie każde dziecko (//),
- ile cukierków zostanie (%),
- czy cukierków wystarczy dla wszystkich dzieci (cukierki >= dzieci),
- czy cukierków jest mniej niż 10 lub więcej niż 100.
"""



#
# candies = int(input("Podaj liczbę cukierów dla dzieci: "))
# num = int(input("Podaj liczbę dzieci: "))
#
# print(f"Kazde dziecko dostanie {int(candies / num)} cukierków")
# print(f"zostanie {candies % num} cukierków")
# print(f"czy cukierkow wystarczy dla wszystkich?: {candies >= num }" )
# print(f"czy cukierków jest mniej niż 10 lub więcej niż 100?: {candies <= 10 or candies >= 100 }")
#


# Zadanie 6 — Koszyk PRO: budżet i logika zakupów
"""
Poproś użytkownika o:
- cenę i liczbę sztuk trzech produktów (A, B, C),
- dostępny budżet w zł.

Oblicz i wypisz:
1) łączną wartość koszyka,
2) czy mieści się w budżecie,
3) czy istnieje para produktów o tej samej cenie,
4) czy łączna liczba sztuk > 10,
5) czy żadna cena nie jest 0,
6) czy budżet wystarcza i wszystkie ceny > 0,
7) czy jakiś produkt jest co najmniej 2× droższy od innego.
# """



prod_A = int(input("podaj liczbę sztuk produktu A: "))
price_A = float(input("podaj cenę produktu A: "))
prod_B = int(input("podaj liczbę sztuk produktu B: "))
price_B = float(input("podaj cenę produktu B: "))
prod_C = int(input("podaj liczbę sztuk produktu C: "))
price_C = float(input("podaj cenę produktu C: "))

budget = float(input("Jaki jest dostepny budżet?: "))

total = round(prod_A*price_A + prod_B*price_B + prod_C*price_C , 2)
prod_sum = prod_A + prod_B + prod_C
price_not_zero = bool(price_A != 0 and price_B != 0 and price_C != 0)

print(f"łączna wartość koszyka to {total}")
print(f"suma Większa niż budżet?: {total > budget}")
print(f"czy istnieje para produktów o tej samej cenie?: {price_A == price_B or price_B == price_C or price_C == price_A}")
print(f"liczba produktów większa od 10?: {prod_sum > 10}")
print(f"czy cena żadnego z produktów nie jest równa 0?: {price_A != 0 or price_B != 0 or price_C != 0} ")
print(f"czy budżet wystarczy i czy żadna cena nie jest zerem?: {budget > total and price_not_zero}")
print(f"czy jakis produt ejst 2x droższy od innego?: ")




# print(f"łączna wartość koszyka: {total}")
# # print(f"czy zakupy mieszczą się w budżecie?:{} ")


# Zadanie 7 — Bilety, zniżka i warunki zakupu
"""
Poproś użytkownika o:
- cenę jednego biletu,
- liczbę biletów,
- procent zniżki,
- kwotę w portfelu,
- maksymalną akceptowalną cenę za 1 bilet po zniżce.

Oblicz:
- koszt całkowity po zniżce,
- cenę 1 biletu po zniżce.

Wypisz:
1) koszt po zniżce,
2) czy użytkownika stać na zakup,
3) czy zniżka jest co najmniej 15%,
4) czy liczba biletów jest parzysta,
5) czy cena 1 biletu po zniżce ≤ limit,
6) warunek złożony: stać na zakup oraz (zniżka ≥15% lub liczba biletów parzysta).
"""