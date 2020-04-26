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
    def phenomena_url(self):
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

    @staticmethod
    def get_resource_by_phenomena_url(resource_url, phenomena):
        return "{0}/phenom/{1}".format(resource_url, phenomena)

    @staticmethod
    def get_resource_by_name_url(resource_url, name):
        return "{0}/{1}".format(resource_url, name)

    @staticmethod
    def get_resource_by_user_url(resource_url, user):
        return "{0}/user/{1}".format(resource_url, user)

    @staticmethod
    def get_resource_by_sources_url(resource_url, sources):
        return "{0}/src/{1}".format(resource_url, ','.join(sources))

    @staticmethod
    def get_observed_resource_url(resource_url):
        return "{0}/{1}".format(resource_url, 'observed')

    @staticmethod
    def get_resource_forecast_url(resource_url):
        return "{0}/{1}".format(resource_url, 'forecast')

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


class Forecast:

    def __init__(self, _obj):
        pass


class Catalog:

    def __init__(self, session):
        self._session = session

    # areas of interest

    @property
    def areas_of_interest(self):
        env = self._session.env
        url = env.aoi_url
        return self._get_entities(url, Catalog._aoi_entity_name, AreaOfInterest)

    def areas_of_interest_by_user(self, user):
        env = self._session.env
        url = Environment.get_resource_by_user_url(env.aoi_url, user)
        return self._get_entities(url, self._aoi_entity_name, AreaOfInterest)

    # variables

    @property
    def variables(self):
        env = self._session.env
        url = env.var_url
        return self._get_entities(url, Catalog._var_entity_name, Variable)

    @property
    def variables_forecast(self):
        env = self._session.env
        url = Environment.get_resource_forecast_url(env.var_url)
        return self._get_entities(url, Catalog._forecast_entity_name, Forecast)

    def variable_by_name(self, name):
        env = self._session.env
        url = Environment.get_resource_by_name_url(env.var_url, name)
        return self._get_first_entity(url, self._var_entity_name, Variable)

    def variables_by_phenomena(self, phenomena):
        env = self._session.env
        url = Environment.get_resource_by_phenomena_url(env.var_url, phenomena)
        return self._get_entities(url, self._var_entity_name, Variable)

    def variables_by_phenomena_forecast(self, phenomena):
        env = self._session.env
        resource_url = Environment.get_resource_by_phenomena_url(env.var_url, phenomena)
        url = Environment.get_resource_forecast_url(resource_url)
        return self._get_entities(url, self._var_entity_name, Variable)

    def variables_by_sources(self, sources):
        env = self._session.env
        url = Environment.get_resource_by_sources_url(env.var_url, sources)
        return self._get_entities(url, self._var_entity_name, Variable)

    def variables_by_sources_forecast(self, sources):
        env = self._session.env
        resource_url = Environment.get_resource_by_sources_url(env.var_url, sources)
        url = Environment.get_resource_forecast_url(resource_url)
        return self._get_entities(url, self._var_entity_name, Variable)

    @property
    def observed_variables(self):
        env = self._session.env
        url = Environment.get_observed_resource_url(env.var_url)
        return self._get_entities(url, Catalog._var_entity_name, Variable)

    def observed_variables_by_name(self, name):
        env = self._session.env
        resource_url = Environment.get_resource_by_name_url(env.var_url, name)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._var_entity_name, Variable)

    def observed_variables_by_phenomena(self, phenomena):
        env = self._session.env
        resource_url = Environment.get_resource_by_phenomena_url(env.var_url, phenomena)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._var_entity_name, Variable)

    def observed_variables_by_sources(self, sources):
        env = self._session.env
        resource_url = Environment.get_resource_by_sources_url(env.var_url, sources)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._var_entity_name, Variable)

    # sources

    @property
    def sources(self):
        env = self._session.env
        url = env.src_url
        return self._get_entities(url, Catalog._src_entity_name, Source)

    @property
    def sources_forecast(self):
        env = self._session.env
        url = Environment.get_resource_forecast_url(env.src_url)
        return self._get_entities(url, Catalog._forecast_entity_name, Forecast)

    def source_by_name(self, name):
        env = self._session.env
        url = Environment.get_resource_by_name_url(env.src_url, name)
        return self._get_first_entity(url, self._src_entity_name, Source)

    def sources_by_phenomena(self, phenomena):
        env = self._session.env
        url = Environment.get_resource_by_phenomena_url(env.src_url, phenomena)
        return self._get_entities(url, self._src_entity_name, Source)

    def sources_by_phenomena_forecast(self, phenomena):
        env = self._session.env
        resource_url = Environment.get_resource_by_phenomena_url(env.src_url, phenomena)
        url = Environment.get_resource_forecast_url(resource_url)
        return self._get_entities(url, self._src_entity_name, Source)

    @property
    def observed_sources(self):
        env = self._session.env
        url = Environment.get_observed_resource_url(env.src_url)
        return self._get_entities(url, Catalog._src_entity_name, Source)

    def observed_sources_by_name(self, name):
        env = self._session.env
        resource_url = Environment.get_resource_by_name_url(env.src_url, name)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._src_entity_name, Source)

    def observed_sources_by_phenomena(self, phenomena):
        env = self._session.env
        resource_url = Environment.get_resource_by_phenomena_url(env.src_url, phenomena)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._src_entity_name, Source)

    # phenomenas

    @property
    def phenomenas(self):
        env = self._session.env
        url = env.phenomena_url
        return self._get_entities(url, Catalog._phenomena_entity_name, Phenomenon)

    @property
    def phenomenas_forecast(self):
        env = self._session.env
        url = Environment.get_resource_forecast_url(env.phenomena_url)
        return self._get_entities(url, Catalog._forecast_entity_name, Forecast)

    def phenomena_by_name(self, name):
        env = self._session.env
        url = Environment.get_resource_by_name_url(env.phenomena_url, name)
        return self._get_first_entity(url, self._phenomena_entity_name, Phenomenon)

    def phenomenas_by_sources(self, sources):
        env = self._session.env
        url = Environment.get_resource_by_sources_url(env.phenomena_url, sources)
        return self._get_entities(url, self._phenomena_entity_name, Phenomenon)

    def phenomenas_by_sources_forecast(self, sources):
        env = self._session.env
        resource_url = Environment.get_resource_by_sources_url(env.phenomena_url, sources)
        url = Environment.get_resource_forecast_url(resource_url)
        return self._get_entities(url, self._forecast_entity_name, Forecast)

    @property
    def observed_phenomenas(self):
        env = self._session.env
        url = Environment.get_observed_resource_url(env.phenomena_url)
        return self._get_entities(url, Catalog._phenomena_entity_name, Phenomenon)

    def observed_phenomenas_by_name(self, name):
        env = self._session.env
        resource_url = Environment.get_resource_by_name_url(env.phenomena_url, name)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._phenomena_entity_name, Phenomenon)

    def observed_phenomenas_by_sources(self, sources):
        env = self._session.env
        resource_url = Environment.get_resource_by_sources_url(env.phenomena_url, sources)
        url = Environment.get_observed_resource_url(resource_url)
        return self._get_entities(url, self._phenomena_entity_name, Phenomenon)

    # organizations

    @property
    def organizations(self):
        env = self._session.env
        url = env.org_url
        return self._get_entities(url, Catalog._org_entity_name, Organization)

    # users

    @property
    def users(self):
        env = self._session.env
        url = env.user_url
        return self._get_entities(url, Catalog._users_entity_name, User)

    # subscriptions

    @property
    def subscriptions(self):
        env = self._session.env
        url = env.subscription_url
        return self._get_entities(url, Catalog._subscriptions_entity_name, Subscription)

    # private members

    _aoi_entity_name = 'Areas of Interest'
    _phenomena_entity_name = 'phenomena'
    _org_entity_name = 'organizations'
    _src_entity_name = 'sources'
    _users_entity_name = 'users'
    _var_entity_name = 'variables'
    _subscriptions_entity_name = 'subscriptions'
    _forecast_entity_name = 'forecasts'

    def _get_entities(self, api_url, entity_name, entity_class):
        obj = self._get_resource(api_url, entity_name)

        entities = []
        if obj is not None:
            for entity in obj:
                entities.append(entity_class(entity))

        return entities

    def _get_first_entity(self, api_url, entity_name, entity_class):
        entities = self._get_entities(api_url, entity_name, entity_class)
        if len(entities) > 0:
            return entities[0]

        return None

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
