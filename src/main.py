import verificacoes
frotas = [ ]
Pessoas_cadastradas = [ ]



Tipos_combustiveis = ["Biodiesel","Gasolina","Etanol","Diesel","GNV"]
Status_do_veiculo = ["DISPONÍVEL", "EM ROTA", "MANUTENÇÃO"]
''''********************************
EXIBIÇÃO DE MENUS
************************************
'''
def exibir_menu_gestao_de_frota():
    print("========== GESTÃO DA FROTA ==========")
    print("1 - Cadastrar novo veículo (Placa, Tipo, Peso Máx, Consumo, Chassi, RENAVAM")
    print("2 - Consultar frota completa")
    print("3 - Consultar veículo por Placa")
    print("4 - Alterar status do veículo (Disponível / Manutenção / Inativo")
    print("0 - Voltar ao Menu Principal")

def exibir_menu_gestao_motoristas():
    print("========== GESTÃO DE MOTORISTAS ==========")

    print("1 - Cadastrar motorista (Nome, CPF, CNH, Categoria, Validade CNH)")
    print("2 - Listar todos os motoristas")
    print("3 - Consultar motorista por CPF")
    print("4 - Atualizar renovação de CNH")
    print("0 - Voltar ao Menu Principal")

def exibir_menu_principal():
   print("GLOBALMOVE LOGÍSTICA — SISTEMA INTEGRADO")
   print("1 - Gestão da Frota & Veículos")
   print("2 - Gestão de Motoristas & Habilitações")
   print("3 - Operação de Pátio (Cargas, Alocação & Viagens")
   print("4 - Manutenção & Abastecimento")
   print("5 - Documentação, Impostos & Multas")
   print("6 - Central de Relatórios & Inteligência")
   print("0 - Sair do Sistema")

''''********************************
MENUS DE GESTÃO E FROTA
************************************
'''
def cadastro_veiculo():
    if not Pessoas_cadastradas:
        print("É necessário cadastrar um motorista antes de cadastrar um veículo")
        return -1
    else:
        cpf = input("Digite o seu CPF para verificarmos se está no nosso cadastro: ").replace(".","").replace("-","").strip()
        for pessoa in Pessoas_cadastradas:
            if pessoa["Bloqueado"] == True:
                print("Você está bloqueado no sistema devido a CNH vencida")
                return -1

            if cpf == pessoa["cpf"]:
               Placa = input(" Digite a placa do veículo: ").upper().replace("-","")
                   
               tipo_de_veiculo = input("Digite o tipo de veículo: ")
                
               try:
                    quanto_consome, consumo = input("Digite o valor do consumo do veículo: ").split()
               
               except ValueError or TypeError:
                    print("Digite o valor de quanto consome e a unidade de medida que está utilizando, por exemplo km/l")
                
               consumo_veiculo = quanto_consome + consumo
               try:
                 capacidade_maxima, unidade_de_medida = input("Digite a capacidade máxima do veículo: ").split()
               
               except ValueError or TypeError:
                   print("Digite o valor e a unidade de medida")

               status = input("Qual o status do veículo: (Disponível, Em rota ou em manutenção) ").upper()
               if status not in Status_do_veiculo:
                   print("Você digitou algo diferente de:Disponível, Em rota ou  Manutenção ")
                   continue
               Renavam = input("Digite qual o Renavam do carro: ")
               Modelo = input("Digite qual o modelo do carro: ")
               Ano = input("Digite qual o ano do carro: ")
               try:
                  KM_atual = float(input("Digite o km atual do veículo: "))
               
               except ValueError or TypeError:
                   print("Digite apenas números do conjunto real")

               print("Combustíveis oficiais pelo ANP: ")
                
               for combustivel in Tipos_combustiveis:
                    i +=1
                    print(i,"-",combustivel)
                
               Tipo_de_combustivel = int(input("Digite qual combustível o veículo, se usar mais de um digite", "0",":" ))
               Caracteristicas_veiculo = {
                   "Placa": Placa,
                    "Tipo": tipo_de_veiculo,
                    "Consumo": consumo_veiculo,
                    "Capacidade":capacidade_maxima,
                    "Status": status,
                    "Renavam": Renavam,
                    "Modelo": Modelo,
                    "Ano": Ano,
                    "Tipo Combustivel": Tipos_combustiveis[Tipo_de_combustivel-1],
                    "Outro tipo de combustivel": Tipos_combustiveis[Mais_de_um_combustivel-1],
                    "KM atual": KM_atual,
                    "CPF": cpf
                }
                
               if Tipo_de_combustivel == "MAIS":
                    Mais_de_um_combustivel = verificacoes.tratamento_erros(Mais_de_um_combustivel,"Digite a outra forma de combustível que o veículo utiliza: ")
                    Caracteristicas_veiculo["Outro tipo de combustivel"] = Tipos_combustiveis[Mais_de_um_combustivel-1]
               
               frotas.append(Caracteristicas_veiculo)


