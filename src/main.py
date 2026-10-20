frotas = {

}
Pessoas_cadastradas = {

}
Tipos_combustiveis = ["Biodiesel","Gasolina","Etanol","Diesel","GNV"]
Status_do_veiculo = ["DISPONÍVEL", "EM ROTA", "MANUTENÇÃO"]
''''********************************
MENUS
************************************
'''
def exibir_menu_gestao_de_frota():
    print("1 - Cadastrar novo veículo (Placa, Tipo, Peso Max, Consumo, Chassi, RENAVAM)")
    print("2 - Cadastrar motorista (Nome, CPF, CNH, Categoria, Validade)")
    print("3 - Consultar frota completa")
    print("4 - Consultar veículo por Placa")
    print("0 - Voltar ao Menu Principal")

def cadastro_veiculo():
    if not Pessoas_cadastradas:
        print("É necessário cadastrar um motorista antes de cadastrar um veículo")
        return -1
    else:
        cpf = input("Digite o seu CPF para verificarmos se está no nosso cadastro: ").replace(".","").replace("-","").strip()
        for pessoa in Pessoas_cadastradas:
            if cpf == pessoa["cpf"]:
               Placa = input(" Digite a placa do veículo: ")
                   
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
                    "Outro tipo de combustivel": Tipos_combustiveis[Mais_de_um_combustivel-1]
                }
                
               if Tipo_de_combustivel == "MAIS":
                    Mais_de_um_combustivel = int(input("Digite a outra forma de combustível que o veículo utiliza: "))
                    frotas["Outro tipo de combustivel"] = Tipos_combustiveis[Mais_de_um_combustivel-1]
               
               frotas["Veiculo"] = Caracteristicas_veiculo
def cadastro_motorista():
    Nome_completo = input("Digite o seu nome completo: ")
    CPF = input("Digite o CPF: ")
    CPF = CPF.replace(".","").strip().replace("-","")
    CPF_APENAS_NUMEROS = int(CPF)
    
    CNH = int(input("Digite o Número de registro da sua CNH: "))
    Data_validade_Carteira = input("Digite a data de validade da carteira: ").replace(".","-").strip()
    Pessoa_cadastrada = {
        "Nome": Nome_completo,
        "CPF": CPF_APENAS_NUMEROS,
        "CNH": CNH,
        "Validade Carteira" : Data_validade_Carteira,
    }
    Pessoas_cadastradas["Pessoa cadastrada"] = Pessoa_cadastrada

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

menu_gestao_de_frota()