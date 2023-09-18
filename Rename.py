import pathlib
import os
import os.path
import re

pasta = pathlib.Path(__file__).parent.resolve()
folder = str(pasta) + "\\"
count = 1
nome_da_season = str(pasta).split()

permission = input("Do you want to change ALL the names of the files on this directory? [y/n] \n>")
if permission == "n":
    exit()

for i in nome_da_season:
    if i.isdigit() == True:
        season = i
        break
    else:
        season = 1

name_list = []

# Debbug
# print(f"Season {season}")

# print(os.listdir(folder))
# Fim Debbug

lista_arquivos_pasta = os.listdir(folder)
lista_arquivos_pasta.remove("nomes.py")
lista_arquivos_pasta.sort()

nomes_corretos = [] #Nomes com o formato S[]E[] correto
for item in lista_arquivos_pasta:
    if re.match("S[0-9]E[0-9][0-9].*", item) != None:
        nomes_corretos.append(item)

nomes_corretos.sort()
# print("*" * 80)
# print(nomes_corretos)
# print("*" * 80)

if nomes_corretos == []:
    numero = 0
else:
    auxiliar = nomes_corretos[len(nomes_corretos)-1].split('E')
    auxiliar2 = auxiliar[1].split('.')
    numero = int(auxiliar2[0]) #Numero do ultimo Ep já renomeado

# Criando a lista de outliers
nomes_a_renomear = [] #lista de outliers
for value in lista_arquivos_pasta:
    if value in nomes_corretos:
        continue
    else:
        nomes_a_renomear.append(value)

for index, file_name in enumerate(nomes_a_renomear, start=numero+1):
    if index < 10:
        name_list.append(file_name)
        file_extention = os.path.splitext(file_name)
        source = folder + file_name
        new_file_name = f"S{season}E0{index}" + file_extention[1]
    else:
        name_list.append(file_name)
        file_extention = os.path.splitext(file_name)
        source = folder + file_name
        new_file_name = f"S{season}E{index}" + file_extention[1]

    destination = folder + new_file_name

    # Renaming the file
    os.rename(source, destination)


print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)

print("*" * 80)
print(name_list)
input("\n> ")
