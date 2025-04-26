# Questao 4 - Matheus Silveira e Marcos Brandão

print('Calculador de Salário de Professor')
print('---------------------------------')
valor_hora=float(input("Digite o Valor de sua hora aula: "))
aulas_mes=int(input("Quantas aulas você deu no mês? "))
percentual_inss=float(input("Qual o percentual de desconto do INSS que você paga? "))
horas_trabalhadas=(aulas_mes*50)/60
salario_bruto=(horas_trabalhadas*valor_hora)
desconto_inss=salario_bruto*percentual_inss/100
salario_liquido=salario_bruto-desconto_inss
print('Você trabalhou {} horas. Você receberá R${} de salário'.format(horas_trabalhadas,salario_liquido))