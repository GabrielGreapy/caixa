import matplotlib.pyplot as plt
import pandas as pd

# Dados
arquivo = pd.read_csv('c:/Users/Anderson Gomes/Desktop/Lista 5 Exercicios Anderson Gomes Cunha/dados.csv')
colunas = ['ideb', 'projecao']

# Função para criar ramos e folhas
def stem_and_leaf(data):
    stem_leaf = {}
    for number in colunas:
        stem = int(number)  # Parte inteira (ramo)
        leaf = int(round((number - stem) * 1))  # Parte decimal (folha)
        if stem not in stem_leaf:
            stem_leaf[stem] = []
        stem_leaf[stem].append(leaf)
    return stem_leaf

# Gerar o gráfico de ramos e folhas
stem_leaf_data = stem_and_leaf(colunas)

# Ordenar os caules
sorted_stems = sorted(stem_leaf_data.keys())

# Plotando o gráfico de ramos e folhas com Matplotlib
fig, ax = plt.subplots(figsize=(8, 5))

for idx, stem in enumerate(sorted_stems):
    leaves = ''.join(str(leaf) for leaf in sorted(stem_leaf_data[stem]))
    ax.text(0.1, 1 - idx * 0.1, f"{stem} | {leaves}", fontsize=12, ha='left')

# Configurações do gráfico
ax.axis('off')
ax.set_title("Gráfico de Ramos e Folhas", fontsize=14)

plt.show()
