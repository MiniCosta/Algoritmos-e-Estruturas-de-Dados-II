import re

# Definition of the AVLNode class for AVL tree nodes
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

# Definition of the AVLTree class for the AVL tree
class AVLTree:
    def __init__(self):
        self.root = None

    # Function for inserting a node into the AVL tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        
        # Recursive insertion based on key value
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        # Update node height and balance
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)
        
        # Perform rotations to maintain AVL property
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
    
    # Helper function to get node height
    def _get_height(self, node):
        if not node:
            return 0
        return node.height
    
    # Helper function to get node balance factor
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    # Rotations for AVL tree balancing
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

    # Function to find complete words based on a prefix
    def find_words_with_prefix(self, prefix):
        results = []
        self._find_words_with_prefix(self.root, prefix, results)
        return results

    def _find_words_with_prefix(self, node, prefix, results):
        if not node:
            return
        
        # If the node's key starts with the prefix, add it to the results list
        if node.key.startswith(prefix):
            results.append(node.key)
        
        # Recursive search in the left subtree (if necessary)
        if node.key >= prefix:
            self._find_words_with_prefix(node.left, prefix, results)
        
        # Recursive search in the right subtree
        self._find_words_with_prefix(node.right, prefix, results)

# Function to extract unique words from a text file and remove punctuation
def extract_unique_words(filename):
    unique_words = set()
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # Use regular expression to remove punctuation from the start and end of the word
                cleaned_word = re.sub(r'^\W+|\W+$', '', word)
                if cleaned_word:
                    unique_words.add(cleaned_word)
    return unique_words

# File name containing the text corpus
corpus_file = 'corpus.txt'

# Extract unique words from the file and create the AVL tree
unique_words = extract_unique_words(corpus_file)
avl_tree = AVLTree()
for word in unique_words:
    avl_tree.insert(word)

# Ask the user for a prefix and find matching words
prefix = input("Enter a prefix: ")
matching_words = avl_tree.find_words_with_prefix(prefix)
print("Matching words:", matching_words)