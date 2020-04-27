#!/usr/bin/env python

import kladama as kl
import kladama_queries as klq
import kladama_entities as kle


def get_sandbox_session():
    env = kl.Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'

    return kl.authenticate(env, api_token)


def test_areas_of_interest():
    print('Testing Areas of Interest ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().aoi

    # when
    aois = kl.QueryExecutor(session).all(query)

    # then
    assert len(aois) > 0
    for aoi in aois:
        assert isinstance(aoi, kle.AreaOfInterest)
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_get_areas_of_interest_by_user_dev():
    print('Testing Areas of Interest for user dev ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().aoi.by_user('dev')

    # when
    aois = kl.QueryExecutor(session).all(query)

    # then
    assert len(aois) > 0
    for aoi in aois:
        assert isinstance(aoi, kle.AreaOfInterest)
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_variables():
    print('Testing Variables ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().var

    # when
    variables = kl.QueryExecutor(session).all(query)

    # then
    assert len(variables) > 0
    for var in variables:
        assert isinstance(var, kle.Variable)
        print(var.name, 'from', var.source.name, 'in', var.link)

    print('\n')


def test_sources():
    print('Testing Sources ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().src

    # when
    sources = kl.QueryExecutor(session).all(query)

    # then
    assert len(sources) > 0
    for source in sources:
        assert isinstance(source, kle.Source)
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
    session = get_sandbox_session()
    executor = kl.QueryExecutor(session)

    for source_name in source_names:
        print('Testing Source by name: ', source_name, ' ========================')

        # given
        query = klq.Query().src.by_name(source_name)

        # when
        source = executor.first(query)

        # then
        assert isinstance(source, kle.Source)
        assert source.name == source_name
        print(source_name, ':', source.description, 'in', source.link)
        print('\n')


def test_phenomenas():
    print('Testing Phenoms ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().phenom

    # when
    phenoms = kl.QueryExecutor(session).all(query)

    # then
    assert len(phenoms) > 0
    for phenom in phenoms:
        assert isinstance(phenom, kle.Phenomena)
        print(phenom.name, ':', phenom.description, 'in', phenom.link)

    print('\n')


def test_phenoms_by_not_existing_name():
    print('Testing Phenom by not existing name ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().phenom.by_name('FAKE NAME')

    # when
    phenom = kl.QueryExecutor(session).first(query)

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
    session = get_sandbox_session()
    executor = kl.QueryExecutor(session)

    for phenom_name in phenom_names:
        print('Testing Phenom by name: ', phenom_name, ' ========================')

        # given
        query = klq.Query().phenom.by_name(phenom_name)

        # when
        phenom = executor.first(query)

        # then
        assert isinstance(phenom, kle.Phenomena)
        assert phenom.name == phenom_name
        print(phenom_name, ':', phenom.description, 'in', phenom.link)
        print('\n')


def test_get_phenomena_from_esa_and_cpc():
    print('Testing Phenom from ESA and NOAA-CPC ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().phenom.by_sources('ESA', 'NOAA-CPC')

    # when
    phenomenas = kl.QueryExecutor(session).all(query)

    # then
    assert len(phenomenas) > 0
    for phenomena in phenomenas:
        assert isinstance(phenomena, kle.Phenomena)
        print(phenomena.name, ':', phenomena.description, 'in', phenomena.link)
        print('\n')


def test_organizations():
    print('Testing Organizations ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().org

    # when
    organizations = kl.QueryExecutor(session).all(query)

    # then
    assert len(organizations) > 0
    for organization in organizations:
        assert isinstance(organization, kle.Organization)
        print(organization.name, ':', organization.acronym, 'in', organization.link)

    print('\n')


def test_users():
    print('Testing Users ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().user

    # when
    users = kl.QueryExecutor(session).all(query)

    # then
    assert len(users) > 0
    for user in users:
        assert isinstance(user, kle.User)
        print(user.username, 'from', user.organization.name, 'in', user.link)

    print('\n')


def test_subscriptions():
    print('Testing Subscriptions ========================')

    # given
    session = get_sandbox_session()
    query = klq.Query().subsc

    # when
    subscriptions = kl.QueryExecutor(session).all(query)

    # then
    assert len(subscriptions) > 0
    for subscription in subscriptions:
        assert isinstance(subscription, kle.Subscription)
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
