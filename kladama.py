#!/usr/bin/env python

import json
import requests


class Environment:

    def __init__(self, api_url_base):
        self._api_url_base = api_url_base

    @property
    def var_url(self):
        return '{0}/var'.format(self._api_url_base)


class Environments:

    @property
    def prod(self):
        return Environment('http://kladama.com')

    @property
    def sandbox(self):
        return Environment('http://kladama.com')


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


class Identifiable:

    def __init__(self, obj):
        self._name = obj['name']
        self._description = obj['description']

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description


class Linkable:

    def __init__(self, obj):
        links = obj['_links']
        self_link = links['self']
        self._link = self_link['href']

    @property
    def link(self):
        return self._link


class Phenomenon(Identifiable, Linkable):

    def __init__(self, obj):
        Identifiable.__init__(self, obj)
        Linkable.__init__(self, obj)


class Source(Identifiable, Linkable):

    def __init__(self, obj):
        Identifiable.__init__(self, obj)
        Linkable.__init__(self, obj)


class Variable(Identifiable, Linkable):

    def __init__(self, obj):
        Identifiable.__init__(self, obj)
        Linkable.__init__(self, obj)
        self._type = obj['type']
        self._format = obj['format']
        self._spatialResolution = obj['spatialResolution']
        self._temporalResolution = obj['temporalResolution']
        self._phenomenon = Source(obj['phenomenon'])
        self._source = Source(obj['source'])

    @property
    def type(self):
        return self._type

    @property
    def source(self):
        return self._source


class Catalog:

    def __init__(self, session):
        self._session = session

    @property
    def vars(self):
        variables = []

        api_token = self._session.api_token
        api_url = self._session.env.var_url
        response = get_from_api(api_token, api_url)
        variables_obj = self._get_variables(response)
        if variables_obj is not None:
            for var in variables_obj:
                variables.append(Variable(var))

        return variables

    @staticmethod
    def _get_root(response):
        if response is None:
            return None

        return response['_embedded']

    @staticmethod
    def _get_variables(response):
        root = Catalog._get_root(response)
        if root is None:
            return None

        return root['variables']


def authenticate(env, api_token):
    return Session(env, api_token)


def catalog(session):
    return Catalog(session)


def get_from_api(api_token, api_url):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {0}'.format(api_token)
    }

    response = requests.get(api_url, headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))

    return None
