#!/usr/bin/env python

import kladama as kl


def get_sandbox_session():
    env = kl.Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'

    return kl.authenticate(env, api_token)


def test_areas_of_interest():
    session = get_sandbox_session()
    aois = kl.catalog(session).areas_of_interest

    print('Areas of Interest ========================')
    for aoi in aois:
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_areas_of_interest_for_dev():
    session = get_sandbox_session()
    aois = kl.catalog(session).areas_of_interest_for_user('dev')

    print('Areas of Interest for dev ========================')
    for aoi in aois:
        print(aoi.name, '-', aoi.description, 'in', aoi.link)

    print('\n')


def test_variables():
    session = get_sandbox_session()
    variables = kl.catalog(session).vars

    print('Variables ========================')
    for var in variables:
        print(var.name, 'from', var.source.name, 'in', var.link)

    print('\n')


def test_sources():
    session = get_sandbox_session()
    sources = kl.catalog(session).src

    print('Sources ========================')
    for source in sources:
        print(source.name, ':', source.description, 'in', source.link)

    print('\n')


def test_phenoms():
    session = get_sandbox_session()
    phenoms = kl.catalog(session).phenom

    print('Phenoms ========================')
    for phenom in phenoms:
        print(phenom.name, ':', phenom.description, 'in', phenom.link)

    print('\n')


def test_organizations():
    session = get_sandbox_session()
    organizations = kl.catalog(session).organizations

    print('Organizations ========================')
    for organization in organizations:
        print(organization.name, ':', organization.acronym, 'in', organization.link)

    print('\n')


def test_users():
    session = get_sandbox_session()
    users = kl.catalog(session).users

    print('Users ========================')
    for user in users:
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
