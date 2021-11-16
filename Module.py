def loe_failist(f)->list:
    fail=open(f,'r',encoding='utf-8-sig')
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def uus_sona(file:str,x:str)->list:
    mas=[]
    with open(file,'a') as f:
        f.write(x+'\n')
    mas=loe_failist(file)
    return mas

def translate()->str:
    word=input('Sisesta sõnu, mis on vaja tõlgida: ')
    rus_list=loe_failist('rus.txt')
    est_list=loe_failist('est.txt')
    eng_list=loe_failist('eng.txt') 
    return word