def consultar_frota():
    
    if not frotas:
        print("Não há nenhum veículo cadastrado")
    else:
        print("""===================================================================
            CONSULTA DA FROTA COMPLETA                              
        =========================================================================""")
        espaco = " "*5
        espaco_maior = ""*10
        print(f"Placa{espaco}Modelo/Marca{espaco_maior}Tipo{espaco}Capacidade(kg){espaco}KM atual{espaco}STATUS")
        print("-"*55)
        for frota in frotas:
            for veiculos in frota:
                print(f"{veiculos["Placa"]}{espaco}veiculos{["Modelo"]}{espaco_maior}{["Tipo"]}{espaco}{["Capacidade"]}{espaco}{["KM atual"]}{espaco}{['Status']}")
    
def consultar_veiculo_pela_placa():
    consulta_veiculo = input("Digite qual placa de veículo você deseja consultar: ").upper().replace("-","")
    for veiculo in frotas:
        if consulta_veiculo == veiculo["Placa"]:
            print("Dados do veículo: ")
            espaco = " "*5
            espaco_maior = ""*10
            print(f"Placa{espaco}Modelo/Marca{espaco_maior}Tipo{espaco}Capacidade(kg){espaco}KM atual{espaco}STATUS")
            print("-"*55)
            print(f"{veiculo["Placa"]}{espaco}{veiculo["Modelo"]}{espaco_maior}{veiculo["Tipo"]}{espaco}{veiculo["Capacidade"]}{espaco}{veiculo["KM atual"]}{espaco}{veiculo['Status']}")
            print("Dados do cadastrador do veículo: ")
            for Pessoa in Pessoas_cadastradas:
                if veiculo["CPF"] == Pessoa["CPF"]:
                    print(f"Nome{espaco_maior}CNH{espaco_maior}CPF")
                    print(f"{Pessoa["Nome"]}{espaco_maior}{Pessoa["CNH"]}")


def menu_gestao_de_frota():
    while True:
        exibir_menu_gestao_de_frota()
        
        qual_opcao = int(input("Digite qual opção você deseja realizar: "))
        if qual_opcao == 1:
            cadastro_veiculo()
        elif qual_opcao == 2:
            cadastro_motorista()
        elif qual_opcao == 3:
            consultar_frota()
''''********************************
MENUS DE CADASTRO DE MOTORISTA
************************************
'''
def cadastro_motorista():
    Nome_completo = input("Digite o seu nome completo: ")
    CPF = input("Digite o CPF: ")
    CPF = CPF.replace(".","").strip().replace("-","")
    CPF_APENAS_NUMEROS = int(CPF)
    CNH = verificacoes.tratamento_erros(CNH,"Digite o Número de registro da sua CNH: ")
    Data_validade_Carteira = input("Digite a data de validade da carteira(apenas o mês e o ano ex: 10/29): ").replace("/","").strip()
    ano = Data_validade_Carteira[-2:]
    mes = Data_validade_Carteira[2:]
    
    Pessoa_cadastrada = {
            "Nome": Nome_completo,
            "CPF": CPF_APENAS_NUMEROS,
            "CNH": CNH,
            "Validade Carteira" : Data_validade_Carteira,
        }
    if ano<26 or mes<10 and ano<=26:
        print("Sua carteira de CNH já venceu, recomenda-se atualizar a carteira e por enquanto você não pode cadastrar nenhum veículo")
        Pessoa_cadastrada["Bloqueado"] = True
        return -1
    Pessoa_cadastrada["Bloqueado"] = False

    
    Pessoas_cadastradas.append(Pessoa_cadastrada)
                     


def menu_principal():
    exibir_menu_principal()
    qual_opcao = int(input("Digite a opção desejada: "))
    if qual_opcao == 1:
        menu_gestao_de_frota()
    elif qual_opcao == 2:
        menu_gestao_motoristas()