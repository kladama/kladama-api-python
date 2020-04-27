import json
import requests


class Environment:

    def __init__(self, api_url_base):
        self._api_url_base = api_url_base

    def get_url_from(self, path):
        return '{0}{1}'.format(self._api_url_base, path)


class Environments:

    @property
    def prod(self):
        return Environment('https://kladama.com')

    @property
    def sandbox(self):
        return Environment('https://kladama.com')


class Session:

    def __init__(self, env, api_token):
        self._env = env
        self._api_token = api_token

    @property
    def env(self):
        return self._env

    @property
    def api_token(self):
        return self._api_token


def authenticate(env, api_token):
    return Session(env, api_token)


class QueryExecutor:

    def __init__(self, session):
        self._session = session

    @property
    def env(self):
        return self.session.env

    @property
    def session(self):
        return self._session

    def all(self, query):
        return self._get_entities(query)

    def first(self, query):
        return self._get_first_entity(query)

    # private methods

    def _request_from_service(self, api_url):
        api_token = self.session.api_token
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token)
        }

        response = requests.get(api_url, headers)
        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))

        return None

    def _get_resource(self, query):
        url = self.env.get_url_from(query.url_path)
        json_obj = query.entity_meta.json_obj
        response = self._request_from_service(url)
        if response is not None:
            root = response['_embedded']
            return root[json_obj]

        return None

    def _get_entities(self, query):
        obj = self._get_resource(query)
        entity_class = query.entity_meta.entity_class

        entities = []
        if obj is not None:
            for entity in obj:
                entities.append(entity_class(entity))

        return entities

    def _get_first_entity(self, query):
        entities = self._get_entities(query)
        if len(entities) > 0:
            return entities[0]

        return None
