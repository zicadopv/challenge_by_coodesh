# Projeto Space Flight News

Tem como objetivo pegar os dados do site [site da API]{https://api.spaceflightnewsapi.net/v3/articles} 
e disponibilizar no nosso siSteMA para ser consumidos via API pelos clientes


### *Linguagens*
- Python

### *Frameworks*
- Django
- Django Rest Framework

### *Banco de dados*
- Postgres

### *Hospedagem*
- Heroku

## Como instalar o sistema:
- Faça o clone do projeto: 
````
git clone https://github.com/zicadopv/challenge_by_coodesh.git
````
- Entre na pasta
````
cd challenge_by_coodesh
````
- Criar uma máquina virtual, entrar e instalar as libs
````
python.exe -m venv .venv
.venv\Scripts\activate
python.exe -m pip install --upgrade pip 
pip install -r requirements.txt
````
- Faça uma cópia do arquivo **env-sample**
````
cp contrib\env-sample .env
````
- Rode as migrations
````
python manage.py migrate
````
- Criar um usuário e rodar o scripts para baixar os dados do site 
````
python manage.py createsuperuser
python api_spaceflight.py
````

## Endpoints

### Melhor maneira de acessar os endpoints é através do programa INSOMNIA

Acesso sem TOKEN
````
[GETT]http://127.0.0.1:8000/articles/ -> Lista todos os artigos da base
[GETT]http://127.0.0.1:8000/article_details/key/ -> Lista de um artigo específico
````
Acesso com TOKEN
````
[POST]http://127.0.0.1:8000/article/ -> Cria um novo artigo
[PUT]http://127.0.0.1:8000/article/key/ -> Edita um novo artigo
[DELETE]http://127.0.0.1:8000/article_delete/key/ -> Deleta um artigo
````
Para gerar o TOKEN é só acessar o endpoint a seguir e logar
````
[POST]http://127.0.0.1:8000/api/token/
````

## ***This is a challenge by Coodesh***
