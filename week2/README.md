<a href=“https://www.loom.com/share/89f11c49cf3645e899c1cbf113dfbfab?sid=e6f412ca-d3bc-4ee7-a2f3-2409f7e7641a“>Link do Vídeo</a>

**SISTEMA DE AUTOCOMPLETAR PALAVRAS**

**INTRODUÇÃO**

Esse projeto tem o objetivo de criar um programa capaz de receber um input de texto do usuário e buscar palavras que comecem com essa entrada usando árvores AVL e python, bem como gerar uma discussão sobre o desempenho desse algoritmo.

**METODOLOGIA**

Com o auxílio do GPT-3.5, foi possível criar o programa 'search.py', o qual é capaz de instanciar uma Árvore AVL e incorporar o corpus (banco de textos usado como referência), além de possuir a função de busca. O corpus usado é composto pelas obras "Crime e Castigo" e "Os Demônios" de Fiódor Dostoiévski, em inglês, obtidos através do <a href="https://www.gutenberg.org/">Projeto Gutenberg.</a>

**ANÁLISE DE DESEMPENHO**

Comparar o desempenho da árvore AVL com uma estrutura de dados mais simples, como uma lista ou uma árvore binária de busca sem balanceamento, pode nos dar uma ideia da eficiência do balanceamento em relação à simplicidade. Vamos analisar o desempenho das três estruturas de dados em termos de tempo de inserção, altura da árvore e tempo de busca.

*Lista Simples*

Tempo de Inserção: O tempo de inserção em uma lista simples é O(1) para inserções no final da lista, mas O(n) para inserções no início, já que todos os elementos precisam ser movidos. Em média, pode ser considerado O(n/2) para inserções aleatórias.

Altura da Lista: A lista não possui uma estrutura hierárquica como uma árvore, portanto, não há altura da lista.

Tempo de Busca: O tempo de busca em uma lista simples é O(n) no pior caso, pois todos os elementos precisam ser verificados.

*Árvore Binária de Busca não Balanceada*

Tempo de Inserção: O tempo de inserção em uma árvore binária de busca não balanceada é O(n) no pior caso, quando a árvore não é balanceada e se parece com uma lista encadeada. No melhor caso, pode ser O(log n) se a árvore for balanceada.

Altura da Árvore: A altura da árvore binária de busca não balanceada pode ser O(n) no pior caso, tornando-se semelhante a uma lista encadeada.

Tempo de Busca: O tempo de busca em uma árvore binária de busca não balanceada pode ser O(n) no pior caso, quando a árvore não é balanceada, ou O(log n) no melhor caso.

*Árvore AVL*

Tempo de Inserção: O tempo de inserção em uma árvore AVL é maior do que em uma lista simples ou uma árvore binária de busca não balanceada devido às operações de rotação necessárias para manter o balanceamento. O tempo médio de inserção é O(log n) devido à propriedade de balanceamento, onde "n" é o número de elementos na árvore.

Altura da Árvore: A árvore AVL é projetada para manter uma altura balanceada, o que significa que sua altura é garantida como O(log n), onde "n" é o número de elementos na árvore.

Tempo de Busca: O tempo de busca em uma árvore AVL é O(log n), já que a árvore é equilibrada.

Além dessas comparações, o tamanho do corpus, ou seja, o número de palavras únicas que você insere em uma árvore AVL, tem um impacto significativo no desempenho dessa estrutura de dados. Vamos analisar o impacto em diferentes aspectos:

Tempo de Inserção: À medida que o tamanho do corpus aumenta, o tempo de inserção em uma árvore AVL aumenta. Isso ocorre porque a árvore precisa ser balanceada após cada inserção para manter a propriedade AVL. O tempo de inserção médio é O(log n), mas à medida que "n" aumenta, o tempo médio de inserção também aumenta. Em termos práticos, o tempo de inserção em uma árvore AVL para um corpus pequeno pode ser negligenciável, mas para um corpus muito grande, o tempo de inserção pode ser significativo.

Altura da Árvore: O tamanho do corpus influencia diretamente a altura da árvore AVL. Quanto mais palavras únicas você inserir, mais profunda a árvore se tornará. Idealmente, você deseja manter a altura da árvore próxima a O(log n) para garantir um desempenho eficiente nas operações de busca.
Se o corpus for grande e as palavras forem inseridas em uma ordem que não mantenha o balanceamento, a altura da árvore pode se aproximar de O(n), tornando as operações de busca muito menos eficientes.

Tempo de Busca: O tempo de busca em uma árvore AVL é influenciado pelo tamanho do corpus, principalmente pela altura da árvore. Quanto mais alto a árvore, mais tempo leva para encontrar um elemento.
À medida que o tamanho do corpus aumenta, o tempo de busca médio tende a aumentar, embora permaneça na ordem de O(log n) quando a árvore está equilibrada.

Espaço em Memória: O tamanho do corpus também afeta o espaço em memória necessário para armazenar a árvore AVL. À medida que mais palavras são inseridas, a árvore cresce e requer mais espaço em memória para armazenar os nós e suas chaves.

**CONCLUSÃO**

A árvore AVL tem um melhor desempenho em termos de altura da árvore e tempo de busca, mantendo uma altura balanceada.
Uma lista simples é mais eficiente em termos de tempo de inserção no final, mas pior em termos de busca.
A árvore binária de busca não balanceada pode ter um desempenho semelhante ao de uma lista no pior caso, a menos que seja mantida balanceada.

Paralelamente, o tamanho do corpus afeta o desempenho da árvore AVL principalmente em termos de tempo de inserção e altura da árvore. Para garantir um desempenho eficiente, é importante manter a árvore balanceada, especialmente se você estiver lidando com grandes conjuntos de dados. Isso pode ser alcançado através da utilização de técnicas adequadas de inserção, como inserção aleatória ou rebalanceamento periódico da árvore. Além disso, ao lidar com grandes corpora, pode ser útil considerar outras estruturas de dados, dependendo dos requisitos específicos do seu aplicativo, como estruturas de hash ou índices invertidos.
