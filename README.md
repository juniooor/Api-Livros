# API de Livros

Esta é uma API simples para gerenciar informações sobre livros, incluindo nome, autor e data de lançamento. A API permite adicionar, atualizar, excluir e listar informações sobre livros. Além disso, existem planos para adicionar recursos adicionais no futuro, como gênero, opiniões de usuários e contagem de downloads de livros em PDF.

## Pré-requisitos

Antes de usar esta API, você deve ter o seguinte instalado:

- Python 3.11
- Django 
- Django Rest Framework (framework web em Python)


## Instalação

1. Clone este repositório para o seu sistema local:

   ```shell
   git clone https://github.com/seu-usuario/api-de-livros.git

2. Navegue até o diretório do projeto:

   ``` shell
   cd api-de-livros

3. Crie um ambiente virtual para isolar as dependências do projeto:

   ```shell
   python -m venv venv
   
4. Ative o ambiente virtual:

  * No Windows:
   
    ```shell
      venv\Scripts\activate

   
 * No macOS e Linux:

   ``` shell
   source venv/bin/activate
   
5. Instale as dependências do projeto:

   ```shell
   pip install -r requirements.txt
   
## Uso

Para iniciar o servidor da API, execute o seguinte comando:

   ```shell
   python app.py
```


A API estará disponível em **'http://localhost:5000'** .


## Endpoints
Método | Endpoint | Descrição
:------|:---------:| ---------:
GET |  /livros  |   Retorna uma lista de todos os livros.
GET  | /livros/{id}| Retorna informações sobre um livro específico.
POST  | /livros  | Adiciona um novo livro.
PUT | /livros/{id} | Atualiza informações sobre um livro existente.
DELETE | /livros/{id}: | Exclui um livro.


# Futuras Funcionalidades
Aqui estão algumas das funcionalidades que planejamos adicionar à API no futuro:

* **Gênero**: Adicionar informações sobre o gênero de cada livro.
* **Opiniões dos Usuários**: Permitir que os usuários deixem comentários e avaliações sobre os livros.
* **Contagem de Downloads de PDF**: Acompanhar o número de downloads de versões em PDF de cada livro.

# Contribuindo
Sinta-se à vontade para contribuir para este projeto. Você pode abrir problemas (issues) para relatar bugs, fazer sugestões ou criar pull requests para adicionar novos recursos.

# Licença
Este projeto está licenciado sob a Licença MIT.
