#!/usr/bin/env python

import kladama as kl


def test_variables():
    env = kl.Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'
    session = kl.authenticate(env, api_token)

    catalog = kl.catalog(session)
    variables = catalog.vars

    for var in variables:
        print(var.name, 'from', var.source.name, 'in', var.link)


if __name__ == '__main__':
    test_variables()