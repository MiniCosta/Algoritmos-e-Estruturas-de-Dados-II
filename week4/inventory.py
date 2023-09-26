import csv
import time
import random
import re  

# Abrir o arquivo CSV com informações sobre laptops
with open('laptops.csv') as f:
    reader = csv.reader(f)
    rows = list(reader)
    header = rows[0]
    rows = rows[1:]

# Função que extrai o preço de uma linha
def row_price(row):
    return row[-1]

class Inventory():
    
    def __init__(self, csv_filename):
        # Inicialização da classe Inventory com o arquivo CSV especificado
        with open(csv_filename) as f:
            reader = csv.reader(f)
            rows = list(reader)
        self.header = rows[0]
        self.rows = rows[1:]
        for row in self.rows:
            row[-1] = float(row[-1])  # Converter o preço para um número de ponto flutuante
        
        # Criar um mapeamento de ID para a linha correspondente
        self.id_to_row = {}
        for row in self.rows:
            self.id_to_row[row[0]] = row
        
        # Criar um conjunto de preços únicos e ordenar as linhas por preço
        self.prices = set()
        for row in self.rows:
            self.prices.add(row[-1])
        self.rows_by_price = sorted(self.rows, key=row_price) 
    
    def get_laptop_from_id(self, laptop_id):
        # Obter um laptop pelo ID (versão lenta)
        for row in self.rows:
            if row[0] == laptop_id:
                return row
        return None
    
    def get_laptop_from_id_fast(self, laptop_id):
        # Obter um laptop pelo ID (versão rápida usando mapeamento)
        if laptop_id in self.id_to_row:
            return self.id_to_row[laptop_id]
        return None

    def check_promotion_dollars(self, dollars):
        # Verificar se há uma combinação de laptops que somam ao valor em dólares (versão lenta)
        for row in self.rows:
            if row[-1] == dollars:
                return True
        for row1 in self.rows:
            for row2 in self.rows:
                if row1[-1] + row2[-1] == dollars:
                    return True
        return False
    
    def check_promotion_dollars_fast(self, dollars):
        # Verificar se há uma combinação de laptops que somam ao valor em dólares (versão rápida usando conjunto)
        if dollars in self.prices:
            return True
        for price in self.prices:
            if dollars - price in self.prices:
                return True
        return False
    
    def find_laptop_with_price(self, target_price):
        # Encontrar um laptop com um preço específico (versão binária)
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            value = self.rows_by_price[range_middle][-1]
            if value == target_price:
                return range_middle
            elif value < target_price:
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1
        if self.rows_by_price[range_start][-1] != target_price:
            return -1
        return range_start
    
    def find_first_laptop_more_expensive(self, target_price):
        # Encontrar o primeiro laptop mais caro que um preço específico (versão binária)
        range_start = 0
        range_end = len(self.rows_by_price) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            price = self.rows_by_price[range_middle][-1]
            if price > target_price:
                range_end = range_middle
            else:
                range_start = range_middle + 1
        if self.rows_by_price[range_start][-1] <= target_price:
            return -1
        return range_start
    
    def find_laptops_in_price_range(self, min_price, max_price):
        laptops_in_range = []
        for row in self.rows:
            price = row[-1]
            if min_price <= price <= max_price:
                laptops_in_range.append(row)
        return laptops_in_range

    def find_cheapest_laptop_with_characteristics(self, ram_gb, storage_gb):
        # Extrair os valores numéricos e as unidades das entradas
        ram_match = re.match(r'(\d+)GB', ram_gb, re.I)  # Extrair xGB da entrada da RAM
        storage_match = re.match(r'(\d+)(GB|TB)\s*(HDD|SSD)?', storage_gb, re.I)  # Extrair y(GB ou TB)(HDD ou SSD) da entrada de armazenamento

        if not (ram_match and storage_match):
            return None  # Retornar None se as entradas não corresponderem ao padrão

        ram_value = int(ram_match.group(1))  # Extrair o valor numérico da RAM
        storage_value = int(storage_match.group(1))  # Extrair o valor numérico do armazenamento
        storage_unit = storage_match.group(2)  # Extrair a unidade (GB ou TB) do armazenamento
        storage_type = storage_match.group(3)  # Extrair o tipo de armazenamento (HDD ou SSD) se presente

        cheapest_laptop = None
        cheapest_price = float('inf')  # Inicializar o preço mais baixo como infinito

        for row in self.rows:
            price = row[-1]  # Obter o preço do laptop
            ram_str = row[7]  # Coluna da RAM 
            storage_str = row[8]  # Coluna da capacidade de armazenamento

            # Usar expressões regulares para extrair os valores numéricos e as unidades
            ram_match = re.search(r'(\d+)GB', ram_str, re.I)
            storage_match = re.search(r'(\d+)(GB|TB)\s*(HDD|SSD)?', storage_str, re.I)

            if not (ram_match and storage_match):
                continue  # Ignorar linhas com valores inválidos

            laptop_ram_value = int(ram_match.group(1))  # Extrair o valor numérico da RAM do laptop
            laptop_storage_value = int(storage_match.group(1))  # Extrair o valor numérico do armazenamento do laptop
            laptop_storage_unit = storage_match.group(2)  # Extrair a unidade (GB ou TB) do armazenamento do laptop
            laptop_storage_type = storage_match.group(3)  # Extrair o tipo de armazenamento (HDD ou SSD) do laptop se presente

            # Verificar se as características atendem aos critérios
            if (
                laptop_ram_value >= ram_value
                and (
                    (laptop_storage_unit == "GB" and storage_unit == "GB")
                    or (laptop_storage_unit == "TB" and storage_unit == "TB")
                )
                and (not storage_type or (storage_type and laptop_storage_type and storage_type.upper() == laptop_storage_type.upper()))
                and price < cheapest_price
            ):
                cheapest_laptop = row  # Atualizar o laptop mais barato
                cheapest_price = price  # Atualizar o preço mais baixo

        return cheapest_laptop  # Retornar o laptop mais barato que corresponda às características desejadas


    
