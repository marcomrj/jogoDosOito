import tkinter as tk
from bfs import JogoDosOitoComBusca
from aEstrela import aEstrela

class JogoDosOitoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo dos Oito")
        self.jogo = None
        self.create_widgets()

    def create_widgets(self):
        """Cria os componentes da interface gráfica."""
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        # Botões para o tabuleiro
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, text="", font=("Arial", 24), width=4, height=2)
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        # Controles
        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack()

        self.bfs_button = tk.Button(self.control_frame, text="Resolver com BFS", command=self.solve_with_bfs)
        self.bfs_button.pack(side="left", padx=5)

        self.astar_button = tk.Button(self.control_frame, text="Resolver com A*", command=self.solve_with_astar)
        self.astar_button.pack(side="left", padx=5)

        self.shuffle_button = tk.Button(self.control_frame, text="Embaralhar", command=self.shuffle_board)
        self.shuffle_button.pack(side="left", padx=5)

        self.update_board()

    def update_board(self):
        """Atualiza os botões para refletir o estado atual do tabuleiro."""
        if not self.jogo:
            return

        for i in range(3):
            for j in range(3):
                valor = self.jogo.tabuleiro[i][j]
                if valor == 0:
                    self.buttons[i][j].config(text="", state="disabled", bg="lightgray")
                else:
                    self.buttons[i][j].config(text=str(valor), state="normal", bg="white")

    def animate_solution(self, solution):
        """Mostra a solução passo a passo na interface."""
        for estado in solution:
            self.jogo.tabuleiro = estado
            self.update_board()
            self.root.update()
            self.root.after(500)  # Aguarda 500ms entre os passos

    def solve_with_bfs(self):
        """Resolve o jogo com BFS."""
        self.jogo = JogoDosOitoComBusca()
        solution = self.jogo.bfs()
        if solution:
            self.animate_solution(solution)
        else:
            print("Nenhuma solução encontrada com BFS.")

    def solve_with_astar(self):
        """Resolve o jogo com A*."""
        self.jogo = aEstrela()
        solution = self.jogo.resolver()
        if solution:
            self.animate_solution(solution)
        else:
            print("Nenhuma solução encontrada com A*.")

    def shuffle_board(self):
        """Embaralha o tabuleiro."""
        self.jogo = JogoDosOitoComBusca()  # Gera um novo tabuleiro resolvível
        self.update_board()


if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDosOitoGUI(root)
    root.mainloop()
