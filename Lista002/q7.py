qntd_fita=int(input('Quantas fitas têm na locadora? '))
aluguel_fita=float(input('Quanto é o aluguel da fita? '))

# Quantidade de fitas que são alugadas
fitas_alugadas_mes=(qntd_fita/3)

# Quantidade de fitas que são devolvidas com atraso
fitas_com_atraso=fitas_alugadas_mes/10

# Preço do aluguel das fitas em atraso
aluguel_com_multa=aluguel_fita+aluguel_fita*0.1

# Dinheiro ganho somente com multa
ganho_com_multa= fitas_com_atraso*(aluguel_fita*0.1)

# Quantidade de fitas que a locadora terá no final do ano
fitas_estragadas=qntd_fita*0.02
reposicao_fitas=qntd_fita/10
qntd_fita_final=int(qntd_fita-fitas_estragadas+reposicao_fitas)

# Faturamento total da locadora
faturamento_total=(((fitas_alugadas_mes-fitas_com_atraso)*aluguel_fita)+fitas_com_atraso*aluguel_com_multa)*12

print ("O faturamento total da locadora no ano é R${}".format(faturamento_total))
print ("O valor ganho com multa por mês é R${}".format(ganho_com_multa))
print ("A quantidade de fitas que a locadora terá no fim do ano será {} fitas".format(qntd_fita_final))