import openai
import pandas as pd
import re
from colorama import init, Fore, Style

# Inicializa a colorama para colorir o terminal
init(autoreset=True)

# Configuração da chave da API da OpenAI (adicione sua chave aqui)
openai.api_key = 'API-KEY-OPENAI'

# Função para ler o CSV com as novas estatísticas
def carregar_dados_csv(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)

# Função para processar a consulta e extrair informações sobre estatísticas do CSV
def processar_consulta(consulta, dados):
    temporada = None
    ligas_mencionadas = []

    # Procurar por temporadas mencionadas na consulta
    temporada_encontrada = re.search(r'(\d{4}/\d{4}|\d{4})', consulta)
    if temporada_encontrada:
        temporada = temporada_encontrada.group(0)

    # Procurar por ligas mencionadas na consulta (baseado em nomes presentes no CSV)
    ligas_disponiveis = dados['League'].unique()
    for liga in ligas_disponiveis:
        if liga.lower() in consulta.lower():
            ligas_mencionadas.append(liga)

    # Filtro com base nas ligas e na temporada
    if temporada:
        dados_filtrados = dados[dados['Season'].str.contains(temporada, na=False)]
    else:
        dados_filtrados = dados

    if ligas_mencionadas:
        dados_filtrados = dados_filtrados[dados_filtrados['League'].isin(ligas_mencionadas)]

    return dados_filtrados

# Função para gerar resposta usando a OpenAI com a API de chat, agora considerando as novas estatísticas
def gerar_resposta(consulta, dados):
    # Processa a consulta para extrair informações
    dados_relevantes = processar_consulta(consulta, dados)

    if not dados_relevantes.empty:
        # Selecionar colunas relevantes para exibir na resposta
        colunas_interessantes = [
            'Country', 'League', 'Season', 'Home', 'Away', 'HG', 'AG', 'Res',
            'PSCH', 'PSCD', 'PSCA', 'MaxCH', 'MaxCD', 'MaxCA', 'AvgCH', 
            'AvgCD', 'AvgCA', 'BFECH', 'BFECD', 'BFECA'
        ]
        dados_exibicao = dados_relevantes[colunas_interessantes].head().to_dict(orient='records')

        # Explicação das siglas para o prompt
        explicacao_siglas = """
        Aqui estão as explicações para as siglas dos dados:
        - Home:  time da casa.
        - Away: time visitante.
        - Season: temporada do campeonato.
        - HG: Gols marcados pelo time da casa.
        - AG: Gols sofridos pelo time da casa.
        - Res: Resultado do jogo (V, E, D).
        - PSCH: Probabilidade de o time da casa marcar o primeiro gol.
        - PSCD: Probabilidade de o time da casa marcar o primeiro gol contra.
        - PSCA: Probabilidade de o time da casa marcar o primeiro gol em um intervalo específico.
        - MaxCH: Máximo de gols marcados pelo time da casa.
        - MaxCD: Máximo de gols sofridos pelo time da casa.
        - MaxCA: Máximo de gols marcados pelo time visitante.
        - AvgCH: Média de gols marcados pelo time da casa.
        - AvgCD: Média de gols sofridos pelo time da casa.
        - AvgCA: Média de gols marcados pelo time visitante.
        - BFECH: Expectativa de gols a favor do time da casa.
        - BFECD: Expectativa de gols contra o time da casa.
        - BFECA: Expectativa de gols a favor do time visitante.
        """

        # Criar o prompt para o chat da OpenAI
        mensagens = [
            {"role": "system", "content": "Você é um assistente que responde perguntas sobre ligas de futebol."},
            {"role": "user", "content": f"{consulta}"},
            {"role": "system", "content": f"Aqui estão alguns dados relevantes: {dados_exibicao}. Baseado nisso e nas seguintes explicações das siglas: {explicacao_siglas}, responda à pergunta."}
        ]

        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            max_tokens=150
        )

        return resposta['choices'][0]['message']['content'].strip()
    else:
        return "Não consegui encontrar informações relevantes para sua consulta. Tente ser mais específico, mencionando a liga ou a temporada."

# Função para exibir pergunta e resposta formatadas
def exibir_pergunta_e_resposta(consulta, resposta):
    print(Fore.GREEN + Style.BRIGHT + "\n" + "-" * 50)
    print(Fore.GREEN + "Pergunta: " + consulta)
    print(Fore.WHITE + Style.BRIGHT + "-" * 50)
    print(Fore.WHITE + "Resposta: " + resposta)
    print(Fore.GREEN + "-" * 50 + "\n")

# Exemplo de uso
if __name__ == "__main__":
    # Nome do usuário

    # Carregar dados da liga do CSV
    caminho_csv = 'league.csv'
    dados_liga = carregar_dados_csv(caminho_csv)

    # Pergunta do usuário
    consulta_usuario = input(Fore.GREEN + Style.BRIGHT + "Qual é a sua pergunta sobre a liga? " + Fore.RESET)

    # Gerar resposta
    resposta = gerar_resposta(consulta_usuario, dados_liga)

    # Exibir a pergunta e a resposta de forma bonita
    exibir_pergunta_e_resposta(consulta_usuario, resposta)
