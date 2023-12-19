import spacy
import networkx as nx
import json
from tqdm import tqdm
import os

# Carregar o modelo de linguagem para o Português (modelo grande)
nlp = spacy.load('pt_core_news_lg')

# Função para realizar a análise de PoS Tagging e NER em um texto
def analyze_text(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    
    # Realizar a análise de NER
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return {"pos_tags": pos_tags, "entities": entities}

# Função para criar um grafo a partir dos resultados da análise
def create_graph(pos_tags, entities):
    G = nx.Graph()

    # Adicionar nós e arestas ao grafo
    for word, pos_tag in pos_tags:
        G.add_node(word, pos_tag=pos_tag)

    for entity, entity_type in entities:
        G.add_node(entity, entity_type=entity_type)

    return G

# Mapear categorias gramaticais para cores
node_colors = {
    "NOUN": "blue",
    "PROPN": "green",
    "ADP": "red",
    "MISC": "gray"
}

# Função para adicionar cores aos nós do grafo com base nas categorias gramaticais
def add_node_colors(graph):
    for node, data in graph.nodes(data=True):
        entity_type = data.get('pos_tag', 'MISC')  # Default para 'MISC' se a chave 'pos_tag' não existir
        data['color'] = node_colors.get(entity_type, 'gray')

# Função para salvar um grafo em formato GEXF
def save_graph_as_gexf(graph, file_path):
    nx.write_gexf(graph, file_path)

# Função para processar os resultados da NER
def process_ner_results(book_id, data_directory):
    ner_file_path = os.path.join(data_directory, f'{book_id}_ner_results.json')

    # Verificar se o arquivo já existe
    if os.path.exists(ner_file_path):
        with open(ner_file_path, 'r', encoding='utf-8') as ner_file:
            ner_data = json.load(ner_file)
        print(f"Dados NER carregados do arquivo: {ner_file_path}")
    else:
        # Se o arquivo não existe, realizar a análise de PoS Tagging e NER
        file_path = os.path.join(data_directory, f'{book_id}.txt')

        with open(file_path, 'r', encoding='utf-8') as file:
            book_text = file.read()

        # Realizar a análise de PoS Tagging e NER
        result = analyze_text(book_text)

        # Salvar os resultados em um arquivo NER
        with open(ner_file_path, 'w', encoding='utf-8') as ner_file:
            json.dump(result, ner_file, ensure_ascii=False, indent=4)

        print(f"Dados NER salvos em: {ner_file_path}")
        ner_data = result

    return ner_data

# Diretório onde os arquivos de NER e JSON estão localizados
base_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(base_directory, 'machado_de_assis')

# Lista de IDs dos livros de Machado de Assis no Projeto Gutenberg
machado_de_assis_books = [55752, 55682, 67162]

# Iterar sobre os livros
for book_id in machado_de_assis_books:
    # Processar os resultados da NER
    ner_data = process_ner_results(book_id, data_directory)

    # Criar o grafo
    G = create_graph(ner_data["pos_tags"], ner_data["entities"])

    # Adicionar cores aos nós do grafo
    add_node_colors(G)

    # Salvar o grafo em um arquivo JSON
    output_graph_path = os.path.join(data_directory, f'{book_id}_graph.json')
    with open(output_graph_path, 'w', encoding='utf-8') as json_file:
        json.dump(nx.node_link_data(G), json_file, ensure_ascii=False, indent=4)

    print(f"Grafo do Livro {book_id} salvo em: {output_graph_path}")

    # Salvar o grafo em um arquivo GEXF
    output_gexf_path = os.path.join(data_directory, f'{book_id}_graph.gexf')
    save_graph_as_gexf(G, output_gexf_path)

    print(f"Grafo do Livro {book_id} salvo em: {output_gexf_path}")
