'''
script para gerar números aleatórios
agrupados em jogos de loteria
'''

def gerar(qtd_jogos, qtd_dezendas=6, dezena_max=60):
    '''
    qtd_jogos: int, número de jogos a serem gerados
    qtd_dezenas: int, quantidade de jogos a comporem cada jogo, padrão 6
    dezena_max: int, limite escolha do número aleatório, padrão 60
    '''
    import numpy as np

    #gera o número aleatório da loteria
    def numero_magico():
        return np.random.randint(1, dezena_max + 1)
    
    #laço para criar a qtd de jogos 
    for i in range(qtd_jogos):
        jogo = [numero_magico()]

        #laço para adicionar as dezenas restantes
        for j in range(qtd_dezendas - 1):
                valida = True
                while valida:
                    novo_num = numero_magico()

                    #adiciona ao jogo se novo número não estiver lá
                    if novo_num not in jogo:
                        jogo.append(novo_num)
                        valida = False

        print(np.sort(jogo))
            

if __name__ == '__main__':
    gerar(2)

