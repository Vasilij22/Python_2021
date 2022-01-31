#Teksta datņu atvēršana, nolasīšana, aizvēršana

#1. veids
file = open("pirmais.txt", "r", encoding="utf-8")
print(file.read())
file.close()

#2.veids
with open("pirmais.txt", "r", encoding="utf-8") as file:
    print(file.read())
    file.close()

#Līnijas izvade
file = open("pirmais.txt", "r", encoding="utf-8")
print(file.readline())
file.close()

#Simbolu lasīšana
file = open("pirmais.txt", "r", encoding="utf-8")
print(file.read(15))
file.close()