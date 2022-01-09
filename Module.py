def loe_failist(f)->list:
    fail=open(f,'r',encoding='utf-8-sig')
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def uus_sona(file1:str,file2:str,file3:str,x:str)->list:
    mas=[]
    with open(file,'a') as f:
        f.write(x+'\n')
    mas=loe_failist(file)   
    return mas

def checklang (s1,s2): #s1-russian
    ru=list(map(ord,list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')))
    en=list(map(ord,list('abcdefghiklmnopqrstvxyz')))
    text=input('Please enter your word ').lower()
    text1=list(map(ord,list(text)))
    check = 0
    for i in text1:
        if i in en:
            check+=1
    if check == len(text1):
        eng=text
        print ('english ',eng)
    check1=0
    for i in text1:
        if i in ru:
            check1+=1
    if check1==len(text1):
        rus=text
        print ('russian ', rus)
    if text !='eng' or text!='rus':
        print (f'{text} is not in dict')
        f=input('Do you want to add? 1 - for yes, 0 - for no ')
        if f==1:
            if text=='eng':
                s2.append(text)
                s1.append(input('Enter translation '))
            elif text=='rus':
                s1.append(text)
                s2.append(input('Enter translation '))
        elif f==0:
            print('Thank you')
    if text in s1:
        print(f'{text}-{s2[s1.index(text)]}')
    elif text in s2:
        print(f'{text}-{s1[s2.index(text)]}')
    else:
        (f'{text} is not in dict')

def translate()->str:
    word=input('Sisesta sõnu, mis on vaja tõlgida: ')
    rus_list=loe_failist('rus.txt')
    est_list=loe_failist('est.txt')
    eng_list=loe_failist('eng.txt')
    if word in rus_list:
        wordInd=rus_list.index(word)
        print(est_list[wordInd])
        print(eng_list[wordInd])
        print()
    elif word in est_list:
        wordInd=est_list.index(word)
        print(rus_list[wordInd])
        print(eng_list[wordInd])
        print()
    elif word in eng_list:
        wordInd=eng_list.index(word)
        print(rus_list[wordInd])
        print(est_list[wordInd])
        print()
    else:
        print('Этого слова нет в словаре')
    
    return word

def correction(sona:str,mas:list)->list:
    #mas=[]
    print(mas)
    for i in range(len(mas)):
        if mas[i]==sona:       
            uus_sona=sona.replace(sona, input('Uus sõna: '))
            mas.insert(i, uus_sona)
            mas.remove(sona)
            print(mas)
    return mas

def failisse(mas:list, file:str):
    pass

def loe_fail(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    print(mas)
    return mas

def kirjuta_fail(f,rida):
    fail=open(f,'a',encoding='utf-8-sig')
    fail.write(rida+'\n')
    fail.close()

def tolkimine(s1,s2):
    text=input('text: ')
    if text in s1:
        print(f'{text}-{s2[s1.index(text)]}')
    elif text in s2:
        print(f'{text}-{s1[s2.index(text)]}')
    else:
        print(f'{text} is not in dict')

def checklang (s1,s2): #s1-russian
    ru=list(map(ord,list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')))
    en=list(map(ord,list('abcdefghiklmnopqrstvxyz')))
    text=input('Please enter your word ').lower()
    text1=list(map(ord,list(text)))
    check = 0
    for i in text1:
        if i in en:
            check+=1
    if check == len(text1):
        eng=text
        print ('english ',eng)
    check1=0
    for i in text1:
        if i in ru:
            check1+=1
    if check1==len(text1):
        rus=text
        print ('russian ', rus)
    if text !='eng' or text!='rus':
        print (f'{text} is not in dict')
        f=input('Do you want to add? 1 - for yes, 0 - for no ')
        if f==1:
            if text=='eng':
                s2.append(text)
                s1.append(input('Enter translation '))
            elif text=='rus':
                s1.append(text)
                s2.append(input('Enter translation '))
        elif f==0:
            print('Thank you')
    if text in s1:
        print(f'{text}-{s2[s1.index(text)]}')
    elif text in s2:
        print(f'{text}-{s1[s2.index(text)]}')
    else:
        (f'{text} is not in dict')
