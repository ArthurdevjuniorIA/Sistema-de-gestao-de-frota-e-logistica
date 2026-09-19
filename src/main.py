frotas = {

}
while True:
    Placa = input(" Digite a placa do veículo: ")
    tipo_de_veiculo = input("Digite o tipo de veículo: ")
    quanto_consome, consumo = input("Digite o valor do consumo do veículo: ").split()
    consumo_veiculo = quanto_consome + consumo
    capacidade_maxima = float(input("Digite a capacidade máxima do veículo: "))
    status = input("Qual o status do veículo: ")
    Placa = {
        "Tipo de veículo": tipo_de_veiculo,
        "Consumo": consumo_veiculo,
        "Capacidade máxima":capacidade_maxima,
        "Status": status
    }
    frotas["Placa"] = Placa
    if Placa == "fim":
        break