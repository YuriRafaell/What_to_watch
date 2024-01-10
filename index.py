import random

def sortear_categoria(lista_categoria):
    if not lista_categoria:
        print("A lista de categoria esta vazia!")
        return None
    
    categoria_sorteado = random.choice(lista_categoria)
    print(f"A categoria sorteada foi: {categoria_sorteado}")
    return categoria_sorteado

categorias = ["Series", "Move", "K-drama", "Anime"]
sortear_categoria(categorias)