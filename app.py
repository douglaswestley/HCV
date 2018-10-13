#Começando com Python
import csv

usuarios = []

def registra_ligacao(linha):
    with open('ligacoes.csv','a') as f:
        f.write(linha)
    

with open('usuarios.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        usuarios.append(row)

busca = input('Digite o nome do usuário.: ')

if(busca):
    for element in usuarios:
        if(busca.upper() in element['DS_USUARIO'].upper()):
            texto = f"\"{element['NM_USUARIO']}\",\"{element['DS_USUARIO']}\",\"{element['SETOR']}\"\n"
            print(texto)
            registra_ligacao(texto)
            
