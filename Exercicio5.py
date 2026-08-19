# EP7_5.py
import pandas as pd
# lemos o arquivo
df = pd.read_csv("P1P2TFaltas.csv")
# recebemos um numero inteiro que representa o indice do aluno (0 a 99)
indice = int(input())
# lemos as notas da Prova 1 , Prova 2 e Trabalho do aluno selecionado
p1 = df.loc[indice, "Prova 1"]
p2 = df.loc[indice, "Prova 2"]
trabalho = df.loc[indice, "Trabalho"] 
# guardamos as notas originais para o print final antes de alterá-las
p1_orig = p1
p2_orig = p2
# calculamos a media atual da Prova 1, Prova 2 e Trabalho
mediaAtual = (p1 + p2 + trabalho) / 3
# perguntamos se o aluno fez (S) ou nao fez (N) a recuperacao
recuperacao = input()
if recuperacao == "S":
  notaRec = float(input())
  # a nota de recuperacao deve ser de 0 a 100
  if 0 <= notaRec and notaRec <= 100:
    # a nota da recuperacao  substitui a menor entre a Prova 1 e Prova 2 (Trabalho não e substituído)
    if p1 < p2:
      p1 = notaRec
    else:
      p2 = notaRec 
# recalculamos a media 
mediaNova = (p1 + p2 + trabalho)/3 
# diferenca entre as medias
diferenca = mediaNova - mediaAtual
# analisamos o desempenho do aluno
if diferenca > 0:
    desempenho = "O aluno melhorou."
elif diferenca < 0:
    desempenho = "O aluno piorou."
else:
   desempenho = "O aluno manteve a média."
# imprimimos as notas originais da Prova 1, Prova 2 e Trabalho
if recuperacao == "S":
    print(f"Notas originais — Prova 1: {p1_orig}, Prova 2: {p2_orig}, Trabalho: {trabalho}")
    print(f"Média original: {mediaAtual:.2f}")
    print(f"Média após recuperação: {mediaNova:.2f}")
    print(desempenho)
    print(f"Diferença: {abs(diferenca):.2f} pontos")
else:
    print(f"Notas originais — Prova 1: {p1_orig}, Prova 2: {p2_orig}, Trabalho: {trabalho}")
    print(f"Média original: {mediaAtual:.2f}")
    print("O aluno manteve a média")