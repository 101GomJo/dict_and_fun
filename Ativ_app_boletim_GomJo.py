#Atividade com Funções - Cadastro e Análise de Notas
#Obs.: Utilize um dicionário para armazenar os dados dos alunos.
###Boas Praticas: 1. Use um dicionário para armazenar os dados dos alunos.
# 2. Use listas para armazenar as notas.
# 3. Crie funções para cada funcionalidade.
# 4. Utilize o método get() para evitar erros ao consultar alunos.
# 5. Utilize match case para o menu de opções.

dic_boletim = {}

#Função 1 (dividida em duas funções): Cadastrar aluno: nome e  cadastrar 3 notas (armazenar em um dicionário).

def cad_alun():
    aluno = input("Insira o nome do aluno: ").title()    
    dic_boletim = [aluno]
    print(f"O aluno {aluno} foi cadastrado com sucesso!\n Voltando ao menu...\n")
    menu_boletim()
    return dic_boletim

#Função 2
def add_notas():
    notas = []
    p1 = float(input("Insira a nota da p1: "))
    p2 = float(input("Insira a nota da p2: "))
    p3 = float(input("Insira a nota da p3: "))
    notas.append(p1)
    notas.append(p2)
    notas.append(p3)
    dic_boletim = [notas]
    print(f"Notas cadastradas com sucesso!\n Voltando ao menu...\n")
    menu_boletim()
    return dic_boletim
   
#teste funcao 2
#cad_alun()
##add_notas()
#print(dic_boletim)

#Função 3: Calcular média: função que recebe uma lista de notas e retorna a média.
#OBS.: a media so sera eximbida ao chmar a função situação (item )

def media():
    aluno = input("Digite o nome do aluno para consultar as notas: ").title()
    if aluno in dic_boletim.keys():
        notas = (dic_boletim[aluno])
        soma_nt = sum(notas)
        calc_media = soma_nt / len(notas)
        mediaR = round(calc_media, 2)
        media = mediaR   
        return media
    else:
        print("O aluno não conta no nosso cadastro! Use a ooção 1 do menu para cadastrar o aluno.\n")
        menu_boletim()

#teste funcao 3 
#media = calc_media() #media = mediaR
#print(f"Sua média é: {media}")

#Função 4: Verificar situação: função que recebe a média e retorna a situação.
def situacao():
    media = media()
    if media >= 7.0:
        situacao = "aprovado"
        print(f"Sua média é: {media}. Você está aprovado. Parabéns!\n")
    else:
        situacao = "reprovado"
        print(f"Sua média é: {media}. você está reprovado. Estude mais!\n")
    menu_boletim()
    return situacao

#teste funcao 4 para verificar o return
##situacao = (situacao(media))
#print(situacao)


#Função 5: Exibir boletim de um aluno: nome, notas, média e situação.
#Função de atualização dados boletim
#não aparece no menu e é invocada na fun~]ao exibir boletim
def atual_boletim():
    dic_boletim.update({"média": media, "situação": situacao})
    return None

def exb_boletim():
    atual_boletim()
    aluno = input("Consultar o boletim.\n digite o nome do aluno: ").title()
    dic_boletim.get(aluno)
    boletim = dic_boletim
    menu_boletim()
    return boletim

#teste funcao 5 - return boletim atualizado
#print(exb_boletim())

#Função 6: Exibir todos os alunos cadastrados com suas médias e situações.

def dados_sistema():
    print(dic_boletim.items)
    boletim = dic_boletim
    return boletim

#teste funcao 6 exibir dados do sistema
#dados = dados_sistema()
#print(dados)

def sair_sistema(): #confirma se quer sair do menu, caso N chama a função menu novamente
    sai_sist = input("Deseja sair do sistema? S/N\n").upper()
    if sai_sist == "N":
        menu_boletim()
    else:
        print("Obrigado por utilizar o SIBA. Até logo!\n")


#Função 7: Menu com match case para navegar entre as opções.
def menu_boletim():   #menu match case
    try:
        menu = int(input("Opções do menu:\n1- Cadastrar aluno\n2- Adicionar notas\n3- Média e Situação\n4- Seu boletim\n5- Dados do sistema\n0- Sair\nDigite ao número referente a opção desejada: "))
    except ValueError:
        print("Opção inválida!\n Tente novamente\n")
        menu_boletim()   

    match menu:
        case 1:
            cad_alun()
            print(dic_boletim) #teste: verifica se o dict foi atualizado corretamente
        case 2:
            add_notas()
            print(dic_boletim) #teste: verifica se o dict foi atualizado corretamente       
        case 3:
            situacao()
        case 4:
            exb_boletim()
        case 5:
            dados_sistema()
        case 0:
            sair_sistema()
        case _:
            print("Opção inválida, tente novamente!")
            menu_boletim()


#menssagem de apresentação do sistema
print("SIBA - Sistema Boletim do Aluno\n") 
menu_boletim()