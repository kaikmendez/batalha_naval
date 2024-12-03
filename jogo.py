import random as rm

def criar_tabuleiro():
    return [
        ["~"] * 20
         for _ in range(20)
    ]

def exibir_tabuleiro(tabuleiro):
    for row in tabuleiro:
        print("  ".join(row))

tabuleiro = criar_tabuleiro()        

exibir_tabuleiro(tabuleiro)