import sys
import os
import time
from recomendation import *
##############################################################################################################################
def escrevaMenu():
    print ("\n\t\t\tSistema de Recomendação\n\n")
    print ("\t1 - Acessar Perfil")
    print ("\t2 - Criar Novo Perfil")
    print ("\t3 - Sair")
#################################################################################################################################################################
def escrevaMenuPerfil():
    tempo()
    clear()
    print ("\n\t\t\t::::Menu de usuário::::\n\n")
    print ("\t1 - Histórico de filmes")
    print ("\t2 - Adicionar filme")
    print ("\t3 - Excluir filme")
    print ("\t4 - Filmes recomendados")
    print ("\t5 - Mudar nota")
    print ("\t6 - Excluir perfil")
    print ("\t7 - Voltar ao menu principal")
######################################################################################################################################################################
def criarPerfil ():
    clear()
    print("\t\t\t::::Novo Usuário::::\n\n")
    print ("Digite seu nome de usuário: ")
    name = input("")
    validarNewUser = newUser(name)
    while (validarNewUser != True ):
        print ("Nome já existente, crie um novo: ")
        name = input ("")
        validarNewUser = newUser(name)
    
    #adicionar no dicionario ()()()()
    print ("Deseja adicionar um filme a sua lista?")
    print ("1 - Sim")
    print ("2 - Não")
    choice = input ()
    while ((choice!="1")and (choice != "2")):
        print ("Opção inválida! Digite novamente: ")
        choice = input("")
    if (choice == "1"):
        print("Filmes disponíveis: ", avaliacoesModel['Model'])
        movie = input("Qual o filme: \n")
        validarMovies = addMovie(movie, name)
        while (validarMovies != True ):
            print ("Filme não encontrado, tente outro: ")
            movie = input ("")
            validarMovies = addMovie(movie, name)
        while (choice == "1"):
            print("Deseja adicionar mais um filme?")
            print("1 - Sim")
            print("2 - Não")
            choice = input("")
            if (choice == "1"):
                print("Filmes disponíveis: ", avaliacoesModel['Model'])
                movie = input("Qual o filme: \n")
                validarMovies = addMovie(movie, name)
                while (validarMovies != True ):
                    print ("Filme não encontrado, tente outro: ")
                    movie = input ("")
                    validarMovies = addMovie(movie, name)
    print ("Usuário cadastrado com sucesso!\n\n\n\n\n")
    Menu()


#############################################################################################################################################
def excluirPerfil(user):
    clear()
    resp = False
    print ("\nTem certeza? sim ou nao")
    comand = input ("")
    while (resp!= True):
        clear()
        if (comand=="sim"):
            print ("\n\t\t\tO usuário ", user, "foi deletado!")
            del avaliacoesUsers[user]
            x = input("")
            return True
        elif(comand=="nao"):
            print("\n\t\t\tUsuário não excluído")
            x = input("")
            return False
        elif ((comand!="sim") and (comand!="nao")):
            clear()
            print("\nDeseja excluir seu perfil? sim ou nao")
            comand = input ("")
            
#############################################################################################################################################
def excluirFilme(user):
    if (len(avaliacoesUsers[user])==0):
        print("\n\t\t\tNão há filmes para serem excluídos")
        tempo()
        x = input("")
        clear()
        return False
    else:
        print("\n\nQual filme deseja deletar?")
        movieDel = input("")
        for item in avaliacoesModel.items():
            if (movieDel in avaliacoesModel['Model']):
                if (movieDel in avaliacoesUsers[user]):    
                    del avaliacoesUsers[user][movieDel]
                    clear()
                    print ("\n\t\t\tFilme Excluído!")
                    x=input("")
                    return True
                else: 
                    clear()
                    print("\n\t\t\tUsuário ainda não assistiu este filme!")
                    tempo()
                    x = input("")
                    return False
            else: 
                clear()
                print ("\n\t\t\tFilme não encontrado!")
                tempo()
                x = input("")
                return False

######################################################################################################################################
def mudarNota(user):
    if (len(avaliacoesUsers[user])==0):
        print("\n\t\t\t Não há filmes no histórico")
        tempo()
        x = input("")
        return()
    else:
        clear()    
        for item in avaliacoesUsers[user].items(): 
                print(item)
        print ("Deseja mudar nota de qual filme?\n\n")
        movie = input("")
        if (movie in avaliacoesUsers[user]):
            clear()
            print ("\n Qual a nova nota desse filme?")
            nota = float (input(""))
            validar = False
            while (validar != True):
                if ((nota >= 0.0) and (nota<=5.0)):
                    validar = True
                    avaliacoesUsers[user][movie] = nota
                    clear()
                    print ("\n\t\t\tFilme modficado!")
                    x = input("")
                    return()
                else: 
                    print("\n\t\t\tNota inválida!")
                    clear()
                    print ("Qual a nova nota desse filme? (0.0 - 5.0)")
                    nota = float (input(""))
        else:
            clear()
            print ("Filme não encontrado!")
        x = input("")
        return()
    
########################################################################################################################################################################

