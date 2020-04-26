#!/usr/bin/env python

import json
import requests


class Environment:

    def __init__(self, api_url_base):
        self._api_url_base = api_url_base

    @property
    def aoi_url(self):
        return self._get_url('aoi')

    @property
    def var_url(self):
        return self._get_url('var')

    @property
    def src_url(self):
        return self._get_url('src')

    @property
    def phenom_url(self):
        return self._get_url('phenom')

    @property
    def org_url(self):
        return self._get_url('org')

    @property
    def user_url(self):
        return self._get_url('user')

    @property
    def subscription_url(self):
        return self._get_url('subsc')

    def aoi_url_for_user(self, user):
        return "{0}/user/{1}".format(self.aoi_url, user)

    def _get_url(self, path):
        return '{0}/{1}'.format(self._api_url_base, path)


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

    @property
    def name(self):
        return self._name


class Describable(Identifiable):

    def __init__(self, obj):
        Identifiable.__init__(self, obj)
        self._description = obj['description']

    @property
    def description(self):
        return self._description


class Linkable:

    def __init__(self, obj):
        links = obj['_links']
        self_link = links['self']
        self._link = self_link['href']
        all_links = {}
        for key in list(links.keys()):
            link = links[key]
            all_links[key] = link['href']

        self._all_links = all_links

    @property
    def link(self):
        return self._link

    @property
    def all_links(self):
        return self._all_links


class AreaOfInterest(Describable, Linkable):

    def __init__(self, obj):
        Describable.__init__(self, obj)
        Linkable.__init__(self, obj)


class Phenomenon(Describable, Linkable):

    def __init__(self, obj):
        Describable.__init__(self, obj)
        Linkable.__init__(self, obj)


class Source(Describable, Linkable):

    def __init__(self, obj):
        Describable.__init__(self, obj)
        Linkable.__init__(self, obj)


class Variable(Describable, Linkable):

    def __init__(self, obj):
        Describable.__init__(self, obj)
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


class Organization(Identifiable, Linkable):

    def __init__(self, obj):
        Identifiable.__init__(self, obj)
        Linkable.__init__(self, obj)
        self._acronym = obj['acronym']
        self._juridic_id = obj['juridicId']
        self._address = obj['address']
        self._actual_credits = obj['actualCredits']
        self._migrated_credits = obj['migratedCredits']

    @property
    def acronym(self):
        return self._acronym

    @property
    def juridic_id(self):
        return self._juridic_id

    @property
    def address(self):
        return self._address

    @property
    def actual_credits(self):
        return self._actual_credits

    @property
    def migrated_credits(self):
        return self._migrated_credits


class User(Identifiable, Linkable):

    def __init__(self, obj):
        Identifiable.__init__(self, obj)
        Linkable.__init__(self, obj)
        self._username = obj['login']
        self._organization = Organization(obj['organization'])

    @property
    def username(self):
        return self._username

    @property
    def organization(self):
        return self._organization


class Subscription(Linkable):

    def __init__(self, obj):
        Linkable.__init__(self, obj)
        self._code = obj['code']
        self._owner = obj['owner']
        self._type = obj['type']
        self._created_timestamp = obj['createdTimestamp']
        self._spatial_operation = obj['spatialOperation']
        self._status = obj['status']
        self._schedule = obj['schedule']
        self._aoi = obj['aoi']
        self._variable = Variable(obj['variable'])

    @property
    def code(self):
        return self._code

    @property
    def owner(self):
        return self._owner

    @property
    def type(self):
        return self._type

    @property
    def created_timestamp(self):
        return self._created_timestamp

    @property
    def spatial_operation(self):
        return self._spatial_operation

    @property
    def status(self):
        return self._status

    @property
    def schedule(self):
        return self._schedule

    @property
    def aoi(self):
        return self._aoi

    @property
    def variable(self):
        return self._variable


class Catalog:

    _aoi_entity_name = 'Areas of Interest'
    _phenomena_entity_name = 'phenomena'
    _org_entity_name = 'organizations'
    _src_entity_name = 'sources'
    _users_entity_name = 'users'
    _var_entity_name = 'variables'
    _subscriptions_entity_name = 'subscriptions'

    def __init__(self, session):
        self._session = session

    @property
    def areas_of_interest(self):
        return self._get_entities(self._session.env.aoi_url, Catalog._aoi_entity_name, AreaOfInterest)

    @property
    def vars(self):
        return self._get_entities(self._session.env.var_url, Catalog._var_entity_name, Variable)

    @property
    def src(self):
        return self._get_entities(self._session.env.src_url, Catalog._src_entity_name, Source)

    @property
    def phenom(self):
        return self._get_entities(self._session.env.phenom_url, Catalog._phenomena_entity_name, Phenomenon)

    @property
    def organizations(self):
        return self._get_entities(self._session.env.org_url, Catalog._org_entity_name, Organization)

    @property
    def users(self):
        return self._get_entities(self._session.env.user_url, Catalog._users_entity_name, User)

    @property
    def subscriptions(self):
        return self._get_entities(self._session.env.subscription_url, Catalog._subscriptions_entity_name, Subscription)

    def areas_of_interest_for_user(self, user):
        return self._get_entities(self._session.env.aoi_url_for_user(user), self._aoi_entity_name, AreaOfInterest)

    def _get_entities(self, api_url, entity_name, entity_class):
        obj = self._get_resource(api_url, entity_name)

        entities = []
        if obj is not None:
            for entity in obj:
                entities.append(entity_class(entity))

        return entities

    def _get_resource(self, api_url, resource_name):
        api_token = self._session.api_token
        response = get_from_api(api_token, api_url)
        if response is not None:
            root = response['_embedded']
            return root[resource_name]

        return None


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
