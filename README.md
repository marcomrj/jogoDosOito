# Jogo dos Oito

## Descrição
Este projeto implementa o jogo dos oito com uma interface gráfica simples utilizando Python e tkinter. Ele também integra dois métodos de busca para resolver o jogo automaticamente:
- **BFS (Busca em Largura)**
- **A* (Busca Informada com Distância de Manhattan)**

O objetivo do jogo é organizar os números no tabuleiro 3x3 até alcançar o estado final:
```
1 2 3
4 5 6
7 8 0
```
O espaço vazio é representado pelo número `0`.

## Requisitos

### Dependências
- **Python 3.6 ou superior**
- **tkinter** (biblioteca padrão do Python para GUI)

### Instalação do tkinter
O tkinter geralmente é incluído com o Python, mas pode ser necessário instalá-lo manualmente em alguns sistemas operacionais.

#### Em distribuições Linux (Ubuntu/Debian):
```bash
sudo apt-get install python3-tk
```

#### Em macOS:
O tkinter já vem instalado com o Python. Certifique-se de estar usando o Python do sistema ou o Python do Homebrew.

#### Em Windows:
O tkinter já está incluído no instalador padrão do Python. Certifique-se de instalar a versão correta do Python.

#### Testando a instalação do tkinter:
Execute o comando a seguir para verificar se o tkinter está instalado:
```bash
python3 -m tkinter
```
Se uma janela gráfica for aberta, o tkinter está configurado corretamente.

## Estrutura do Projeto
- **jogoDosOito.py**: Contém a classe base `JogoDosOito` que implementa a lógica do jogo.
- **bfs.py**: Implementa a classe `JogoDosOitoComBusca`, que resolve o jogo usando Busca em Largura (BFS).
- **aEstrela.py**: Implementa a classe `aEstrela`, que resolve o jogo usando o algoritmo A*.
- **gui.py**: Contém a classe `JogoDosOitoGUI` para a interface gráfica e integração dos métodos de busca.

## Como Executar
1. Certifique-se de que todas as dependências estão instaladas.
2. Execute o arquivo `gui.py`:
```bash
python3 gui.py
```

## Funcionalidades
- **Embaralhar Tabuleiro**: Gera um novo estado inicial resolvível.
- **Resolver com BFS**: Aplica o algoritmo de Busca em Largura para resolver o jogo.
- **Resolver com A***: Aplica o algoritmo A* para resolver o jogo.
- **Exibição Gráfica**: Mostra o tabuleiro e os movimentos da solução passo a passo.

## Observações
- Os métodos de busca garantem encontrar a solução apenas para estados resolvíveis.
- A animação das soluções apresenta cada movimento com um intervalo de 500ms.
