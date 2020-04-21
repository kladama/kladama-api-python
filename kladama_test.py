#!/usr/bin/env python

import kladama as kl


def get_sandbox_session():
    env = kl.Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'

    return kl.authenticate(env, api_token)


def test_variables():
    session = get_sandbox_session()
    variables = kl.catalog(session).vars

    for var in variables:
        print(var.name, 'from', var.source.name, 'in', var.link)


if __name__ == '__main__':
    test_variables()