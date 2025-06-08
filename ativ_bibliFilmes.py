#Atividade: Biblioteca de Filmes Dicionário 'usuarios_filmes':
#• Chave: Nome do usuário (string)
#• Valor: Lista de filmes (strings) que ele assistiu
#Menu de Opções
#• Menu de opções com uso de match case:
# 1 - Adicionar filme
# 2 - Remover filme
# 3 - Ver filmes de um usuário
# 4 - Ver todos os usuários
# 0 - Sair
#Uso de get() no item 3
#• Use get() para evitar erro ao consultar usuários que não existem.

#variaveis globais
user_lis = ["João" , "Maria"]
filmes_lis = [["Matrix" , "Constantine" ] , ["Titanic" , "Avatar" ]]
dict_user_filmes = {user_lis[i]: filmes_lis[i] for i in range(len(user_lis))}

#funções:
def add_user():  #cadastra novo usuario
    cad_user = input("Deseja cadastrar novo usuário? S/N ").upper()
    if cad_user == "S":
        user = input("Digite o nome de usuário que deseja cadastrar: ").title()
        user_lis.append(user)
        dict_user_filmes[user] = []
        print(user_lis)
        print(dict_user_filmes)
        print(f"o usuário {user} foi cadastrado com sucesso!\n Voltando ao menu...\n")
        menu_bibFilmes()
    else:
        print("Ops!\nPara continuar é preciso que o usuário esteja cadastrado.\nTente novamente\n")
        menu_bibFilmes()
   
    print(dict_user_filmes)

def add_filme():    #adiciona um filme a lista de um usuario cadastrado ou cadastra novo usuario e adiciona o filme a sua lista, ou chama a funão novamente
    print("Adicionando filme...")
    user = input("Digite o nome de usuário: ").title()
    if user in dict_user_filmes:
        novo_filme = input("Digite o nome do filme: ").title()
        menu_bibFilmes()  
    else:
        print("Ops!\nPara continuar é preciso que o usuário esteja cadastrado.\n")
        add_user()
    print(F"Nome do usuário: {user}\nNome do filme: {novo_filme}\nFilme adicionado com sucesso!\n")

def remover_filme():      #remove um filme da lista de um usuário cadastrado. se o usuario não estiver cadastrado chama a função novamente
    print("Removendo filme...")
    user = input("Digite o nome de usuário: ").title()
    if user in user_lis:
        rmv_flm = input("Digite o nome do filme: ").title()
        filmes_lis.remove(rmv_flm)
        print(f"Nome do usuário: {user}\nNome do filme: {rmv_flm}\nFilme removido com sucesso!\n") 
        menu_bibFilmes()
    else:
        print(f'O usuário "{user}" não está cadastrado no nosso sistema.\n"')
        add_user()
        print(dict_user_filmes) #teste: verifica se o dict foi atualizado corretamente

def consultar_filme():     #consulta os filmes de cada usuário cadastrado. Se o usuario nao estiver cadastrado chama a função novamente
    print("Consultando filme...")
    user = input("Digite o nome de usuário: ").title()
    if user in user_lis:
        filmes = dict_user_filmes.get(user)
        print(f"Nome do usuário: {user}\nFilmes assistidos: {filmes}")
        menu_bibFilmes()
    else:
        print(f'O usuário "{user}" não está cadastrado no nosso sistema.\n')
        add_user()

def sair_menu(): #confirma se quer sair do menu, caso N chama a função menu novamente
    sai_menu = input("Deseja sair do menu? S/N").upper()
    if sai_menu == "N":
        menu_bibFilmes()
    else:
        print("Você saiu do menu. Até logo!")

def menu_bibFilmes():   #menu match case
    try:
        bib_filmes = int(input("Opções do menu:\n1- Adicionar filme\n2- Remover filme\n3- Ver filmes de um usuário\n4- Ver todos os usuários\n0- Sair\nDigite ao número referente a opção desejada: "))
    except ValueError:
        print("Opção inválida!\n Tente novamente")
        menu_bibFilmes()   

    match bib_filmes:
        case 1:
            add_filme()
            print(dict_user_filmes) #teste: verifica se o dict foi atualizado corretamente
        case 2:
            remover_filme()
            print(dict_user_filmes) #teste: verifica se o dict foi atualizado corretamente       
        case 3:
            consultar_filme()
        case 4:
            users = dict_user_filmes.keys()
            print(users)
        case 0:
            sair_menu()
        case _:
            print("Opção inválida, tente novamente!")
            menu_bibFilmes()


#menssagem de boas vindas do app
print("Seja bem vindo a sua Biblioteca de Filmes\n") 
menu_bibFilmes()