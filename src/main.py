frotas = {

}
Pessoas_cadastradas = {

}
Tipos_combustiveis = ["Biodiesel","Gasolina","Etanol","Diesel","GNV"]
i = 1
while True:
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

    Placa = input(" Digite a placa do veículo: ")
    
    tipo_de_veiculo = input("Digite o tipo de veículo: ")
    
    try:
        quanto_consome, consumo = input("Digite o valor do consumo do veículo: ").split()
    except ValueError:
        print("Digite o valor de quanto consome e a unidade de medida que está utilizando, por exemplo km/l")
    
    consumo_veiculo = quanto_consome + consumo
    capacidade_maxima = float(input("Digite a capacidade máxima do veículo: "))
    status = input("Qual o status do veículo: ")
    Renavam = input("Digite qual o Renavam do carro: ")
    Modelo = input("Digite qual o modelo do carro: ")
    Ano = input("Digite qual o ano do carro: ")
    print("Combustíveis oficiais pelo ANP:")
    
    for combustivel in Tipos_combustiveis:
        i +=1
        print(i,"-",combustivel)
    
    Tipo_de_combustivel = int(input("Digite qual combustível o veículo, se usar mais de um digite", "MAIS",":" ))
    
    if Tipo_de_combustivel == "MAIS":
        Mais_de_um_combustivel = int(input("Digite a outra forma de combustível que o veículo utiliza: "))
    Caracteristicas_veiculo = {
        "Tipo de veículo": tipo_de_veiculo,
        "Consumo": consumo_veiculo,
        "Capacidade máxima":capacidade_maxima,
        "Status": status,
        "Renavam": Renavam,
        "Modelo": Modelo,
        "Ano": Ano,
        "Tipo Combustivel": Tipos_combustiveis[Tipo_de_combustivel-1],
        "Outro tipo de combustivel": Tipos_combustiveis[Mais_de_um_combustivel-1]
    }
    frotas["Placa"] = Placa
    
    if Placa == "fim":
        break