import random

def sortear_categoria_e_conteudo(lista_categoria):
    if not lista_categoria:
        print("A lista de categoria esta vazia!")
        return None
    
    # Sorteia a categoria
    categoria_sorteado = random.choice((list(lista_categoria.keys())))
    print(f"A categoria sorteada foi: {categoria_sorteado}")

    # Sorteia o conteudo
    conteudo_sorteado = random.choice(lista_categoria[categoria_sorteado])
    print(f"O conteúdo sorteado foi: {conteudo_sorteado}")
    return categoria_sorteado, conteudo_sorteado

categoria_e_conteudo = {
    "Series": ["Good girls", "The Rookie", "Masterchef profissionais"],
    "Movies": ["Diário de intercâmbio", "Better Days", "The follout"],
    "K-Drama": ["É tudo meu", "Weak Hero Class", "The could've-gone-all-the-way committee"],
    "Anime": ["Naruto", "Black lagoon", "Assim falava Kishibe Rohan", "The beginning"]
}

sortear_categoria_e_conteudo(categoria_e_conteudo)