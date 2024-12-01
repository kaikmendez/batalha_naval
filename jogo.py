import ramdom as rm

def criar_tabuleiro():
    return [
        ["~"] * 20
         for _ in range(20)
    ]

tabuleiro = criar_tabuleiro()

def exibir_tabuleiro(tabuleiro):
    for row in tabuleiro:
        print("  ".join(row))

exibir_tabuleiro(tabuleiro)