# solução EP6_3
import pandas as pd
import numpy as np 
# lemos um arquivo csv
df = pd.read_csv("pacientes.csv", sep = ";", decimal = "," )
# lemos duas colunas
coluna1 = input()
coluna2 = input()
# calculamos o coeficiente de correlação 
coefCorr = (df[coluna1]).corr(df[coluna2])
# calculamos o coeficiente de determinação 
coefDet = coefCorr**2
#  determinamos se a correlação é positiva, negativa ou nula
if coefCorr > 0:
    tipo = "Positiva"
elif coefCorr < 0:
    tipo = "Negativa"
else:
    tipo = "Nula"
# determinamos a intensidade da correlação
if coefCorr <= 0.29:
    intensidade = "Correlação muito fraca"
elif coefCorr <= 0.59:
    intensidade = "Correlação fraca"
elif coefCorr <= 0.79:
    intensidade = "Correlação moderada"
elif coefCorr <= 0.89:
    intensidade = "Correlação forte"
else:
    intensidade = "Correlação muito forte"
# imprimimos a correlação
print ("Coeficiente de correlação: %.2f" % coefCorr)
print ("Coeficiente de Determinação (R²): %.2f" % coefDet )
print("Tipo da correlação:", tipo)
print("Intensidade:", intensidade)