inventory = Inventory('laptops.csv')

ids = [str(random.randint(1000000, 9999999)) for _ in range(10000)] # Gerar IDs aleatórios para consultas

#Calcular o tempo de execução de get_laptop_from_id e get_laptop_from_id_fast
total_time_no_dict = 0
for identifier in ids:
    start = time.time()
    inventory.get_laptop_from_id(identifier)
    end = time.time()
    total_time_no_dict += end - start

total_time_dict = 0
for identifier in ids:
    start = time.time()
    inventory.get_laptop_from_id_fast(identifier)
    end = time.time()
    total_time_dict += end - start

prices = [random.randint(100, 5000) for _ in range(100)] # Gerar preços aleatórios para consultas de promoção

# Calcular o tempo de execução de check_promotion_dollars e check_promotion_dollars_fast
total_time_no_set = 0
for price in prices:
    start = time.time()
    inventory.check_promotion_dollars(price)
    end = time.time()
    total_time_no_set += end - start

total_time_set = 0
for price in prices:
    start = time.time()
    inventory.check_promotion_dollars_fast(price)
    end = time.time()
    total_time_set += end - start

#Testes das funções implementadas

#Imprimir o cabeçalho e as cinco primeiras linhas do arquivo CSV\n
print('#Imprimir o cabeçalho e as cinco primeiras linhas do arquivo CSV\n')
print(header)
for i in range(5):
    print(rows[i])
print('\n')

#Imprimir o cabeçalho e o número total de linhas do inventário\n
print('#Imprimir o cabeçalho e o número total de linhas do inventário\n')
print(inventory.header)
print(len(inventory.rows))
print('\n')

#Testar a função get_laptop_from_id com IDs existentes e inexistentes\n
print('#Testar a função get_laptop_from_id com IDs existentes e inexistentes\n')
print(inventory.get_laptop_from_id('33'))
print(inventory.get_laptop_from_id('151551'))
print('\n')

#Testar a função get_laptop_from_id_fast com IDs existentes e inexistentes\n
print('#Testar a função get_laptop_from_id_fast com IDs existentes e inexistentes\n')
print(inventory.get_laptop_from_id_fast('45'))
print(inventory.get_laptop_from_id_fast('3362736'))
print('\n')

#Comparar o tempo de execução entre get_laptop_from_id e get_laptop_from_id_fast\n
print('#Comparar o tempo de execução entre get_laptop_from_id e get_laptop_from_id_fast\n')
print(total_time_no_dict)
print(total_time_dict)
print('get_laptop_from_id_fast é '+ str(total_time_no_dict / total_time_dict) + ' vezes mais rápido que get_laptop_from_id')
print('\n')

#Testar a função check_promotion_dollars com valores de dólares\n
print('#Testar a função check_promotion_dollars com valores de dólares\n')
print(inventory.check_promotion_dollars(1000))
print(inventory.check_promotion_dollars(442))
print('\n')

#Testar a função check_promotion_dollars_fast com valores de dólares\n
print('#Testar a função check_promotion_dollars_fast com valores de dólares\n')
print(inventory.check_promotion_dollars_fast(1000))
print(inventory.check_promotion_dollars_fast(442))
print('\n')

#Comparar o tempo de execução entre check_promotion_dollars e check_promotion_dollars_fast\n
print('#Comparar o tempo de execução entre check_promotion_dollars e check_promotion_dollars_fast\n')
print(total_time_no_set)                                 
print(total_time_set)
print('check_promotion_dollars_fast é '+ str(total_time_no_set/total_time_set) + ' vezes mais rápido que check_promotion_dollars')
print('\n')

# Imprimir os laptops dentro do intervalo de preços\n
print('# Imprimir os laptops dentro do intervalo de preços\n')
min_price = 980
max_price = 1000
laptops_in_range = inventory.find_laptops_in_price_range(min_price, max_price)

for laptop in laptops_in_range:
    print(laptop)
print('\n')

#Imprimir laptop mais barato com as características desejadas\n
print('#Imprimir laptop mais barato com as características desejadas\n')

ram_gb = '4GB'
storage_gb = '256GB HDD'
cheapest_laptop = inventory.find_cheapest_laptop_with_characteristics(ram_gb, storage_gb)

if cheapest_laptop:
    print("Laptop mais barato com as características desejadas:")
    print(cheapest_laptop)
else:
    print("Nenhum laptop corresponde às características desejadas. Verifique a ortografia.")