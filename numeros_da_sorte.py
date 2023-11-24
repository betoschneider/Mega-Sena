
class numero_da_sorte():
    def __init__(self):
        pass
        
    def gerar(self, qtd):
        import numpy as np
        for i in range(qtd):
            a = np.array([np.random.randint(0, 61),
                  np.random.randint(0, 61),
                  np.random.randint(0, 61),
                  np.random.randint(0, 61),
                  np.random.randint(0, 61),
                  np.random.randint(0, 61)]
                  )
            print(np.sort(a))

if __name__ == '__main__':
    n = numero_da_sorte()
    n.gerar(2)

