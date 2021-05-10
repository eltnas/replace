import os

files = os.listdir('.')
numero = int(input("Numero: "))

print(len(files))

for i in range(0, len(files)):
    file = files[i]
    print(i)
    
    novoNome = '{:02d}'.format(numero) + ' - ' + file
    print(novoNome)
    os.rename(file, novoNome)
    print(file + ' -> ' + novoNome)