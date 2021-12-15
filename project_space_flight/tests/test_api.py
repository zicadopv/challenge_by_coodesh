import json
import uuid

import pytest
from django.urls import reverse


@pytest.fixture
def resp(client):
    resp = client.get('https://127.0.0.1:8000')
    return resp

@pytest.fixture
def test_password():
   return 'strong-test-pass'


def popular_banco_api():
    ...

def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.django_db
def test_list_(client):
   url = reverse(
       'article_details', kwargs={'key': '1221'}
   )
   response = client.get(url)
   assert response.status_code == 200
   assert len(response.json()) > 0


@pytest.fixture
def create_user(db, django_user_model, test_password):
   def make_user(**kwargs):
       kwargs['password'] = test_password
       if 'username' not in kwargs:
           kwargs['username'] = str(uuid.uuid4())
       return django_user_model.objects.create_user(**kwargs)
   return make_user


@pytest.mark.django_db
def test_user_detail(client, create_user):
   user = create_user(username='someone')
   url = reverse('user-detail-view', kwargs={'pk': user.pk})
   response = client.get(url)
   assert response.status_code == 200
   assert 'someone' in user.username
   assert user is not None


@pytest.mark.django_db
def test_auth_view(client, create_user, test_password):
   user = create_user()
   url = reverse('auth-url')
   client.login(
       username=user.username,
       password=test_password
   )
   response = client.get(url)
   assert response.status_code == 200


@pytest.mark.django_db
def test_lista_de_artigos_vazia(client):
    url = reverse('articles')
    retorno = client.get(url)
    assert retorno.json() == []


def test_preencher_base_com_dados(db):
    assert retorno.json() == []


@pytest.mark.django_db
def test_generate_token(client, create_user):
    user = create_user()
    url = reverse('token_obtain_pair')
    payload = {'username': user.username, 'password': user.password}
    assert user is None
    # assert payload['username'] == 'Anta'
    # token = client.post(
    #     url,
    #     data=payload,
    #     format='json',
    # )
    # print(token.data)
    # assert token == []


def test_columns_exists(resp):
    columns = ['id', 'title', 'url', 'imageUrl', 'newsSite', 'summary', 'publishedAt',
               'updatedAt', 'featured', 'launches', 'events']
    for info in json.loads(resp.text):
        line = info
        for index, key in enumerate(line):
            assert key == columns[index]
