import random

coordenadasLetras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
coordenadasNumeros = ["1","2","3","4","5","6","7","8","9","10"]
sorteio = []

sorteio1 = random.sample(coordenadasLetras, 4)

while True:
    sorteio2 = random.sample(coordenadasNumeros, 4)
    if int(sorteio2[1]) > 8:
        continue
    if int(sorteio2[2]) > 7:
        continue
    if int(sorteio2[3]) > 6:
        continue
    else:
        break


for i in range(len(sorteio1)):
    sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")

print(sorteio)


barcos = []

for a in range(len(sorteio)):
    if a == 0:
        for i in range(len(sorteio)):
             barcos.append(sorteio[i])

    if a == 1:
        print("\nCOMEÇA O 2")
        separado = list(sorteio[a])
        print(separado)
        barcos.append(f"{separado[0]}{int(separado[1])+1}")
        print(barcos)
        
    
    if a == 2:
        for i in range(2):
            print("\nCOMEÇA O 3")
            separado = list(sorteio[a])
            print(separado)
            barcos.append(f"{separado[0]}{int(separado[1])+(i + 1)}")
            print(barcos)

    if a == 3:
            for i in range(3):
                print("\nCOMEÇA O 4")
                separado = list(sorteio[a])
                print(separado)
                barcos.append(f"{separado[0]}{int(separado[1])+(i+1)}")
                print(barcos)
          