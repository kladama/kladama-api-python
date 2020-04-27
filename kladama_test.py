#!/usr/bin/env python

from kladama import *
from kladama.entities import *
from kladama.queries import Query


# unit tests


def test_url_paths():
    assert Query().aoi.url_path == '/aoi'
    assert Query().aoi.by_name('aoi-name').url_path == '/aoi/aoi-name'
    assert Query().aoi.by_user('user-name').url_path == '/aoi/user/user-name'
    assert Query().aoi.by_user('user-name').filter_by('aoi-name').url_path == '/aoi/user/user-name/aoi-name'

    assert Query().phenom.url_path == '/phenom'
    assert Query().phenom.forecast.url_path == '/phenom/forecast'
    assert Query().phenom.observed.url_path == '/phenom/observed'
    assert Query().phenom.by_name('phenomena-name').url_path == '/phenom/phenomena-name'
    assert Query().phenom.by_sources('source-1').url_path == '/phenom/src/source-1'
    assert Query().phenom.by_sources('source-1', 'source-2').url_path == '/phenom/src/source-1,source-2'
    assert Query().phenom.by_sources('source-1').observed.url_path == '/phenom/src/source-1/observed'
    assert Query().phenom.by_sources('source-1').forecast.url_path == '/phenom/src/source-1/forecast'

    assert Query().org.url_path == '/org'
    assert Query().org.by_name('organization-name').url_path == '/org/organization-name'

    assert Query().src.url_path == '/src'
    assert Query().src.forecast.url_path == '/src/forecast'
    assert Query().src.observed.url_path == '/src/observed'
    assert Query().src.by_name('source-name').url_path == '/src/source-name'
    assert Query().src.by_phenomena('phenomena-name').url_path == '/src/phenom/phenomena-name'
    assert Query().src.by_phenomena('phenomena-name').observed.url_path == '/src/phenom/phenomena-name/observed'
    assert Query().src.by_phenomena('phenomena-name').forecast.url_path == '/src/phenom/phenomena-name/forecast'

    assert Query().subsc.url_path == '/subsc'
    assert Query().subsc.by_name('subscription-name').url_path == '/subsc/subscription-name'
    assert Query().subsc.by_user('user-name').url_path == '/subsc/user/user-name'
    assert Query().subsc.by_user('user-name').filter_by('subscription-name')\
               .url_path == '/subsc/user/user-name/subscription-name'

    assert Query().var.url_path == '/var'
    assert Query().var.forecast.url_path == '/var/forecast'
    assert Query().var.observed.url_path == '/var/observed'
    assert Query().var.by_name('var-name').url_path == '/var/var-name'
    assert Query().var.by_phenomena('phenomena-name').url_path == '/var/phenom/phenomena-name'
    assert Query().var.by_phenomena('phenomena-name').observed.url_path == '/var/phenom/phenomena-name/observed'
    assert Query().var.by_phenomena('phenomena-name').forecast.url_path == '/var/phenom/phenomena-name/forecast'
    assert Query().var.by_sources('source-1').url_path == '/var/src/source-1'
    assert Query().var.by_sources('source-1', 'source-2').url_path == '/var/src/source-1,source-2'
    assert Query().var.by_sources('source-1').observed.url_path == '/var/src/source-1/observed'
    assert Query().var.by_sources('source-1').forecast.url_path == '/var/src/source-1/forecast'


# integration tests


def _get_sandbox_session():
    env = Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'
    return authenticate(env, api_token)


def test_areas_of_interest():
    print('Testing Areas of Interest ========================')

    # given
    session = _get_sandbox_session()
    query = Query().aoi

    # when
    aois = Context(session).all(query)

    # then
    assert len(aois) > 0
    for aoi in aois:
        assert isinstance(aoi, AreaOfInterest)
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_get_areas_of_interest_by_user_dev():
    print('Testing Areas of Interest for user dev ========================')

    # given
    session = _get_sandbox_session()
    query = Query().aoi.by_user('dev')

    # when
    aois = Context(session).all(query)

    # then
    assert len(aois) > 0
    for aoi in aois:
        assert isinstance(aoi, AreaOfInterest)
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_variables():
    print('Testing Variables ========================')

    # given
    session = _get_sandbox_session()
    query = Query().var

    # when
    variables = Context(session).all(query)

    # then
    assert len(variables) > 0
    for var in variables:
        assert isinstance(var, Variable)
        print(var.name, 'from', var.source.name, 'in', var.link)

    print('\n')


