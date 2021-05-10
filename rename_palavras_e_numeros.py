import os

files = os.listdir('.')
new = input("Acrescenta: ")

print(len(files))

for i in range(0, len(files)):
    file = files[i]
    print(i)
    
    novoNome = new + ' - ' + file
    print(novoNome)
    os.rename(file, novoNome)
    print(file + ' -> ' + novoNome)