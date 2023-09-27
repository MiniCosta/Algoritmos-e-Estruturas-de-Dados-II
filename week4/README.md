[Link do vídeo](https://www.loom.com/share/973a5f2ec90c4c9d81fa28e0a87f9452?sid=bf1e8701-e36f-4aa4-948d-278dff8fe1cd)

**Construindo Consultas Rápidas em um CSV**

**INTRODUÇÃO**

Este projeto tem como objetivo extender o projeto guiado da Dataquest "Building Fast Queries on a CSV", baseado no 
database *"Laptop Prices"* fornecido pelo *Kaggle*, do curso de Introdução a Algoritmos. Para tal, serão implementadas as 
funções sugeridas no final do projeto, além de uma análise da complexidade dos algoritmos implementados, considerando os 
aspectos de Big O, Big θ (Theta), e Big Ω (Omega).

**METODOLOGIA**

O código base foi escrito durante o curso do Dataquest, e foi comparado ao 
<a href="https://github.com/dataquestio/solutions/blob/master/Mission481Solution.ipynb">código-solução</a> fornecido. 
As funções adicionais são: elaborar um sistema de filtragem para achar produtos entre uma faixa de preço mínimo e máximo; criar um 
sistema de busca que acha o menor preço dados os parâmetros de busca *RAM* e *Armazenamento*. Essas funções foram 
escritas com ajuda do GPT-3.5 e estão documentadas no *inventory.py*. Por meio da biblioteca *re*(regular expression), foi 
possível filtrar adequadamente os sufixos "GB" e "TB", assim como "HDD" e "SSD", de maneira que o input pode ter o formato 
ideal (ex: 8GB e 500GB HDD).

**ANÁLISE DE DESEMPENHO**

A análise de complexidade vai levar em consideração os casos de Big O, Big θ (Theta) e Big Ω (Omega) para as funções adicionais, sendo elas:

*find_laptops_in_price_range*

Complexidade de Tempo (Big O):

Nessa função há um loop que itera por todas as linhas do inventário, que possui n linhas, onde n é o número de laptops no inventário. Dentro do loop, há apenas comparações para verificar se o preço de cada laptop está dentro da faixa de preço especificada. Portanto, a complexidade de tempo da função é dominada pelo loop que itera pelas linhas do inventário, resultando em uma complexidade de tempo de O(n).

Complexidade de Tempo (Big Theta e Big Omega):

Numa função de filtragem como essa, não há necessariamente um "melhor caso", pois independentemente dos preços min e max estabelecidos, a função ainda vai iterar o inventário inteiro em busca de produtos dentro dos parâmetros. Por isso, tanto Big Theta quanto Big Omega são também O(n).

*find_cheapest_laptop_with_characteristics*

Complexidade de Tempo (Big O): 

Nessa função, após a criação de uma variável preço com valor muito alto, o algoritmo itera pelo inventário de 'n' laptops em busca de um produto que tenha os mesmos parâmetros de busca e um preço menor. Mais um caso simples de um pior caso O(n).

Complexidade de Tempo (Big Theta e Big Omega):

Considerando apenas os casos em que o input está no formatodo correto, no melhor caso o algoritmo ainda deve buscar no inventário inteiro um preço menor que o atual, até o final. Por isso, assim como na outra função, o Big Theta quanto Big Omega são também O(n).

**CONCLUSÃO** 

Algoritmos de filtragem, que envolvem percorrer uma lista de elementos e verificar quais deles satisfazem determinados critérios, muitas vezes têm uma complexidade de tempo de O(n), onde "n" representa o número de elementos na lista. Isso ocorre porque, em sua forma mais simples, você precisa examinar cada elemento da lista para determinar se ele atende aos critérios de filtragem ou não. 

No entanto, em alguns casos, é possível otimizar algoritmos de filtragem usando estruturas de dados específicas ou algoritmos especializados. Por exemplo, usando índices ou estruturas de dados auxiliares; se for notório com antecedência quais critérios de filtragem serão aplicados com frequência, pode criar índices ou estruturas de dados auxiliares que acelerem o processo de filtragem.
Além disso, em ambientes de computação paralela, é possível realizar a filtragem em paralelo, o que pode acelerar significativamente o processo, especialmente para conjuntos de dados grandes.
