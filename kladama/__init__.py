import json
import requests
import re
from kladama.queries import BinaryDataQuery
from kladama.queries import SimpleResultsQuery
from kladama.entities import BinaryData


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


class Context:

    def __init__(self, session):
        self._session = session

    @property
    def env(self):
        return self.session.env

    @property
    def session(self):
        return self._session

    def get(self, query):
        if isinstance(query, BinaryDataQuery):
            return self._get_binary_data(query)

        if isinstance(query, SimpleResultsQuery):
            return self._get_first_entity(query)

        return self._get_entities(query)

    # private methods

    @staticmethod
    def _is_successfully_response(response):
        return 200 <= response.status_code < 300

    def _web_get(self, url):
        api_token = self.session.api_token
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(api_token)
        }

        return requests.get(url, headers)

    def _web_get_json(self, api_url):
        response = self._web_get(api_url)
        if self._is_successfully_response(response):
            return json.loads(response.content.decode('utf-8'))

        return None

    def _get_resource(self, query):
        url = self.env.get_url_from(query.url_path)
        json_obj = query.entity_meta.json_obj
        response = self._web_get_json(url)
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

    def _get_binary_data(self, query: BinaryDataQuery):

        url = self.env.get_url_from(query.url_path)
        response = self._web_get(url)
        if self._is_successfully_response(response):
            filename_match = re.match('.* filename=(.*)', response.headers['Content-disposition'], re.M|re.I)
            return BinaryData({
                'name': filename_match.group(1),
                'content': response.content
            })

        return None
