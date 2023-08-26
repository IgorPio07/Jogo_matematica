from random import randint


class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar, 2 = subtrair, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    # Criar uma variável string para apresetar as operações

    def __str__(self: object) -> str:
        op: str = ''
        match self.operacao:
            case 1:
                op = 'Somar'
            case 2:
                op = 'Subtrair'

            case 3:
                op = 'Multiplicar'
            case _:
                op = 'Operação Inválida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> int:
        match self.dificuldade:
            case 1:
                return randint(0, 10)
            case 2:
                return randint(0, 100)
            case 3:
                return randint(0, 1000)
            case 4:
                return randint(0, 10000)
            case _:
                return randint(0, 1000000)

    @property
    def _gerar_resultado(self: object) -> int:
        match self.operacao:
            case 1:
                return self.valor1 + self.valor2
            case 2:
                return self.valor1 - self.valor2
            case 3:
                return self.valor1 * self.valor2
    
    @property
    def _op_simbolo(self: object) -> str:
        match self.operacao:
            case 1:
                return '+'
            case 2:
                return '-'
            case 3:
                return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta Correta!')
            certo = True
        else:
            print('resposta errada...')
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo

    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')

