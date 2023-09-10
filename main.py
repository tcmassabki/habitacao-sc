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

area_expansao =        ['Alfredo Wagner ',
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
obras_rmf            = obras_brasil[obras_brasil['txt_municipio'].isin(regiao_metropolitana_florianopolis)]

qtd_obras_br  = len(obras_brasil)
qtd_obras_sc  = len(obras_santa_catarina)
qtd_obras_rmf = len(obras_rmf)