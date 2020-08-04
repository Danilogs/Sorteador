from random import*
from Amigos import*
dicionario_de_pessoas={}
lista_de_pessoas=[]
pessoas=int(raw_input("Quantas pessoas participaram:? "))
for i in range(pessoas):
    nome=raw_input("Qual o nome?: ")
    numero=raw_input("Qual o numero?: ")
    modelo=raw_input("Qual o modelo?: ")
    pessoinha=Pessoa(nome,numero,modelo)
    dicionario_de_pessoas[nome]=pessoinha
    lista_de_pessoas.append(nome)
for j in dicionario_de_pessoas:
    num_sorteado=randrange(0,len(lista_de_pessoas))
    sorteado=lista_de_pessoas[num_sorteado]
    if sorteado==j:
        while sorteado==j:
            num_sorteado=randrange(0,len(lista_de_pessoas))
            sorteado=lista_de_pessoas[num_sorteado]
    objeto=dicionario_de_pessoas[j]
    objeto.sorte.append(sorteado)
    lista_de_pessoas.remove(sorteado)

for k in dicionario_de_pessoas:
    arquivo= k+".txt"
    arquivando=open(arquivo,"w")
    for l in dicionario_de_pessoas[k].sorte:
        amigo= dicionario_de_pessoas[l].name
        numerinho= dicionario_de_pessoas[l].number
        modelinho=dicionario_de_pessoas[l].model
        novo=" Voce tirou: "+ amigo+"\n"
        novo1= "Com o numero de calcado: "+ numerinho+"\n"
        novo2= "Com o modelo desejado: "+modelinho+"\n"
         
        arquivando.write(novo)
        arquivando.write(novo1)
        arquivando.write(novo2)
        arquivando.close()

print "Encerrou"
        
    
    
