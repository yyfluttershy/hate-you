musicas = [
    ("Musica 1", "Rock"),
    ("Musica 2", "Pop"),
    ("Musica 3", "Jazz"),
    ("Musica 4", "Rock"),
    ("Musica 5", "Pop"),
]

# Histórico de músicas ouvidas pelo usuário 
Historico_usuario = ["Rock", "Jazz", "Pop", "Jazz", "Pop"]


# Função paea recomendar músicas 
def recomendar_musica(historico):
    # Conrae a frequencia de cada genero no historico
    frequencia = {}
    for genero in historico:
        if genero in frequencia:
            frequencia[genero] += 1
        else:
            frequencia[genero] = 1

    # Encontrar o genero mais frequente 
    genero_mais_frequente = max(frequencia, key=frequencia.get)

    # Recomendar músicasdesse genero
    recomendacoes = []
    for titulo, genero in musicas:
        if genero == genero_mais_frequente:
            recomendacoes.append(titulo)
    return recomendacoes


# Obter recomendacoes para o usuário 
recomendacoes_usuario = recomendar_musica(Historico_usuario)
print("Musicas recomendadas:", recomendacoes_usuario)
