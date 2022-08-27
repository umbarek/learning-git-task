print("Zadanie_1")
print("")
lista = ("marchew", "seler", "rukola", "chleb", "pączek", "bułki")
sklep1 = { "warzywniak" : ["marchew","seler","rukola"] }
sklep2 = { "piekarnia" : ["chleb","pączek","bułki"] }
print("Lista zakupów:")
for nazwa in sklep1.keys():
    for rzecz in sklep1.values():
        print (f"Idę do {nazwa.capitalize()}, kupuję tu następujące rzeczy:", rzecz)
("")
for nazwa in sklep2.keys():
    for rzecz in sklep2.values():
        print (f"Idę do {nazwa.capitalize()}, kupuję tu następujące rzeczy:", rzecz)
lista = ("marchew", "seler", "rukola", "chleb", "pączek", "bułki")
print ("W sumie kupię ", len(lista),"produktów")
print ("To jest koniec zadania")