[Link do vídeo 1](https://www.loom.com/share/cb1eb7c8241e45368069c27767282fd9?sid=0722c21c-1444-4a2b-afef-89cdae3902df)
[Link do vídeo 2](https://www.loom.com/share/0dab42096d5c4465acdd2ee6c37adae7?sid=3bc69c6b-6be8-408f-b1ba-45d6179ce8f8)
[Link do vídeo 3](https://www.loom.com/share/4b624586472a4e4da7d1ce94aebf9b33?sid=847df4ed-5542-40d5-bb93-5d2bf0d71b3b)

**Projeto: Análise de Redes de PoS Tagging e NER com NetworkX em livros de Machado de Assis**

### Objetivo do Projeto

O objetivo deste projeto é realizar uma análise aprofundada das Redes de PoS Tagging (Part of Speech) e NER (Named Entity Recognition) em 3 livros de Machado de Assis (Quincas Borbas, Helena e Dom Casmurro). Para isso, utilizarei a biblioteca NetworkX para criar grafos que representem as relações entre as palavras nas categorias gramaticais e entidades nomeadas presentes nos textos.

### Introdução Teórica

**Processamento de Linguagem Natural (NLP)** 

O Processamento de Linguagem Natural (NLP) é um campo da inteligência artificial que se concentra na interação entre computadores e a linguagem humana. O principal objetivo do NLP é capacitar as máquinas a entender, interpretar e responder à linguagem natural de maneira significativa. Isso envolve uma série de tarefas, como análise de sentimentos, tradução automática, reconhecimento de voz e extração de informações, todas voltadas para melhorar a comunicação entre humanos e sistemas computacionais. 

Com avanços recentes em modelos de linguagem, como o GPT-4, o NLP continua a desempenhar um papel crucial no desenvolvimento de tecnologias que facilitam a interação eficaz entre humanos e máquinas.

**Reconhecimento de Entidades Nomeadas (NER)** 

O Reconhecimento de Entidades Nomeadas (NER) e a Part-of-Speech Tagging (PoS) são componentes fundamentais do Processamento de Linguagem Natural (NLP). Enquanto o NER se concentra na identificação e classificação de entidades específicas em um texto, como nomes de pessoas, locais, organizações, datas e valores numéricos, a PoS Tagging analisa a estrutura gramatical do texto, atribuindo rótulos a cada palavra com base em sua função sintática, como substantivos, verbos, adjetivos, etc. Juntos, esses dois aspectos desempenham papéis complementares na análise linguística automatizada. 

O NER extrai informações significativas de documentos de texto, facilitando a compreensão contextual das entidades mencionadas, enquanto a PoS Tagging fornece insights sobre a estrutura gramatical, permitindo uma compreensão mais profunda das relações e significados entre as palavras. Essa combinação de técnicas contribui para uma abordagem abrangente na interpretação e extração de conhecimento de documentos textuais, enriquecendo a capacidade de sistemas automatizados compreenderem e processarem a linguagem natural de maneira mais sofisticada.

### Etapas do Projeto

A realização desse projeto foi feita na seguinte ordem:

1.  **Seleção e Preparação dos Textos:**
    
    *   Escolha dos livros.
    *   Coleta e preparação dos textos para análise, incluindo limpeza de dados e padronização.
2.  **Análise de PoS Tagging:**
    
    *   Utilização da biblioteca *SpaCy* de processamento de linguagem natural para realizar a marcação de partes do discurso (PoS Tagging) nos textos.
    *   Identificação das categorias gramaticais das palavras, como substantivos, verbos, adjetivos, etc.
3.  **Realização de NER:**
    
    *   Aplicação de um modelo de Named Entity Recognition para identificar e classificar entidades nomeadas nos textos, como nomes de pessoas, locais, organizações, etc.
4.  **Criação de Grafos com NetworkX:**
    
    *   Utilização da biblioteca NetworkX para criar grafos a partir das relações entre palavras identificadas nas etapas de PoS Tagging e NER.
    *   Criação de nós para cada palavra e arestas para representar as relações entre elas.
5.  **Análise de Rede:**
    
    *   Avaliação das propriedades da rede, como centralidade, densidade, etc.
    *   Identificação de padrões e estruturas interessantes na rede de PoS Tagging e NER.
6.  **Visualização da Rede:**
    
    *   Utilização da ferramenta de visualização Gephi.
    *   Destaque de padrões e insights obtidos durante a análise.
    https://minicosta.github.io/network_deploy/network/

### Ferramentas e Tecnologias Utilizadas:

*   Linguagem de programação: Python
*   Bibliotecas: SpaCy e NetworkX.

### Resultados Esperados:

Espera-se obter uma compreensão mais profunda das relações entre as palavras, categorias gramaticais e entidades nomeadas nos textos de Assis. A visualização das redes geradas permitirá identificar padrões linguísticos e semânticos, contribuindo para uma análise mais rica e abrangente da obra em questão.
