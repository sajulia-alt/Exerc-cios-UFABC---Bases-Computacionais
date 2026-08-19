# EP9_5.resolucao.py
# importa biblioteca que tem função para realizar tipos de sorteio
import random as rd
# recebemos quatro números inteiros que definem a seed do gerador aleatório, valor inicial disponível, valor de cada aposta e número de rodadas a serem jogadas
seed = int(input())
disponivel = int(input())
aposta = int(input())
rodadas = int(input())
# garantimos que a função seja reprodutível
rd.seed(seed)
# guarda dinheiro inicial
dinheiro = disponivel 
# calculamos o dinheiro restante após as apostas
for i in range (rodadas):
    if disponivel < aposta:
        break
    if disponivel >= aposta:
       resultado = rd.random()
       if resultado < 0.4:
        disponivel = disponivel + aposta
       else:
        disponivel = disponivel - aposta
# imprimimos o resultado
if disponivel > dinheiro:
  print (f"Lucro, ficando com {disponivel} reais")
elif disponivel < dinheiro:
  print (f"Prejuízo, ficando com {disponivel} reais")
else:
  print ("Saiu com o dinheiro inicial")