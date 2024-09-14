import matplotlib.pyplot as plt
import pandas as pd

# Carregar o CSV e selecionar as colunas
arquivo = pd.read_csv('c:/Users/Anderson Gomes/Desktop/Lista 5 Exercicios Anderson Gomes Cunha/dados.csv')
colunas = ['ideb', 'projecao']

# Função para criar o gráfico de ramos e folhas
def stem_and_leaf(data):
    stem_leaf = {}
    for number in data:
        stem = int(number)  # Parte inteira (ramo)
        leaf = int(round((number - stem) * 10))  # Parte decimal (folha)
        if stem not in stem_leaf:
            stem_leaf[stem] = []
        stem_leaf[stem].append(leaf)
    return stem_leaf

# Iterar sobre as colunas escolhidas e gerar o gráfico para cada uma
for coluna in colunas:
    dados = arquivo[coluna].dropna()  # Remover valores ausentes (NaN)
    
    # Gerar ramos e folhas
    stem_leaf_data = stem_and_leaf(dados)
    
    # Ordenar os caules
    sorted_stems = sorted(stem_leaf_data.keys())
    
    # Plotando o gráfico de ramos e folhas
    fig, ax = plt.subplots(figsize=(8, 5))
    
    for idx, stem in enumerate(sorted_stems):
        leaves = ''.join(str(leaf) for leaf in sorted(stem_leaf_data[stem]))
        ax.text(0.1, 1 - idx * 0.1, f"{stem} | {leaves}", fontsize=12, ha='left')
    
    # Configurações do gráfico
    ax.axis('off')
    ax.set_title(f"Gráfico de Ramos e Folhas - {coluna.capitalize()}", fontsize=14)
    
    plt.show()
