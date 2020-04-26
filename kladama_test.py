#!/usr/bin/env python

import kladama as kl


def get_sandbox_session():
    env = kl.Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'

    return kl.authenticate(env, api_token)


def test_areas_of_interest():
    print('Testing Areas of Interest ========================')

    session = get_sandbox_session()
    aois = kl.catalog(session).areas_of_interest
    assert len(aois) > 0
    for aoi in aois:
        assert isinstance(aoi, kl.AreaOfInterest)
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_get_areas_of_interest_by_user_dev():
    print('Testing Areas of Interest for user dev ========================')

    session = get_sandbox_session()
    aois = kl.catalog(session).get_areas_of_interest_by_user('dev')
    assert len(aois) > 0
    for aoi in aois:
        assert isinstance(aoi, kl.AreaOfInterest)
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_variables():
    print('Testing Variables ========================')

    session = get_sandbox_session()
    variables = kl.catalog(session).vars
    assert len(variables) > 0
    for var in variables:
        assert isinstance(var, kl.Variable)
        print(var.name, 'from', var.source.name, 'in', var.link)

    print('\n')


def test_sources():
    print('Testing Sources ========================')

    session = get_sandbox_session()
    sources = kl.catalog(session).src
    assert len(sources) > 0
    for source in sources:
        assert isinstance(source, kl.Source)
        print(source.name, ':', source.description, 'in', source.link)

    print('\n')


def test_phenomenas():
    print('Testing Phenoms ========================')

    session = get_sandbox_session()
    phenoms = kl.catalog(session).phenomenas
    assert len(phenoms) > 0
    for phenom in phenoms:
        assert isinstance(phenom, kl.Phenomenon)
        print(phenom.name, ':', phenom.description, 'in', phenom.link)

    print('\n')


def test_phenoms_by_not_existing_name():
    print('Testing Phenom by not existing name ========================')

    session = get_sandbox_session()
    catalog = kl.catalog(session)
    phenom = catalog.get_phenomena_by_name('FAKE NAME')
    assert phenom is None


def test_get_phenomena_by_name():
    session = get_sandbox_session()
    catalog = kl.catalog(session)

    phenom_names = [
        'rain',
        'temperature',
        'soil moisture',
        'vegetation',
        'color',
        'solar radiation',
        'evaporation',
    ]

    assert len(phenom_names) > 0
    for phenom_name in phenom_names:
        print('Testing Phenom by name: ', phenom_name, ' ========================')
        phenom = catalog.get_phenomena_by_name(phenom_name)

        assert isinstance(phenom, kl.Phenomenon)
        print(phenom_name, ':', phenom.description, 'in', phenom.link)
        print('\n')


def test_organizations():
    print('Testing Organizations ========================')

    session = get_sandbox_session()
    organizations = kl.catalog(session).organizations
    assert len(organizations) > 0
    for organization in organizations:
        assert isinstance(organization, kl.Organization)
        print(organization.name, ':', organization.acronym, 'in', organization.link)

    print('\n')


def test_users():
    print('Testing Users ========================')

    session = get_sandbox_session()
    users = kl.catalog(session).users
    assert len(users) > 0
    for user in users:
        assert isinstance(user, kl.User)
        print(user.username, 'from', user.organization.name, 'in', user.link)

    print('\n')


def test_subscriptions():
    print('Testing Subscriptions ========================')

    session = get_sandbox_session()
    subscriptions = kl.catalog(session).subscriptions
    assert len(subscriptions) > 0
    for subscription in subscriptions:
        assert isinstance(subscription, kl.Subscription)
        print(subscription.code, 'from', subscription.owner, 'in', subscription.link)

    print('\n')


if __name__ == '__main__':
    test_areas_of_interest()
    test_get_areas_of_interest_by_user_dev()
    test_variables()
    test_sources()
    test_phenomenas()
    test_get_phenomena_by_name()
    test_subscriptions()
    test_users()
    test_organizations()
