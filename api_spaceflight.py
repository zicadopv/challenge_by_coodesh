from requests import get
import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_space_flight.settings")
import django

django.setup()
from voos.models import Voo

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[1;33m"

result = get('https://api.spaceflightnewsapi.net/v3/articles')
try:
    result.raise_for_status()
except Exception as err:
    print(err)
else:
    for dado in json.loads(result.text):
        voo = Voo()
        voo.key = dado['id']
        voo.title = dado['title']
        voo.url = dado['url']
        voo.image_url = dado['imageUrl']
        voo.news_site = dado['newsSite']
        voo.summary = dado['summary']
        voo.published_at = dado['publishedAt']
        voo.updated_at = dado['updatedAt']
        voo.featured = dado['featured']
        lista = []
        [lista.append(r) for r in dado['launches']]
        voo.launches = lista
        lista = []
        [lista.append(r) for r in dado['events']]
        voo.events = lista
        try:
            print(f'{"*" * 80}\nSalvar no banco de dados..: {RED}{voo.title}{RESET}')
            voo.save()
            print(f'Salvo com sucesso!!!\n{"--" * 80}')
        except Exception as err:
            print(f'{"--" * 80}\nO registro.: {REVERSE}{voo.title}{RESET} deu erro!!!!\n')
            print(f'{err}\n{"*" * 80}')
            pass
