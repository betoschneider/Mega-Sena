
class numero_da_sorte():
    def __init__(self):
        pass
    def gerar(self, qtd_jogos, qtd_dezendas=6):
        import numpy as np
        def numero_magico():
            return np.random.randint(1, 61)
        for i in range(qtd_jogos):
            jogo = [numero_magico()]

            for j in range(qtd_dezendas - 1):
                  chave = True
                  while chave:
                      novo_num = numero_magico()
                      if novo_num not in jogo:
                          jogo.append(novo_num)
                          chave = False

            print(np.sort(jogo))
            

if __name__ == '__main__':
    n = numero_da_sorte()
    n.gerar(2)

