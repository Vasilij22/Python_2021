import json

vards = input('ievadiet vardu: ')
uzvards = input('ievadiet uzvardu: ')
vecums = input('ievadiet vecumu: ')
tel_nr = input('ievadiet telefona numuru: ')

vardnica = {
    'Vards':vards,
    'Uzvards':uzvards,
    'Vecums':vecums,
    'Telefona Numurs':tel_nr
}

def dati(vards,uzvards,vecums,tel_nr):
    with open('ievaktieDati.json','a',encoding='utf-8') as outfile:
        
        json.dump(vardnica,outfile,indent=4,ensure_ascii=False)

dati(vards,uzvards,vecums,tel_nr)
