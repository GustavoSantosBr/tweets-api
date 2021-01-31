# Tweets API

[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/GustavoSantosBr/)
[![Minimum Python Version](https://img.shields.io/badge/python-%5E3.9.1-blue)](https://www.python.org)

* [Introdução](#Introdução)
* [Requisitos](#Requisitos)
* [Instalação](#Instalação)
* [Configuração](#Configuração)
* [Endpoints](#Endpoints)

## Introdução

Esta API foi feita como uma forma de praticar os conceitos de DDD, e está divida em duas funcionalidades básicas:

- Coletar tweets de um usuário e processar os dados em JSON.
- Coletar tweets de um usuário e salvá-los em um arquivo CSV, atualizando-o a cada nova consulta.

## Requisitos

Para a instalação e execução do projeto, sera necessário:

- [Python](https://www.python.org/downloads)
- [pip](https://pip.pypa.io/en/stable/installing)

## Instalação

Para este exemplo, estarei utilizando o powershell. Use um terminal conforme seu sistema operacional. No terminal,
navegue até o diretório de sua preferência, e execute:

```bash
> git clone https://github.com/GustavoSantosBr/tweets-api.git
```

Navegue até a pasta {seudiretorio} utilizando:

```bash
> cd {seudiretorio} 
```

Para criar um ambiente isolado para trabalhar o projeto:

```bash
> cd python -m venv env
```

Para ativar o ambiente virtual:

```bash
> cd ./env/Scripts/activate.bat
```

Instale as depêndencias do projeto com o seguinte comando:

```bash
> pip install -r requirements.txt
```

## Configuração
Para estabelecer uma conexão segura com a API do Twitter, precisamos fornecer uma `api_key` e uma `api_secret`.         
Para obter esses dados, basta criar um perfil de desenvolvedor no Twitter. Você pode solicitar acesso [aqui](https://developer.twitter.com/en/apply-for-access).  
Quando obtiver seus dados de acesso, basta adicioná-los ao projeto, dentro do arquivo `config.ini`, localizado em `src`.

## Endpoints

**GET** `/tweets/<name>`

Busca os dados do usuário e seus tweets.

- **Parâmetros:**

  `name` — nome de usuário no Twitter.


- **Query Params:**

  `limit` — define um limite máximo de registros a serem buscados;

  `since` — define uma data como ponto de “partida” para a busca.


- **Exemplos:**

  - Request `/tweets/elonmusk`
  - Response    
     ```json
        {
          "data": {
              "user_id": 44196397,
              "user_name": "Elon Musk",
              "user_created_at": "2009-06-02T20:12:29",
              "user_tweets": [
                  {
                      "tweet_id": 1355068728128516101,
                      "created_at": "2021-01-29T08:22:15",
                      "text": "In retrospect, it was inevitable",
                      "followers_on_the_day": 44107351,
                      "retweets": 41171,
                      "favorites": 381709
                  },
                  {
                      "tweet_id": 1355021874850394114,
                      "created_at": "2021-01-29T05:16:04",
                      "text": "@RGVaerialphotos Great shot",
                      "followers_on_the_day": 44107351,
                      "retweets": 397,
                      "favorites": 18709
                  },
                  {
                      "tweet_id": 1354954300041080835,
                      "created_at": "2021-01-29T00:47:33",
                      "text": "@its_menieb Live by the sword, die by the sword",
                      "followers_on_the_day": 44107351,
                      "retweets": 1232,
                      "favorites": 14183
                  },
                  {
                      "tweet_id": 1354951746305585152,
                      "created_at": "2021-01-29T00:37:24",
                      "text": "@lexfridman Entropy",
                      "followers_on_the_day": 44107351,
                      "retweets": 1139,
                      "favorites": 30555
                  }
              ]
          }
      }
    ```
    
  - Request `/tweets/elonmusk?limit=1&since=2021-01-28`
  - Response    
    ```json
       {
          "data": {
              "user_id": 44196397,
              "user_name": "Elon Musk",
              "user_created_at": "2009-06-02T20:12:29",
              "user_tweets": [
                  {
                      "tweet_id": 1355068728128516101,
                      "created_at": "2021-01-29T08:22:15",
                      "text": "In retrospect, it was inevitable",
                      "followers_on_the_day": 44109726,
                      "retweets": 41316,
                      "favorites": 383534
                  }
              ]
          }
      }
    ```
    
  
**PUT** `/tweets/<name>/csv`

Inserir ou alterar um dataset de tweets. 
Se não existir um dataset, ele será criado e preenchido com os tweets do usuário.
Se o dataset já existir, ele irá atualizar apenas com os novos tweets que não estiverem no arquivo. 
O arquivo CSV será gerado dentro do diretório `src`.

- **Parâmetros:**

  `name` — nome de usuário no Twitter.


- **Query Params:**

  `limit` — define um limite máximo de registros a serem buscados;

  `since` — define uma data como ponto de “partida” para a busca.


- **Exemplos:**

  - Request `/tweets/elonmusk/csv`
  - Response    
     ```json
        {
            "data": {
                "updated_at": "2021-01-29T14:32:40.447900",
                "new_records": 10,
                "all_records": 10
            }
        }
     ```
    
  - Request `/tweets/elonmusk/csv` (executando uma nova requisição com o arquivo criado)  
  - Response   
     ```json
        {
            "data": {
                "updated_at": "2021-01-29T14:34:18.321131",
                "new_records": 0,
                "all_records": 10
            }
        }
     ```