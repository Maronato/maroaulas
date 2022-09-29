def main():
    # Pergunta quantos reais o usuario quer
    total = perguntar_reais()

    # Calcula quantas notas de 10 reais
    # cabem no total, depois subtrai o valor
    notas_10 = calcula_10(total)
    total = total - notas_10 * 10

    # Faz o mesmo para notas de 5
    notas_5 = calcula_5(total)
    total = total - notas_5 * 5

    # Faz o mesmo para notas de 2
    notas_2 = calcula_2(total)
    total = total - notas_2 * 2

    # Faz o mesmo para notas de 1
    notas_1 = calcula_1(total)
    total = total - notas_1 * 1

    # Soma o total de notas
    notas = notas_10 + notas_5 + notas_2 + notas_1

    # Imprime o número total de notas que
    # o usuário receberá
    print(f"Você vai receber {notas} notas")


def perguntar_reais():
    # IMPLEMENTE AQUI
    return 0


def calcula_10(total):
    # IMPLEMENTE AQUI
    return 0


def calcula_5(total):
    # IMPLEMENTE AQUI
    return 0


def calcula_2(total):
    # IMPLEMENTE AQUI
    return 0


def calcula_1(total):
    # IMPLEMENTE AQUI
    return 0


# Só executa o programa se ele for executado diretamente
if __name__ == "__main__":
    # Chama nossa função principal
    main()
