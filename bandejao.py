import urllib.request
fim = 0

def recuperaPrato(refeicao,turno):
    global fim
    tamanho = len(refeicao)
    inicio = texto.find(refeicao,fim)
    fim = texto.find('<',inicio)
    prato = texto[inicio+tamanho+2:fim]
    print(refeicao + ": " + prato)
    


pagina = urllib.request.urlopen('http://www2.ufscar.br/servicos/restaurantes.php')
texto = pagina.read().decode('iso8859')
cardapio = ["Prato Principal", "Guarnição", "Arroz", "Feijão", "Saladas", "Sobremesa", "Bebida"]
dataInicio = texto.find("HOJE")
dataFim = texto.find('<', dataInicio)
dataHoje = texto[dataInicio+5:dataFim]
print("Cardápio do dia " + dataHoje)
print("--------------------------- \n")
print("Almoço \n")
for i in range(len(cardapio)):
    recuperaPrato(cardapio[i],0)
print("\nJantar \n")
for i in range(len(cardapio)):
    recuperaPrato(cardapio[i],0)
    
a = input("\nPressione qualquer tecla para sair...")
