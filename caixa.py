# passo 1 ler, passo 2 graafico, passo 3, apresentação.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Ler o arquivo CSV
dados = pd.read_csv('data_inep.csv')

# Mostrar os dados lidos
dados['ano'] = dados['ano'].astype(str)  # Certificar que o ano está como string

# 4. Criar o gráfico de caixa
plt.figure(figsize=(14, 8))
sns.boxplot(x='ano', y='nota_saeb_matematica', hue='rede', data=dados)
plt.xticks(rotation=45)
plt.title('Distribuição das Notas do SAEB de Matemática por Ano e Rede de Ensino')
plt.xlabel('Ano')
plt.ylabel('Nota SAEB Matemática')
plt.legend(title='Rede de Ensino')
plt.tight_layout()
plt.savefig('grafico_de_caixa.png')  # Salva o gráfico em um arquivo PNG
