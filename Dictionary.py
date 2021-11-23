from Module import *
rus_list=loe_failist('rus.txt')
est_list=loe_failist('est.txt')
eng_list=loe_failist('eng.txt')
#print(rus_list)
#print(est_list)
#print(eng_list)

while True:
    menu=input('Tõlgida: T, \nUus sõna: U, \nViga: V,\nKontroll: K,\nLõpp: L\nSinu valik: ')
    if menu.upper()=='T':
        translate()
        #rus_list=loe_failist('rus.txt')
        #est_list=loe_failist('est.txt')
        #eng_list=loe_failist('eng.txt')
    if menu.upper()=='U':

        rus_list.clear()
        rus_list=loe_failist('rus.txt')
    if menu.upper()=='V':
        v=input('Keel: est või rus - ')
        if v=='rus':
            rus_list=correction(input('Введи слово: '),rus_list)

            failisse(rus_list, 'rus.txt')
    if menu.upper()=='K':
        pass
    if menu.upper()=='L':
        pass