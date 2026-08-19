# EP8_8.py
# recebemos um valor 1 <= N <= 100 que seria a quantidade de pessoas
N = int(input())
# criamos uma variavel para contar adultos e uma para somar as idades
adultos = 0
somaIdades = 0
# recebemos as idades das pessoas
for i in range (0, N):
  idade = int(input())
  somaIdades = somaIdades + idade
  if idade >= 18:
    adultos = adultos + 1
# calculamos a proporção de adultos e a média das idades de todas as N pessoas 
proporcaoAdultos = (adultos / N) * 100
mediaIdades = somaIdades / N
# imprimimos a mensagem com o resultado    
print(f"{proporcaoAdultos:.1f}%")
print(f"{mediaIdades:.1f}")    
