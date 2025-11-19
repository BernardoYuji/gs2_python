# Global Solution 2 – Análise de Dados em Python

Projeto desenvolvido para a Global Solution 2 utilizando Python para análise de indicadores socioeconômicos de diversos países. O sistema permite consultar dados, realizar cálculos estatísticos e visualizar informações através de um menu interativo.

# Estrutura do Projeto
### Descrição dos Arquivos

**analise_global.py**  
Contém a lógica principal do programa, as funções de exibição das informações, cálculos estatísticos (média, variância, desvio padrão, mediana e média ponderada), além do menu de interação com o usuário.

**dados.py**  
Arquivo que funciona como um banco de dados, contendo um dicionário com os países e seus respectivos indicadores.

## Como Executar

1. Certifique-se de que os arquivos `analise_global.py` e `dados.py` estão no mesmo diretório.  
2. Abra o Terminal ou Prompt de Comando.  
3. Navegue até o diretório onde os arquivos estão salvos.  
4. Execute o script principal:


Após isso, o sistema exibirá o menu principal para interação.

##Funcionalidades

# Funções de Exibição

1. Apresentar Dados: Exibe o valor de um indicador específico para todos os países.  
2. Apresentar País: Exibe todos os dados referentes a um país selecionado.

# Funções Estatísticas

3. Média Aritmética: Calcula a média simples de um indicador.  
4. Variância e Desvio Padrão: Calcula a variância e o desvio padrão populacional.  
5. Média Ponderada: Calcula a média ponderada de um indicador usando outro como peso.  
6. Mediana: Calcula a mediana de um indicador.

# Outras Opções

0. Sair.

# Chaves de Dados Válidas

- pib  
- idh  
- inflacao  
- gini  
- populacao  

# Funções Auxiliares

**limpar_e_converter(valor_texto)**  
Função que trata valores textuais e os converte para float.

**extrair_dados_numericos(tipo_dado)**  
Percorre o dicionário de países, aplica limpeza e conversão e retorna apenas valores numéricos válidos.

# Objetivo do Projeto

Criar uma ferramenta simples e funcional para explorar indicadores globais e aplicar cálculos estatísticos fundamentais utilizando Python.


## 👥 Equipe desenvolvedora
Bernardo Yuji Rodriguez Hanashiro RM: 565266

Gabriel Ciriaco de Oliveira Silva RM:564880

Marco Aurélio RM: 563827