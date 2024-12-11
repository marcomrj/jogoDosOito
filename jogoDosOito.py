import random

class JogoDosOito:
    def __init__(self):
        self.tabuleiro = self.gerar_tabuleiro_aleatorio_resolvivel()
        self.linha_vazia, self.coluna_vazia = self.encontrar_posicao_vazia()

    def gerar_tabuleiro_aleatorio_resolvivel(self):
        """Gera um tabuleiro aleatório resolvível."""
        while True:
            numeros = list(range(9)) 
            random.shuffle(numeros)
            if self.eh_valido(numeros):
                return [numeros[i:i+3] for i in range(0, 9, 3)]

    def eh_valido(self, numeros):
        """Verifica se uma configuração de tabuleiro é passivel de solução."""
        inversoes = 0
        for i in range(len(numeros)):
            for j in range(i + 1, len(numeros)):
                if numeros[i] != 0 and numeros[j] != 0 and numeros[i] > numeros[j]:
                    inversoes += 1
        return inversoes % 2 == 0

    def encontrar_posicao_vazia(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == 0:
                    return i, j

    def mover(self, direcao):
        """Move o espaço vazio para a direção especificada se possível."""
        movimentos = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1),
        }
        if direcao in movimentos:
            nova_linha = self.linha_vazia + movimentos[direcao][0]
            nova_coluna = self.coluna_vazia + movimentos[direcao][1]

            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
                self.tabuleiro[self.linha_vazia][self.coluna_vazia], self.tabuleiro[nova_linha][nova_coluna] = \
                    self.tabuleiro[nova_linha][nova_coluna], self.tabuleiro[self.linha_vazia][self.coluna_vazia]
                self.linha_vazia, self.coluna_vazia = nova_linha, nova_coluna
            else:
                print("Movimento inválido!")

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(linha)
        print()