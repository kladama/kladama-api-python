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


def test_areas_of_interest_for_dev():
    print('Testing Areas of Interest for dev ========================')

    session = get_sandbox_session()
    aois = kl.catalog(session).areas_of_interest_for_user('dev')
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


def test_phenoms():
    print('Testing Phenoms ========================')

    session = get_sandbox_session()
    phenoms = kl.catalog(session).phenom
    assert len(phenoms) > 0
    for phenom in phenoms:
        assert isinstance(phenom, kl.Phenomenon)
        print(phenom.name, ':', phenom.description, 'in', phenom.link)

    print('\n')


def test_organizations():
    print('Testing Organizations ========================')

    session = get_sandbox_session()
    organizations = kl.catalog(session).organizations
    assert len(organizations) > 0
    for organization in organizations:
        assert isinstance(organization, kl.Organization)
        print(
            organization.name, ':', organization.acronym,
            'in', organization.link
        )

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


if __name__ == '__main__':
    test_areas_of_interest()
    test_areas_of_interest_for_dev()
    test_variables()
    test_sources()
    test_phenoms()
    test_users()
    test_organizations()
