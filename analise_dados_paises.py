import statistics
import math
from pprint import pprint

# Import do dicionário 
from dados import dados_paises 


# Funções auxiliares
def limpar_e_converter(valor_texto):
    if not isinstance(valor_texto, str):
        return float(valor_texto)

# Remove pontuações
    valor_limpo = valor_texto.replace("%", "").replace(".", "")
    valor_limpo = valor_limpo.replace(",", ".")
    
    return float(valor_limpo)


def extrair_dados_numericos(tipo_dado):
    valores = []
    for pais, info in dados_paises.items():
        try:
            valor_texto = info[tipo_dado]
            valor_numerico = limpar_e_converter(valor_texto)
            valores.append(valor_numerico)
        except (KeyError, ValueError):
            pass
            
    return valores

# Funções de exibição
# Apresenta os dados a partir do tipo de dado
def apresenta_dado():
    print("FUNÇÃO: 1. Apresentar Dado (para todos os países)")
    print("Chaves válidas: pib, idh, inflacao, gini, populacao.")
    tipo_dado = input("Digite o nome do dado que deseja visualizar: ").lower().strip()

    if not tipo_dado: return

    encontrou_algum = False
    print(f"\n--- VALORES DE {tipo_dado.upper()} ---\n")

    for pais, info in dados_paises.items():
        try:
            print(f"{pais}: {info[tipo_dado]}")
            encontrou_algum = True
        except KeyError:
            print(f"{pais}: Dado não disponível ({tipo_dado})")

    if not encontrou_algum:
        print(f"\nERRO: A chave '{tipo_dado}' não foi encontrada no banco de dados.")

# Apresenta os dados a partir do nome do país
def apresenta_pais():
    print("FUNÇÃO: 2. Apresentar País (todos os dados)")
    
    nome_pais = input("Digite o nome do país: ").strip().title()

    if not nome_pais: return

    try:
        dados = dados_paises[nome_pais]
        
        print(f"\n--- Dados completos para {nome_pais.upper()} ---")
        pprint(dados)

    except KeyError:
        print(f"\nERRO: O país '{nome_pais}' não consta no banco de dados.")


# Funções de estatísticas

# Calcula a média aritmética do dado 
def calcula_media_aritmetica():
    print("FUNÇÃO: 3. CÁLCULO DE MÉDIA ARITMÉTICA")
    tipo_dado = input("Qual dado para cálculo da Média? ").lower().strip()
    
    if not tipo_dado: return

    valores = extrair_dados_numericos(tipo_dado)
    N = len(valores)
    
    if N > 0:
        media = sum(valores) / N
        print(f"\n--- Resultado de {tipo_dado.upper()} ---")
        print(f"Total de amostras válidas: {N}")
        print(f"Média Aritmética: {media:,.4f}")
    else:
        print(f"\nERRO: Não foi possível calcular a média do dado '{tipo_dado}'.")

# Calcula a variância
def calcula_variancia_desvio():
    print("FUNÇÃO: 4. CÁLCULO DE VARIÂNCIA E DESVIO PADRÃO")
    tipo_dado = input("Qual dado para cálculo da Variância? ").lower().strip()
    
    if not tipo_dado: return

    valores = extrair_dados_numericos(tipo_dado)
    N = len(valores)
    
    if N < 2:
        print("\nERRO: É necessário pelo menos 2 amostras para calcular a variância.")
        return

    # 1. Calcula a Média
    media = sum(valores) / N
    
    # 2. Calcula a soma das diferenças quadradas (xi - média)^2
    soma_diferencas_quadradas = sum((x - media) ** 2 for x in valores)
    
    # 3. Calcula a Variância (sigma^2)
    variancia = soma_diferencas_quadradas / N
    
    # 4. Calcula o Desvio Padrão (sigma)
    desvio_padrao = math.sqrt(variancia)
    
    print(f"\n--- Resultado de {tipo_dado.upper()} ---")
    print(f"Amostras Válidas: {N}")
    print(f"Média: {media:,.4f}")
    print(f"Variância: {variancia:,.4f}")
    print(f"Desvio Padrão: {desvio_padrao:,.4f}")
    print("\n[A Variância mede o quão disperso o conjunto de dados está em relação à média.]")

# Calcula a média ponderada partindo de um dado e um peso
def calcula_media_ponderada():
    print("FUNÇÃO: 5. CÁLCULO DE MÉDIA PONDERADA")
    
    tipo_dado = input("Qual dado (VALOR) você deseja analisar? ").lower().strip()
    tipo_peso = input("Qual dado usar como PESO (ex: populacao)? ").lower().strip()

    if not tipo_dado or not tipo_peso: return

    soma_ponderada = 0.0
    peso_total = 0.0
    paises_utilizados = 0

    # Loop do cálculo
    for pais, info in dados_paises.items():
        try:
            valor = limpar_e_converter(info[tipo_dado])
            peso = limpar_e_converter(info[tipo_peso])
            
            soma_ponderada += (valor * peso)
            peso_total += peso
            paises_utilizados += 1
            
        except (KeyError, ValueError):
            pass

    if paises_utilizados > 0 and peso_total > 0:
        media_ponderada = soma_ponderada / peso_total
        print(f"\n--- Média Ponderada ---")
        print(f"Total de amostras válidas: {paises_utilizados}")
        print(f"Média Ponderada de {tipo_dado.upper()} por {tipo_peso.upper()}: {media_ponderada:,.4f}")
    else:
        print(f"\nERRO: Não foi possível calcular. Verifique se as chaves '{tipo_dado}' e '{tipo_peso}' são válidas.")


# Função que calcula a mediana de um dado
def calcula_mediana():
    print("FUNÇÃO: 6. CÁLCULO DE MEDIANA")
    tipo_dado = input("Qual dado para cálculo da Mediana? ").lower().strip()
    
    if not tipo_dado: return

    valores = extrair_dados_numericos(tipo_dado)
    N = len(valores)
    
    if N > 0:
        mediana = statistics.median(valores)
        
        print(f"\n--- Resultado de {tipo_dado.upper()} ---")
        print(f"Total de amostras válidas: {N}")
        print(f"Mediana (Valor Central): {mediana:,.4f}")
    else:
        print(f"\nERRO: Não foi possível calcular a mediana do dado '{tipo_dado}'.")


# Menu para o usuário escolher o que ele quer visualizar do programa

def menu_principal():
    while True:
        print("\n" + "="*70)
        print("SISTEMA DE ANÁLISE DE DADOS GLOBAIS")
        print("="*70)
        print("FUNÇÕES DE EXIBIÇÃO (20 PONTOS):")
        print("  1. Apresentar um Dado (para todos os países)")
        print("  2. Apresentar um País (todos os dados)")
        print("-" * 70)
        print("FUNÇÕES ESTATÍSTICAS (15 PONTOS CADA):")
        print("  3. Média Aritmética")
        print("  4. Variância e Desvio Padrão (REQ. Variância)")
        print("  5. Média Ponderada")
        print("  6. Mediana (Função Estatística Extra)")
        print("-" * 70)
        print("  0. Sair")
        print("="*70)
        
        escolha = input("Selecione uma opção (0-6): ").strip()
        print("\n")
        
        if escolha == '1':
            apresenta_dado()
        elif escolha == '2':
            apresenta_pais()
        elif escolha == '3':
            calcula_media_aritmetica()
        elif escolha == '4':
            calcula_variancia_desvio()
        elif escolha == '5':
            calcula_media_ponderada()
        elif escolha == '6':
            calcula_mediana()
        elif escolha == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 0 a 6.")

if __name__ == "__main__":
    menu_principal()