def filmesRecomendados (user):
    recom = getRecomUser(avaliacoesUsers, user)
    if (len(avaliacoesUsers[user])==0):
        for item in avaliacoesModel['Model']:
            print (item)
        x = input("")
    else:    
        if (len(recom) == 0):
            clear()
            print ("\n\n\t\t\tSem filmes para recomendar!")
            x = input("")
        else: 
            for i in range (len(recom)):
                print (recom [i])
            x = input("")
###########################################################################################################################################
    # cria um novo usuário
def newUser (user):
    for item in avaliacoesUsers.items():
        if (user in avaliacoesUsers):
            return False
    avaliacoesUsers[user] = {}
    return True
##############################################################
##verifica se o usuário existe
def userExiste (user):
    for item in avaliacoesUsers.items():
        if (user in avaliacoesUsers):
            return True
    return False
##############################################################
## Adicio novo filme############
def addMovie(movie, user):
    for item in avaliacoesModel.items():
        if (movie in avaliacoesModel['Model']):
            if (movie in avaliacoesUsers[user]):
                x = input("")
                return False
            else: 
                avaliacoesUsers[user][movie] = 0.0
                print ("\n\nQual a nota desse filme? (0.0 - 5.0)")
                nota = float (input(""))
                validar = False
                while (validar != True):
                    if ((nota >= 0.0) and (nota<=5.0)):
                        validar = True
                        avaliacoesUsers[user][movie] = nota
                    else:
                        print("Nota inválida")
                        clear()
                        print ("\n\nQual a nota desse filme? (0.0 - 5.0)")
                        nota = float (input(""))
                clear()
                print ("\n\t\t\tFilme Cadastrado!")
            x = input("")
            return True
    x = input("")
    return False
##############################################################
#Historico de Filmes
def historicoFilmes(nome):
    clear()
    print ("\n\t\t\t::::Histórico de filmes::::\n\n")
    if (len(avaliacoesUsers[nome])==0):
        print("\n\t\t\tNão há filmes adicionados!")
        x = input("")
    else:
        for item in avaliacoesUsers[nome].items(): 
            print(item)
        x = input("")

##########################################################################################################################################

def login ():
    clear()
    print ("\n\t\t\t::::Login::::\n\n")
    print ("Nome de usuário:")
    nome = input ("")
    validarUser = userExiste(nome)
    while (validarUser != True ):
        print("\n\nUsuário não encontrado!")
        tempo()
        clear()
        print("\n\t\t\t::::Login::::")
        print ("\n\nNome de usuário:")
        nome = input("")
        validarUser = userExiste(nome)
    escrevaMenuPerfil()
    choice = "0"
    while (choice != "7"):
        choice = input ("\t")
        if (choice == "1"):
            historicoFilmes(nome)
        if (choice == "2"):
            clear()
            if (len(avaliacoesUsers[nome])==6):
                print("\n\t\t\tSem filmes para adicionar!")
                tempo()
            else:
                print("\n\t\t\t::::Filmes disponíveis:::: \n")
                for item in avaliacoesModel['Model']:
                    if item not in avaliacoesUsers[nome]:
                        print (item)
                movie = input("\n\nQual filme deseja adicionar?\t")
                validarMovies = addMovie(movie, nome)
                while (validarMovies != True ):
                    clear()
                    print ("\n\n\n\t\tFilme não encontrado ou já adicionado!")
                    tempo()
                    clear()
                    print("\n\t\t\t::::Filmes disponíveis:::: \n")
                    for item in avaliacoesModel['Model']:
                        if item not in avaliacoesUsers[nome]:
                            print (item)
                    movie = input ("\n\nQual filme deseja adicionar?\t")
                    validarMovies = addMovie(movie, nome)
        if (choice == "3"):
            clear()
            print("\n\t\t\t::::Histórico de filmes::::\n\n")
            for item in avaliacoesUsers[nome].items(): 
                print(item)
            excluirFilme(nome)
        if (choice == "4"):
            clear()
            print ("\n\t\t\t::::Recomendações do Sistema::::\n\n")
            filmesRecomendados(nome)
        if (choice == "5"):
            clear()
            mudarNota(nome)
            
        if (choice == "6"):
            valExcluir = excluirPerfil(nome)
            if (valExcluir==True):
               tempo()
               choice = "7"
            elif (valExcluir== False):
                print ("")
                print ("")
        if ((choice!="1") and (choice !="2")and (choice != "3") and (choice!="4")and (choice!="5")and (choice!="6") and (choice!="7")):
            print ("Opção inválida! Digite novamente:")
        print("")
        escrevaMenuPerfil() 
    print("")
    print("")    
    Menu()
#######################################################################################################################################################################################################################################################

def Menu():
    clear()
    escrevaMenu()
    
    choice = input("\t")
    while ((choice!="1")and(choice!="2")and(choice!="3")and(choice!="4")):
        print ("Opção inválida! Digite novamente: ")
        choice = input ("")
    if (choice == "1"):
        login()
    if (choice == "2"):
        criarPerfil()
    if (choice == "3"):
        sys.exit()
#######################################################################################################################################################################
def clear():
    os.system(['clear','cls'][os.name == 'nt'])
##################################################################################################################################
def tempo():
    time.sleep(1) 
##############################################################################################################################################################
Menu()
