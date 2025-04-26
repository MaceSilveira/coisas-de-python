import math

volume_pote=15*10*13
volume_esfera=math.pi*1.2**3*4/3 
fator_empacotamento=0.74
esfera_nopote= int((0.74*volume_pote)/volume_esfera)

print("Cabem", esfera_nopote, "esferas no pote")