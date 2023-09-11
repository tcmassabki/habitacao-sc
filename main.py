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
obras_florianopolis  = obras_rmf[obras_rmf['txt_municipio'] == 'Florianópolis ']


# Definição das quantidades totais de obras contratadas por território
qtd_obras_br     = len(obras_brasil)
qtd_obras_sc     = len(obras_santa_catarina)
qtd_obras_rmf    = len(obras_rmf)
qtd_obras_fpolis = len(obras_florianopolis)


# Definição de dicionários com grupos de dataframes, separados por território e coluna de interesse
dfs                  = {'Brasil': obras_brasil,
                        'Santa Catarina': obras_santa_catarina,
                        'Região Metropolitana de Florianópolis': obras_rmf,
                        'Florianópolis': obras_florianopolis}
qtd_obras_territorio = {'Brasil': qtd_obras_br,
                        'Santa Catarina': qtd_obras_sc,
                        'Região Metropolitana de Florianópolis': qtd_obras_rmf,
                        'Florianópolis': qtd_obras_fpolis}
programas            = {}
modalidades          = {}
pct_programas        = {}
pct_modalidades      = {}


# Filtragem dos dataframes-base para os específicos de cada coluna que será trabalhada, tanto números absolutos quanto porcentagem
for nome, df in dfs.items():
    programas[nome] = df['txt_programa'].value_counts()
    modalidades[nome] = df['txt_modalidade_programa'].value_counts()
    pct_programas[nome] = (df['txt_programa'].value_counts() / qtd_obras_territorio[nome]) * 100
    pct_modalidades[nome] = (df['txt_modalidade_programa'].value_counts() / qtd_obras_territorio[nome]) * 100
    programas[nome].rename_axis(nome, inplace=True)
    modalidades[nome].rename_axis(nome, inplace=True)
    pct_programas[nome].rename_axis(nome, inplace=True)
    pct_modalidades[nome].rename_axis(nome, inplace=True)


# Concatenação e configuração das colunas para dataframe de programas
programa_df = pd.concat([programas['Brasil'],
                         pct_programas['Brasil'],
                         programas['Santa Catarina'],
                         pct_programas['Santa Catarina'],
                         programas['Região Metropolitana de Florianópolis'],
                         pct_programas['Região Metropolitana de Florianópolis'],
                         programas['Florianópolis'],
                         pct_programas['Florianópolis']
                         ], axis='columns')

programa_df.columns = ['BR', '% (BR)', 'SC', '% (SC)', 'RMF', '% (RMF)', 'FPolis', '% (Fpolis)']



# Concatenação e configuração das colunas para dataframe de modalidades
modalidade_df = pd.concat([modalidades['Brasil'],
                         pct_modalidades['Brasil'],
                         modalidades['Santa Catarina'],
                         pct_modalidades['Santa Catarina'],
                         modalidades['Região Metropolitana de Florianópolis'],
                         pct_modalidades['Região Metropolitana de Florianópolis'],
                         modalidades['Florianópolis'],
                         pct_modalidades['Florianópolis']
                         ], axis='columns')
modalidade_df.columns = ['BR', '% (BR)', 'SC', '% (SC)', 'RMF', '% (RMF)', 'FPolis', '% (Fpolis)']

