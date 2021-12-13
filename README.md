# Projeto Space Flight News

Tem como objetivo pegar os dados do site [site da API]{https://api.spaceflightnewsapi.net/v3/articles} e disponibilizar no nosso siSteMA para ser consumidos via API pelos clientes


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
- Crie uma máquina virtual, entrar e instalar as libs
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
- Criar um usuário e rode o scripts para baixar os dados do site 
````
python manage.py createsuperuser
python api_spaceflight.py
````

## Usar os endpoints

- Toda requisição precisa de um TOKEN que pode ser obtido rodando 
````
````


### Referência para o desafio ***Backend Challenge Space Flight News 20210823***

https://lab.coodesh.com/zicadopv/space-flight-news-20210823?utm_source=mail&utm_medium=sendgrid&utm_campaign=website#


## Dicas

````
Ter 2 contas do github no mesmo computador:
- [by Fabricia]{https://dev.to/fabriciadiniz/como-utilizar-duas-contas-do-github-no-mesmo-computador-windows-2348}
````
