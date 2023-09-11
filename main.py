import pandas as pd

# Definição da região metropolitana de Florianópolis
nucleo_metropolitano = ['Florianópolis ',
                        'São José ',
                        'Palhoça ',
                        'Biguaçu ',
                        'Santo Amaro da Imperatriz ',
                        'Governador Celso Ramos ',
                        'Antônio Carlos ',
                        'Águas Mornas ',
                        'São Pedro de Alcântara '
                        ]

area_expansao        = ['Alfredo Wagner ',
                        'Angelina ',
                        'Anitápolis ',
                        'Canelinha ',
                        'Garopaba ',
                        'Leoberto Leal ',
                        'Major Gercino ',
                        'Nova Trento ',
                        'Paulo Lopes ',
                        'Rancho Queimado ',
                        'São Bonifácio ',
                        'São João Batista ',
                        'Tijucas '
                        ]

regiao_metropolitana_florianopolis = nucleo_metropolitano + area_expansao

# Leitura do arquivo-base
obras_brasil = pd.read_csv('_contratacoes_pcmv_pcva.csv', sep='|', encoding='latin_1', low_memory=False)

# Recorte para obras contratadas para Santa Catarina e Região Metropolitana de Florianópolis
obras_santa_catarina = obras_brasil[obras_brasil['txt_uf'] == 'SC']
obras_rmf            = obras_santa_catarina[obras_santa_catarina['txt_municipio'].isin(regiao_metropolitana_florianopolis)]

qtd_obras_br  = len(obras_brasil)
qtd_obras_sc  = len(obras_santa_catarina)
qtd_obras_rmf = len(obras_rmf)

# Definição de dicionários com grupos de dataframes, separados por território e coluna de interesse
dfs         = {'Brasil': obras_brasil, 'Santa Catarina': obras_santa_catarina, 'Região Metropolitana de Florianópolis': obras_rmf}
programas   = {}
modalidades = {}

# Filtragem dos dataframes-base para os específicos de cada coluna que será trabalhada
for nome, df in dfs.items():
    programas[nome] = df['txt_programa'].value_counts()
    modalidades[nome] = df['txt_modalidade_programa'].value_counts()

