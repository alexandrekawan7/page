import random

def gerar_referencia_pagina(tamanho, max_pagina=9):
    return [random.randint(0, max_pagina) for _ in range(tamanho)]

def fifo(paginas, quadros):
    memoria = []
    falhas = 0
    for pagina in paginas:
        if pagina not in memoria:
            if len(memoria) < quadros:
                memoria.append(pagina)
            else:
                memoria.pop(0)
                memoria.append(pagina)
            falhas += 1
    return falhas

def lru(paginas, quadros):
    memoria = []
    falhas = 0
    uso_recente = []
    for pagina in paginas:
        if pagina not in memoria:
            if len(memoria) < quadros:
                memoria.append(pagina)
            else:
                lru_pagina = uso_recente.pop(0)
                memoria[memoria.index(lru_pagina)] = pagina
            falhas += 1
        else:
            uso_recente.remove(pagina)
        uso_recente.append(pagina)
    return falhas

def experimentar(paginas, quadros):
    falhas_fifo = fifo(paginas, quadros)
    falhas_lru = lru(paginas, quadros)
    return falhas_fifo, falhas_lru

if __name__ == "__main__":
    tamanho_referencia = 20
    quadros_variados = [3, 4, 5]

    referencia_paginas = gerar_referencia_pagina(tamanho_referencia)
    print(f"Referência de páginas gerada: {referencia_paginas}\n")

    for quadros in quadros_variados:
        falhas_fifo, falhas_lru = experimentar(referencia_paginas, quadros)
        print(f"Com {quadros} quadros de página:")
        print(f"Falhas de página (FIFO): {falhas_fifo}")
        print(f"Falhas de página (LRU): {falhas_lru}\n")