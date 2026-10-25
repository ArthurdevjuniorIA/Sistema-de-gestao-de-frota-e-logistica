import main
def tratamento_erros(valor,mensagem):
    try:
        valor = int(input(mensagem))
    except ValueError:
        print("O valor digitado deve ser um número inteiro!")
        return -1
    return valor
    