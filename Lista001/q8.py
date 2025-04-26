numero=123
primeiro_numero= int(numero/100)
segundo_numero= int((numero%100)/10)
terceiro_numero= numero%10
numero_invertido=((terceiro_numero*100)+(segundo_numero*10)+primeiro_numero)


print(numero_invertido)