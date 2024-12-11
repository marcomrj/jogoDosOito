from collections import deque
from jogoDosOito import JogoDosOito


class JogoDosOitoComBusca(JogoDosOito):
    def __init__(self):
        super().__init__()
        self.estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def gerar_estado_serializado(self, tabuleiro):
        """Converte o tabuleiro em uma string única para uso no BFS."""
        return ''.join(str(num) for linha in tabuleiro for num in linha)

    def encontrar_vizinhos(self, estado, posicao_vazia):
        """Gera estados vizinhos a partir de movimentos válidos."""
        linha_vazia, coluna_vazia = posicao_vazia
        movimentos = {
            "cima": (-1, 0),
            "baixo": (1, 0),
            "esquerda": (0, -1),
            "direita": (0, 1),
        }
        vizinhos = []
        for direcao, (dl, dc) in movimentos.items():
            nova_linha, nova_coluna = linha_vazia + dl, coluna_vazia + dc
            if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
                # Copia o estado atual
                novo_estado = [linha[:] for linha in estado]
                # Troca os valores
                novo_estado[linha_vazia][coluna_vazia], novo_estado[nova_linha][nova_coluna] = \
                    novo_estado[nova_linha][nova_coluna], novo_estado[linha_vazia][coluna_vazia]
                vizinhos.append((novo_estado, (nova_linha, nova_coluna)))
        return vizinhos

    def bfs(self):
        """Resolve o jogo dos oito usando busca em largura."""
        estado_inicial = self.tabuleiro
        posicao_vazia = self.encontrar_posicao_vazia()

        fila = deque([(estado_inicial, posicao_vazia, [])])
        visitados = set()

        while fila:
            estado_atual, posicao_vazia_atual, caminho = fila.popleft()
            estado_serializado = self.gerar_estado_serializado(estado_atual)

            if estado_serializado in visitados:
                continue
            visitados.add(estado_serializado)

            if estado_atual == self.estado_final:
                return caminho

            vizinhos = self.encontrar_vizinhos(estado_atual, posicao_vazia_atual)
            for vizinho, nova_posicao_vazia in vizinhos:
                nova_acao = caminho + [vizinho]
                fila.append((vizinho, nova_posicao_vazia, nova_acao))

        return None


jogo = JogoDosOitoComBusca()

print("Tabuleiro inicial gerado aleatoriamente (resolvível):")
jogo.mostrar_tabuleiro()

print("Buscando solução com BFS...")
caminho = jogo.bfs()

if caminho:
    print(f"Solução encontrada em {len(caminho)} passos:")
    for passo in caminho:
        for linha in passo:
            print(linha)
        print()
else:
    print("Nenhuma solução encontrada.")
