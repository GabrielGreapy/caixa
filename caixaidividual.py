import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv('data_inep.csv')

print("Colunas disponíveis no arquivo CSV:", dados.columns)

print("Valores únicos da coluna 'rede':", dados['rede'].unique())

dados['rede'] = dados['rede'].str.lower().str.strip()

redes = ['publica', 'estadual', 'municipal', 'privada', 'local']

for rede in redes:
    dados_rede = dados[dados['rede'] == rede]  # Filtrar os dados para a rede atual

    # Verifica se existem dados para a rede atual
    if not dados_rede.empty:
        plt.figure(figsize=(14, 8))
        sns.boxplot(x='ano', y='nota_saeb_matematica', data=dados_rede)
        plt.xticks(rotation=45)
        plt.title(f'Distribuição das Notas do SAEB de Matemática por Ano ({rede})')
        plt.xlabel('Ano')
        plt.ylabel('Nota SAEB Matemática')
        plt.tight_layout()
        plt.savefig(f'grafico_{rede}.png')  # Salva o gráfico em um arquivo PNG
        plt.close()  # Fecha a figura para liberar a memória
    else:
        print(f'Não há dados para a rede: {rede}')
