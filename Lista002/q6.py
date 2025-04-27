print ('***CALCULADOR DE PRESTAÇÃO***')
print ('-----------------------------')
valor_emprestimo=float(input("Quanto você pegou de empréstimo? "))
taxa_juros=float(input("Qual a taxa de juros? "))
qntd_meses=int(input("Quantos meses você vai pagar? "))
taxa_juros=taxa_juros/100
valor_parcela=valor_emprestimo*((taxa_juros*(1+taxa_juros)**qntd_meses)/((1+taxa_juros)**qntd_meses-1))

print ('O valor da parcela é R${} por mês'.format(valor_parcela))