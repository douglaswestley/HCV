#Começando com Python
#Versao Procedural / Funcional
import csv
from datetime import datetime as dt

usuarios = []

def registra_ligacao(linha):
    with open('ligacoes.csv','a') as f:
        f.write(linha)
    

with open('usuarios.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        usuarios.append(row)
        
while(True):        
    busca = input('Digite o nome do usuário.: ')
    result = []
    cont=0
    if(busca):
    
        for element in usuarios:
            if(busca.upper() in element['DS_USUARIO'].upper()):
                print("[{0}] - {1} - {2}".format(cont,element['DS_USUARIO'],element['SETOR']))
                result.append(element)
                cont += 1
        if(len(result) > 0 ):
            escolha = int(input("Digite o número referênte a sua escolha.: "))
            print(f"Ligação registrada para {result[escolha]['DS_USUARIO']}")
            texto = f"\"{result[escolha]['NM_USUARIO']}\",\"{result[escolha]['DS_USUARIO']}\",\"{result[escolha]['SETOR']}\",\"{dt.now().strftime('%d/%m/%Y %H:%M')}\"\n"
            registra_ligacao(texto)
        else:
            print('Não existe nenhum usuário com o nome digitado!')
    
            
            
