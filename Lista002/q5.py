tempo_viagem = int(input("Quantas horas durou a viagem? "))
velocidade_media= int(input("Qual velocidade média percorrida? Em KM/h: "))
distancia=velocidade_media*tempo_viagem
combustivel_gasto=distancia/12

print('Velocidade média: {}Km/h'.format(velocidade_media))
print('Tempo gasto: {} hora(s)'.format(tempo_viagem))
print('Distancia percorrida: {}Km,'.format(distancia))
print('Combustível gasto: {} litros'.format(combustivel_gasto))