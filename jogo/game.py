from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe a dificuldade desejada [1, 2, 3, 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para aseguinte operação: ')
    calc.mostrar_operacao()  # 5 + 4 = ?

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos')

    continuar: int = int(input('Deseja continuar no jogo? [1 -> sim, 0 -> não]: '))
    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} pontos!')
        print('Até a próxima')


if __name__ == '__main__':
    main()