def test_sources():
    print('Testing Sources ========================')

    # given
    session = _get_sandbox_session()
    query = Query().src

    # when
    sources = Context(session).all(query)

    # then
    assert len(sources) > 0
    for source in sources:
        assert isinstance(source, Source)
        print(source.name, ':', source.description, 'in', source.link)

    print('\n')


def test_get_source_by_name():

    # given
    source_names = [
        'ECMWF',
        'NOAA-NWS',
        'NOAA-CPC',
        'NOAA-STAR',
        'ESA',
    ]
    session = _get_sandbox_session()
    ctx = Context(session)

    for source_name in source_names:
        print('Testing Source by name: ', source_name, ' ========================')

        # given
        query = Query().src.by_name(source_name)

        # when
        source = ctx.first(query)

        # then
        assert isinstance(source, Source)
        assert source.name == source_name
        print(source_name, ':', source.description, 'in', source.link)
        print('\n')


def test_phenomenas():
    print('Testing Phenoms ========================')

    # given
    session = _get_sandbox_session()
    query = Query().phenom

    # when
    phenoms = Context(session).all(query)

    # then
    assert len(phenoms) > 0
    for phenom in phenoms:
        assert isinstance(phenom, Phenomena)
        print(phenom.name, ':', phenom.description, 'in', phenom.link)

    print('\n')


def test_phenoms_by_not_existing_name():
    print('Testing Phenom by not existing name ========================')

    # given
    session = _get_sandbox_session()
    query = Query().phenom.by_name('FAKE NAME')

    # when
    phenom = Context(session).first(query)

    # then
    assert phenom is None


def test_get_phenomena_by_name():

    # given
    phenom_names = [
        'rain',
        'temperature',
        'soil moisture',
        'vegetation',
        'color',
        'solar radiation',
        'evaporation',
    ]
    session = _get_sandbox_session()
    ctx = Context(session)

    for phenom_name in phenom_names:
        print('Testing Phenom by name: ', phenom_name, ' ========================')

        # given
        query = Query().phenom.by_name(phenom_name)

        # when
        phenom = ctx.first(query)

        # then
        assert isinstance(phenom, Phenomena)
        assert phenom.name == phenom_name
        print(phenom_name, ':', phenom.description, 'in', phenom.link)
        print('\n')


def test_get_phenomena_from_esa_and_cpc():
    print('Testing Phenom from ESA and NOAA-CPC ========================')

    # given
    session = _get_sandbox_session()
    query = Query().phenom.by_sources('ESA', 'NOAA-CPC')

    # when
    phenomenas = Context(session).all(query)

    # then
    assert len(phenomenas) > 0
    for phenomena in phenomenas:
        assert isinstance(phenomena, Phenomena)
        print(phenomena.name, ':', phenomena.description, 'in', phenomena.link)
        print('\n')


def test_organizations():
    print('Testing Organizations ========================')

    # given
    session = _get_sandbox_session()
    query = Query().org

    # when
    organizations = Context(session).all(query)

    # then
    assert len(organizations) > 0
    for organization in organizations:
        assert isinstance(organization, Organization)
        print(organization.name, ':', organization.acronym, 'in', organization.link)

    print('\n')


def test_users():
    print('Testing Users ========================')

    # given
    session = _get_sandbox_session()
    query = Query().user

    # when
    users = Context(session).all(query)

    # then
    assert len(users) > 0
    for user in users:
        assert isinstance(user, User)
        print(user.username, 'from', user.organization.name, 'in', user.link)

    print('\n')


def test_subscriptions():
    print('Testing Subscriptions ========================')

    # given
    session = _get_sandbox_session()
    query = Query().subsc

    # when
    subscriptions = Context(session).all(query)

    # then
    assert len(subscriptions) > 0
    for subscription in subscriptions:
        assert isinstance(subscription, Subscription)
        print(subscription.code, 'from', subscription.owner, 'in', subscription.link)

    print('\n')


if __name__ == '__main__':
    test_areas_of_interest()
    test_variables()
    test_sources()
    test_phenomenas()
    test_subscriptions()
    test_users()
    test_organizations()
