import unittest
from kladama import *
from kladama.entities import *
from kladama.queries import Query


class IntegrationTest(unittest.TestCase):

    @staticmethod
    def _get_sandbox_session():
        env = Environments().sandbox
        api_token = 'ANYTHING_WORKS_NOW'
        return authenticate(env, api_token)

    @staticmethod
    def test_areas_of_interest():
        print('Testing Areas of Interest ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().aoi

        # when
        aois = Context(session).get(query)

        # then
        assert len(aois) > 0
        for aoi in aois:
            assert isinstance(aoi, AreaOfInterest)
            print(aoi.name, '-', aoi.description, 'in', aoi.link)

        print('\n')

    @staticmethod
    def test_get_areas_of_interest_by_user_dev():
        print('Testing Areas of Interest for user dev ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().aoi.by_user('dev')

        # when
        aois = Context(session).get(query)

        # then
        assert len(aois) > 0
        for aoi in aois:
            assert isinstance(aoi, AreaOfInterest)
            print(aoi.name, '-', aoi.description, 'in', aoi.link)

        print('\n')

    @staticmethod
    def test_variables():
        print('Testing Variables ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().var

        # when
        variables = Context(session).get(query)

        # then
        assert len(variables) > 0
        for var in variables:
            assert isinstance(var, Variable)
            print(var.name, 'from', var.source.name, 'in', var.link)

        print('\n')

    @staticmethod
    def test_sources():
        print('Testing Sources ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().src

        # when
        sources = Context(session).get(query)

        # then
        assert len(sources) > 0
        for source in sources:
            assert isinstance(source, Source)
            print(source.name, ':', source.description, 'in', source.link)

        print('\n')

    @staticmethod
    def test_get_source_by_name():

        # given
        source_names = [
            'ECMWF',
            'NOAA-NWS',
            'NOAA-CPC',
            'NOAA-STAR',
            'ESA',
        ]
        session = IntegrationTest._get_sandbox_session()
        ctx = Context(session)

        for source_name in source_names:
            print('Testing Source by name: ', source_name, ' ========================')

            # given
            query = Query().src.by_name(source_name)

            # when
            source = ctx.get(query)

            # then
            assert isinstance(source, Source)
            assert source.name == source_name
            print(source_name, ':', source.description, 'in', source.link)
            print('\n')

    @staticmethod
    def test_phenomenas():
        print('Testing Phenoms ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().phenom

        # when
        phenoms = Context(session).get(query)

        # then
        assert len(phenoms) > 0
        for phenom in phenoms:
            assert isinstance(phenom, Phenomena)
            print(phenom.name, ':', phenom.description, 'in', phenom.link)

        print('\n')

    @staticmethod
    def test_phenoms_by_not_existing_name():
        print('Testing Phenom by not existing name ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().phenom.by_name('FAKE NAME')

        # when
        phenom = Context(session).get(query)

        # then
        assert isinstance(phenom, Error)
        assert phenom.code == 404
        print('Expected error message: {0}'.format(phenom.message))

    @staticmethod
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
        session = IntegrationTest._get_sandbox_session()
        ctx = Context(session)

        for phenom_name in phenom_names:
            print('Testing Phenom by name: ', phenom_name, ' ========================')

            # given
            query = Query().phenom.by_name(phenom_name)

            # when
            phenom = ctx.get(query)

            # then
            assert isinstance(phenom, Phenomena)
            assert phenom.name == phenom_name
            print(phenom_name, ':', phenom.description, 'in', phenom.link)
            print('\n')

    @staticmethod
    def test_get_phenomena_from_esa_and_cpc():
        print('Testing Phenom from ESA and NOAA-CPC ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().phenom.by_sources('ESA', 'NOAA-CPC')

        # when
        phenomenas = Context(session).get(query)

        # then
        assert len(phenomenas) > 0
        for phenomena in phenomenas:
            assert isinstance(phenomena, Phenomena)
            print(phenomena.name, ':', phenomena.description, 'in', phenomena.link)
            print('\n')

    @staticmethod
    def test_organizations():
        print('Testing Organizations ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().org

        # when
        organizations = Context(session).get(query)

        # then
        assert len(organizations) > 0
        for organization in organizations:
            assert isinstance(organization, Organization)
            print(organization.name, ':', organization.acronym, 'in', organization.link)

        print('\n')

    @staticmethod
    def test_users():
        print('Testing Users ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().user

        # when
        users = Context(session).get(query)

        # then
        assert len(users) > 0
        for user in users:
            assert isinstance(user, User)
            print(user.username, 'from', user.organization.name, 'in', user.link)

        print('\n')

    @staticmethod
    def test_subscriptions():
        print('Testing Subscriptions ========================')

        # given
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc

        # when
        subscriptions = Context(session).get(query)

        # then
        assert len(subscriptions) > 0
        for subscription in subscriptions:
            assert isinstance(subscription, Subscription)
            print(subscription.code, 'from', subscription.owner, 'in', subscription.link)

        print('\n')

    @staticmethod
    def test_around():
        # given
        user = 'ensoag'
        subscription = '3JSM4MN89SJFLE7VR6KPCM0BVPXTWT'
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).around(5, '20200105', '20200115')

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert len(entity.content) > 0

    @staticmethod
    def test_last():
        # given
        user = 'ensoag'
        subscription = '3JSM4MN89SJFLE7VR6KPCM0BVPXTWT'
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).last

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert len(entity.content) > 0

    @staticmethod
    def test_last_n():
        # given
        user = 'ensoag'
        subscription = '3JSM4MN89SJFLE7VR6KPCM0BVPXTWT'
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).last_n(5)

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert len(entity.content) > 0

    @staticmethod
    def test_last_years():
        # given
        user = 'ensoag'
        subscription = '3JSM4MN89SJFLE7VR6KPCM0BVPXTWT'
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).last_years(5, '20200105', '20200115')

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert len(entity.content) > 0

    @staticmethod
    def test_dates():
        # given
        user = 'ensoag'
        subscription = '3JSM4MN89SJFLE7VR6KPCM0BVPXTWT'
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).dates('20200105', '20200115')

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert len(entity.content) > 0

    @staticmethod
    def test_period():
        # given
        user = 'ensoag'
        subscription = '3JSM4MN89SJFLE7VR6KPCM0BVPXTWT'
        from_ = '20200101'
        to = '20200301'
        session = IntegrationTest._get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).period(from_, to)

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert '{0}_TO_{1}'.format(from_, to) in entity.name
        assert len(entity.content) > 0


if __name__ == '__main__':
    unittest.main()
