import pytest
import json
# from django.urls import reverse
from requests import get


@pytest.fixture
def resp(client):
    resp = get('https://api.spaceflightnewsapi.net/v3/articles')
    # resp = client.get('https://api.spaceflightnewsapi.net/v3/articles')
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_return_instance_list(resp):
    assert type(json.loads(resp.text)) == list


def test_columns_exists(resp):
    columns = ['id', 'title', 'url', 'imageUrl', 'newsSite', 'summary', 'publishedAt',
               'updatedAt', 'featured', 'launches', 'events']
    for info in json.loads(resp.text):
        line = info
        for index, key in enumerate(line):
            assert key == columns[index]
