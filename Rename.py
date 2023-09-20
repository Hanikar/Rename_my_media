import pathlib
import os
import os.path
import re
import time


def season_finder(folder:str) -> list:
    """Find the season of the anime/series by the folder name"""
    nome_da_season = str(folder).split()
    for i in nome_da_season:
        if i.isdigit() == True:
            season = i
            break
        else:
            season = 1
    return season


def corrects_name(files_list:list) -> (list, int):
    """Find and store the name of the files that is not right (will be changed)
    files_list:list -> Is the list of file names from the folder (excluding this script)
    return a list of names to be changed and the number of the last episode with the correct name
    """
    correct_names = [] #Nomes com o formato S[]E[] correto
    for item in files_list:
        if re.match("S[0-9]E[0-9][0-9].*", item) != None:
            correct_names.append(item)

    correct_names.sort()

    if correct_names == []:
        numero = 0
    else:
        auxiliar = correct_names[len(correct_names)-1].split('E')
        auxiliar2 = auxiliar[1].split('.')
        numero = int(auxiliar2[0]) #Numero do ultimo Ep já renomeado
    
    return correct_names, numero


def rename(files_list, correct_names, number):
    # Criando a lista de outliers
    nomes_a_renomear = [] #lista de outliers

    for value in files_list:
        if value in correct_names:
            continue
        else:
            nomes_a_renomear.append(value)

    for index, file_name in enumerate(nomes_a_renomear, start=numero+1):
        if index < 10:
            file_extention = os.path.splitext(file_name)
            source = folder + file_name
            new_file_name = f"S{season}E0{index}" + file_extention[1]
        else:
            file_extention = os.path.splitext(file_name)
            source = folder + file_name
            new_file_name = f"S{season}E{index}" + file_extention[1]
        
        destination = folder + new_file_name
        # Renaming the file
        os.rename(source, destination)
    
    print("Files renamed")
    time.sleep(5)
    quit()


if __name__ == '__main__':

    permission = input("Do you want to change ALL the names of the files on this directory? [y/n] \n>")
    if permission == "n":
        exit()

    #What folder we are?
    folder = str(pathlib.Path(__file__).parent.resolve()) + "\\"
    
    # What the season?
    season = season_finder(folder)
    
    # Get the list of files of the folder, remove the name of this script, and than sort the list
    lista_arquivos_pasta = os.listdir(folder)
    lista_arquivos_pasta.remove(os.path.basename(__file__))
    lista_arquivos_pasta.sort()

    # Get the names that need changing, and the number of the last episode with the correct name
    correct_names, numero = corrects_name(lista_arquivos_pasta)

    # Rename the files that need renaming and quit the script
    rename(lista_arquivos_pasta, correct_names, numero)
