SISTEMA DE AUTOCOMPLETAR PALAVRAS

Introdução

Esse projeto tem o objetivo de criar um programa capaz de receber um input de texto do usuário e buscar palavras que comecem com essa entrada. 

Metodologia

Com o auxílio do GPT-3.5, foi possível criar o programa 'search.py', o qual é capaz de instanciar uma Árvore AVL e incorporar o corpus (banco de textos usado como referência), além de possuir a função de busca. O corpus usado é composto pelas obras "Crime e Castigo" e "Os Demônios" de Fiódor Dostoiévski, em inglês, obtidos através do Projeto Gutenberg.

Análise de Desempenho

Comparar o desempenho da árvore AVL com uma estrutura de dados mais simples, como uma lista ou uma árvore binária de busca sem balanceamento, pode nos dar uma ideia da eficiência do balanceamento em relação à simplicidade. Vamos analisar o desempenho das três estruturas de dados em termos de tempo de inserção, altura da árvore e tempo de busca.

-Árvore AVL:

Tempo de Inserção: O tempo de inserção em uma árvore AVL é maior do que em uma lista simples ou uma árvore binária de busca não balanceada devido às operações de rotação necessárias para manter o balanceamento. O tempo médio de inserção é O(log n) devido à propriedade de balanceamento, onde "n" é o número de elementos na árvore.

Altura da Árvore: A árvore AVL é projetada para manter uma altura balanceada, o que significa que sua altura é garantida como O(log n), onde "n" é o número de elementos na árvore.

Tempo de Busca: O tempo de busca em uma árvore AVL é O(log n), já que a árvore é equilibrada.

-Lista Simples:

Tempo de Inserção: O tempo de inserção em uma lista simples é O(1) para inserções no final da lista, mas O(n) para inserções no início, já que todos os elementos precisam ser movidos. Em média, pode ser considerado O(n/2) para inserções aleatórias.

Altura da Lista: A lista não possui uma estrutura hierárquica como uma árvore, portanto, não há altura da lista.

Tempo de Busca: O tempo de busca em uma lista simples é O(n) no pior caso, pois todos os elementos precisam ser verificados.

-Árvore Binária de Busca não Balanceada:

Tempo de Inserção: O tempo de inserção em uma árvore binária de busca não balanceada é O(n) no pior caso, quando a árvore não é balanceada e se parece com uma lista encadeada. No melhor caso, pode ser O(log n) se a árvore for balanceada.

Altura da Árvore: A altura da árvore binária de busca não balanceada pode ser O(n) no pior caso, tornando-se semelhante a uma lista encadeada.

Tempo de Busca: O tempo de busca em uma árvore binária de busca não balanceada pode ser O(n) no pior caso, quando a árvore não é balanceada, ou O(log n) no melhor caso.

Conclusão

A árvore AVL tem um melhor desempenho em termos de altura da árvore e tempo de busca, mantendo uma altura balanceada.
Uma lista simples é mais eficiente em termos de tempo de inserção no final, mas pior em termos de busca.
A árvore binária de busca não balanceada pode ter um desempenho semelhante ao de uma lista no pior caso, a menos que seja mantida balanceada.
A escolha entre essas estruturas de dados depende das necessidades específicas do seu aplicativo. Se você precisa de um desempenho consistente para inserção e busca, a árvore AVL é uma boa escolha. Se a inserção no final da lista é uma operação comum e a busca não é crítica, uma lista simples pode ser suficiente. A árvore binária de busca não balanceada é menos comum, pois seu desempenho pode variar amplamente dependendo da distribuição dos dados
