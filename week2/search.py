# Definição da classe para os nós da árvore AVL
import re

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Definição da classe para a árvore AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # Função para inserção de um nó na árvore AVL
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        
        # Inserção recursiva com base no valor da chave
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        # Atualização da altura do nó e balanceamento
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)
        
        # Realização das rotações para manter a propriedade da AVL
        if balance > 1:
            if key < node.left.key:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        
        if balance < -1:
            if key > node.right.key:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)
        
        return node
    
    # Função auxiliar para obter a altura de um nó
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    # Função auxiliar para obter o fator de balanceamento de um nó
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    # Rotações para balancear a árvore AVL
    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y
    
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        
        return x

    # Função para encontrar palavras completas com base em um prefixo
    def find_words_with_prefix(self, prefix):
        results = []
        self._find_words_with_prefix(self.root, prefix, results)
        return results

    def _find_words_with_prefix(self, node, prefix, results):
        if not node:
            return
        
        # Se a chave do nó começa com o prefixo, adicionamos à lista de resultados
        if node.key.startswith(prefix):
            results.append(node.key)
        
        # Busca recursiva na subárvore esquerda (se necessário)
        if node.key >= prefix:
            self._find_words_with_prefix(node.left, prefix, results)
        
        # Busca recursiva na subárvore direita
        self._find_words_with_prefix(node.right, prefix, results)

# Função para extrair palavras únicas de um arquivo de texto e remover pontuações
def extract_unique_words(filename):
    unique_words = set()
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Utilizar expressão regular para remover pontuações do início e final da palavra
                cleaned_word = re.sub(r'^\W+|\W+$', '', word)
                if cleaned_word:
                    unique_words.add(cleaned_word)
    return unique_words

# Nome do arquivo contendo o corpus de texto
corpus_file = 'corpus.txt'

# Extrair palavras únicas do arquivo e criar a árvore AVL
unique_words = extract_unique_words(corpus_file)
avl_tree = AVLTree()
for word in unique_words:
    avl_tree.insert(word)

# Solicitar um prefixo ao usuário e encontrar palavras correspondentes
prefix = input("Enter a prefix: ")
matching_words = avl_tree.find_words_with_prefix(prefix)
print("Matching words:", matching_words)

