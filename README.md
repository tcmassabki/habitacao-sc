# Dados sobre habitação de interesse social (HIS) em Santa Catarina

## Um estudo a partir dos Programas Minha Casa Minha Vida (PMCMV) e Casa Verde e Amarela (PCVA)

O presente repositório serve como estudo para o desafio de projeto "Explorando IA Generativa em um Pipeline de ETL com Python", componente do _Santander Bootcamp 2023 - Ciência de Dados com Python_, oferecido pelo [Banco Santander](https://www.santander.com.br/) em parceria com a [Digital Innovation One](web.dio.me/).

Utilizando a noção de pipeline de ETL (Extract, Transform, Load), pretende-se, com o presente repositório, realizar um estudo preliminar sobre as políticas de habitação de interesse social (HIS) no Brasil do século XXI, tendo como foco o estado de Santa Catarina e os programas Minha Casa Minha Vida (PMCMV), de 2009 a 2020, e Casa Verde e Amarela (PCVA), de 2020 a 2022.

Os dados utilizados foram extraídos do portal [Dados Abertos](https://dadosabertos.mdr.gov.br/), do Ministério do Desenvolvimento Regional (MDR), de autoria da Secretaria Nacional de Habitação (SNH). O conjunto de dados consiste na listagem e caracterização das contrataçãoes dos referidos programas, no período de 2009 a 2021, podendos ser acessados no seguinte [link](https://dadosabertos.mdr.gov.br/dataset/cva_mcmv).

Após a obtenção dos dados, criou-se um script em Python para que os dados fossem lidos e organizados, de forma a conseguir estatísticas básicas sobre as contratações feitas no estado de Santa Catarina, especificamente sobre a distribuição de obras contratadas por programa e modalidade, nas seguintes divisões territorias: Brasil, Santa Catarina, Região Metropolitana de Florianópolis (incluindo Núcleo Metropolitano e Área de Expansão, conforme previsto em [lei](https://leisestaduais.com.br/sc/lei-complementar-n-162-1998-santa-catarina-institui-as-regioes-metropolitanas-de-florianopolis-do-vale-do-itajai-e-do-norte-nordeste-catarinense-e-estabelece-outras-providencias)) e município de Florianópolis.

Os dados foram organizados em dois arquivos .txt, no layout de tabela, sendo um para a distribuição das obras contratadas por programas e um para a distribuição das obras contratadas por modalidade dos programas.