# 1)

def asendente (dic):

    valores = []

    for i in dic.values():
        
        if type(i) == int :

            valores.append(i)

    valores.sort()
    print(valores)

dic = {
    "A":90,
    "B":17, 
    "C":30,
    "D":"JOSE",
    "E":24.5
}

#asendente(dic)

# 2)

def dos_dic (dic1,dic2):

    claves_comunes = dic1.keys() & dic2.keys()
    num_comun = 0

    for claves in claves_comunes:

        if dic1[claves] == dic2[claves]:
            
            num_comun += 1

    if len(dic1) == num_comun :

        print("todas la claves y valores en el primer diccionario estan en el segundo")

    else:

        print("no todas la claves y valores en el primer diccionario estan en el segundo")


dic1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dic2 = {
    "A": 10,
    "B": 25,
    "C": 30,
    "D": 40
}

dic3 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dic4 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

#dos_dic (dic1,dic2)
#dos_dic (dic3,dic4)

# 3)


def mezcla (dicc1,dicc2):

    mix ={}

    claves_en_comun = dicc1.keys() & dicc2.keys()

    for cla in claves_en_comun:

        del dicc2[cla]

    for clave,valor in dicc1.items():

        mix[clave]=valor

    for clave,valor in dicc2.items():

        mix[clave]=valor

    print(mix)

dicc1 = {
    "A": 1,
    "B": 26,
    "C": 30,
    "D": 40,
    "I": 35
}

dicc2 = {
    "A": 10,
    "B": 20,
    "F": 60,
    "G": 70,
    "H": 80,
    "I": 90,
    "J": 100,
    "K": 110
}

#mezcla(dicc1,dicc2)

# 4)

def per (lista):

    for i in lista:

        if 18 <= i["edad"] <= 30:
            
            print(i)

    

personas = [{"nombres":"kenny","apellidos":"vargas ruiz","edad":23},
            {"nombres":"dilan felipe","apellidos":"Diaz mesa","edad":35},
            {"nombres":"allan yesid","apellidos":"vargas ruiz","edad":18}]

per(personas)

