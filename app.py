#Começando com Python
import csv

usuarios = []

with open('usuarios.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        usuarios.append(row)

busca = input('Digite o nome do usuário.: ')

if(busca):
    for element in usuarios:
        if(busca.upper() in element['DS_USUARIO'].upper()):
            file = open('ligacoes.csv','w')
            #print(f"{element['DS_USUARIO']} - {element['SETOR']}")





