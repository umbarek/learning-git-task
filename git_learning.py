print("Zadanie_1")
print("")
lista = ("marchew", "seler", "rukola", "chleb", "pączek", "bułki", "sałata", "kapusta", "drozdzówka", "ciasto", "ibuprom")
sklep1 = { "warzywniak" : ["marchew","seler","rukola", "sałata", "kapusta"]}
sklep2 = { "piekarnia" : ["chleb","pączek","bułki", "drozdzówka", "ciasto"]}
sklep3 = {"apteka" : ["ibuprom"]}
print("Lista zakupów:")
for nazwa in sklep1.keys():
    for rzecz in sklep1.values():
        print (f"Idę do {nazwa.capitalize()}, kupuję tu następujące rzeczy:", rzecz)
("")
for nazwa in sklep2.keys():
    for rzecz in sklep2.values():
        print (f"Idę do {nazwa.capitalize()}, kupuję tu następujące rzeczy:", rzecz)
("")
for nazwa in sklep3.keys():
    for rzecz in sklep3.values():
        print (f"Idę do {nazwa.capitalize()}, kupuję tu następujące rzeczy:", rzecz)
print ("W sumie kupię ", len(lista),"produktów")
print ("To jest koniec zadania")
# Specjalne pozdrowienia dla Mentora!