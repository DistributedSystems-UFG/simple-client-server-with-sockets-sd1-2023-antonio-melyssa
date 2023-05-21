[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/pmCXrCMx)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar outro tipo de servidor (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.


_________________________________________________________________________________________________________________________________-

# Aplicação Cliente-Servidor de Informações Meteorológicas

Esta é uma aplicação simples cliente-servidor que permite obter previsão do tempo, clima atual e hora atual utilizando sockets. O servidor recebe solicitações do cliente e se comunica com APIs externas de clima e tempo para obter os dados solicitados.

## Pré-requisitos

- Python 3.x

## Primeiros Passos

1. Clone o repositório ou faça o download dos arquivos do código-fonte.

2. Instale as dependências necessárias executando o seguinte comando:

pip install requests


3. Inicie o servidor:
- Abra um terminal ou prompt de comando.
- Navegue até o diretório do projeto.
- Execute o seguinte comando:
  ```
  python server.py
  ```

4. Faça solicitações a partir do cliente:
- Abra outro terminal ou prompt de comando.
- Navegue até o diretório do projeto.
- Modifique o dicionário `request_payload` no arquivo `client.py` para especificar os parâmetros desejados:
  - `"days"`: Número de dias para a previsão do tempo (por exemplo, 2).
  - `"location"`: Cidade ou localização para obter informações meteorológicas (por exemplo, "Goiânia").
  - `"action"`: Tipo de informação a ser recuperada (por exemplo, "time" para clima atual, "forecast" para previsão do tempo, "time" para hora atual).
- Execute o seguinte comando para enviar a solicitação para o servidor:
  ```
  python client.py
  ```

## Credenciais da API

As credenciais de uso da API foram obtidas gratuitamente, porém, há um limite de 1000 requests.
## Reconhecimentos

- As informações meteorológicas e de tempo são obtidas usando a API M3O (https://m3o.com/).
