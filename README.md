# Open AI + Bet

## Descrição

**Open AI + Bet** é uma projeto de estudo e aprendizado pessoal feito em Python que pretende servir para fornecer previsões e análises detalhadas de resultados de futebol usando dados estatísticos e inteligência artificial. Utilizando a API da OpenAI para processamento de linguagem natural, o projeto permite consultas dinâmicas sobre estatísticas de ligas de futebol e oferece insights para melhorar a tomada de decisões em apostas esportivas.

## Código do Projeto

O código principal do projeto realiza as seguintes funções:

1. **Leitura de Dados**: Carrega dados esportivos de um arquivo CSV chamado `league.csv`, que contém informações detalhadas sobre ligas, temporadas, partidas e estatísticas. O arquivo CSV pode ser obtido no site [Football Data](https://www.football-data.co.uk/brazil.php).

2. **Processamento de Consultas**: Permite que o usuário faça perguntas naturais sobre estatísticas específicas das ligas e temporadas. As consultas são processadas para extrair informações relevantes, como probabilidades de vitória, média de gols e outros parâmetros estatísticos.

3. **Integração com OpenAI**: Utiliza a API da OpenAI para gerar respostas baseadas em análise de dados e explicações das siglas usadas. A integração com a OpenAI permite uma resposta mais precisa e contextualizada às perguntas do usuário.

4. **Interface de Usuário**: A interação com o usuário é feita via terminal, com uma interface colorida que destaca perguntas e respostas de forma clara e atraente.

## Dependências

- **Python**: Linguagem principal utilizada para o desenvolvimento do aplicativo.
- **Pandas**: Biblioteca para manipulação e análise de dados em Python.
- **OpenAI API**: Utilizada para gerar respostas baseadas em análise de dados e processamento de linguagem natural.
- **Colorama**: Biblioteca para adicionar cores ao texto no terminal, melhorando a experiência do usuário.

## Como Usar

1. **Configuração**: Substitua `'sua-chave-da-api'` no código pela sua chave de API da OpenAI.
2. **Dados**: Certifique-se de que o arquivo CSV `league.csv` está disponível no mesmo diretório que o script Python. O arquivo pode ser obtido em [Football Data](https://www.football-data.co.uk/brazil.php).
3. **Execução**: Execute o script Python no terminal. Insira seu nome quando solicitado e faça uma pergunta sobre a liga de futebol.

   ```shell
   python seu_script.py
