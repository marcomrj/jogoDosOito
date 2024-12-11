import heapq
from jogoDosOito import JogoDosOito


class AStar(JogoDosOito):
    def __init__(self):
        super().__init__()
        self.estado_final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def calcular_heuristica(self, estado):
        """Calcula a distância de Manhattan como heurística."""
        distancia = 0
        for i in range(3):
            for j in range(3):
                valor = estado[i][j]
                if valor != 0:
                    linha_destino = (valor - 1) // 3
                    coluna_destino = (valor - 1) % 3
                    distancia += abs(linha_destino - i) + abs(coluna_destino - j)
        return distancia

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
                novo_estado = [linha[:] for linha in estado]
                novo_estado[linha_vazia][coluna_vazia], novo_estado[nova_linha][nova_coluna] = \
                    novo_estado[nova_linha][nova_coluna], novo_estado[linha_vazia][coluna_vazia]
                vizinhos.append((novo_estado, (nova_linha, nova_coluna)))
        return vizinhos

    def resolver(self):
        """Resolve o jogo dos oito usando o algoritmo A*."""
        estado_inicial = self.tabuleiro
        posicao_vazia = self.encontrar_posicao_vazia()

        fila = []
        estado_inicial_serializado = tuple(tuple(linha) for linha in estado_inicial)
        heapq.heappush(fila, (0, estado_inicial, posicao_vazia, []))
        visitados = set()

        while fila:
            _, estado_atual, posicao_vazia_atual, caminho = heapq.heappop(fila)
            estado_serializado = tuple(tuple(linha) for linha in estado_atual)

            if estado_serializado in visitados:
                continue
            visitados.add(estado_serializado)

            if estado_atual == self.estado_final:
                return caminho

            vizinhos = self.encontrar_vizinhos(estado_atual, posicao_vazia_atual)
            for vizinho, nova_posicao_vazia in vizinhos:
                novo_caminho = caminho + [vizinho]
                g = len(novo_caminho)
                h = self.calcular_heuristica(vizinho)
                f = g + h
                heapq.heappush(fila, (f, vizinho, nova_posicao_vazia, novo_caminho))

        return None

jogo = AStar()

print("Tabuleiro inicial gerado aleatoriamente (resolvível):")
jogo.mostrar_tabuleiro()

print("Buscando solução com A*...")
caminho = jogo.resolver()

if caminho:
    print(f"Solução encontrada em {len(caminho)} passos:")
    for passo in caminho:
        for linha in passo:
            print(linha)
        print()
else:
    print("Nenhuma solução encontrada.")
