conta_corrente=int(input("Digite os três dígitos da sua conta corrente: "))

# Separando a conta corrente
primeiro_conta_corrente=int(conta_corrente/100)
segundo_conta_corrente=int((conta_corrente%100)/10)
terceiro_conta_corrente=(conta_corrente%10)

# Calculando o dígito verificador
# Inverso da conta corrente
inverso_conta_corrente=terceiro_conta_corrente*100+segundo_conta_corrente*10+primeiro_conta_corrente

# 1- Somar o numero da conta corrente com inverso dela: Soma1
soma_conta_corrente_com_inverso=conta_corrente+inverso_conta_corrente

# 2- Pegando somente os últimos três numeros da soma da conta corrente com o inverso dela
ultimos_tres=soma_conta_corrente_com_inverso%1000

# 2- Separando a soma da conta corrente com o inverso dela
primeiro_dasoma=int(ultimos_tres/100)
segundo_dasoma=int((ultimos_tres%100)/10)
terceiro_dasoma=(ultimos_tres%10)


# 3- Multiplicando numeros da Soma1 pela sua posição e depois somando-os
soma2=(primeiro_dasoma*1)+(segundo_dasoma*2)+(terceiro_dasoma*3)

# 4- O dígito verificador é a unidade da soma2
digito_verificador=soma2%10

print("Seu dígito verificador é {}".format(digito_verificador))