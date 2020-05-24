import datetime
import unittest
from kladama import *


def _get_sandbox_session():
    env = Environments().sandbox
    api_token = 'ANYTHING_WORKS_NOW'
    return authenticate(env, api_token)


class OperationIntegrationTest(unittest.TestCase):
    user = 'dev'

    @classmethod
    def setUpClass(cls) -> None:
        now_timestamp = datetime.datetime.now().timestamp()
        cls.aoi_id = 'test_aoi_{0}'.format(now_timestamp)

    def test_create_delete_aoi(self):
        # when
        creation_response = self._create_test_aoi(self.user, self.aoi_id)

        # then
        self.fail_if_error(creation_response)

        # and when
        deletion_response = self._delete_test_aoi(self.user, self.aoi_id)

        # then
        self.fail_if_error(deletion_response)

    def test_create_delete_subscription(self):
        # given
        self._create_test_aoi(self.user, self.aoi_id)

        # when
        creation_response = self._create_test_periodic_subscription(self.user, self.aoi_id)

        # then
        self.fail_if_error(creation_response)

        code = creation_response.result['code']
        assert isinstance(code, str)

        # and when
        deletion_response = self._delete_test_subscription(self.user, code)

        # then
        self.fail_if_error(deletion_response)

        # cleanup
        self._delete_test_aoi(self.user, self.aoi_id)

    # private members

    @staticmethod
    def _get_context():
        session = _get_sandbox_session()
        return Context(session)

    @staticmethod
    def _create_test_aoi(user, aoi_id):
        create_operation = Operations() \
            .add_aoi \
            .for_user(user) \
            .with_aoi_id(aoi_id) \
            .with_description("Test AOI") \
            .with_category("Test") \
            .with_features({
                "type": "FeatureCollection",
                "name": "SAM_Municipalities",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "0",
                            "name": "n.a2",
                            "Country": "Uruguay",
                            "State": "Artigas"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                        -56.97458267255223,
                                        -30.350532532150567
                                    ],
                                    [
                                        -56.933055878126254,
                                        -30.33943557709017
                                    ],
                                    [
                                        -56.891361236931516,
                                        -30.34736061070356
                                    ],
                                    [
                                        -56.879180908172316,
                                        -30.363948821680708
                                    ],
                                    [
                                        -56.760517120568636,
                                        -30.33959579490994
                                    ],
                                    [
                                        -56.688446045348655,
                                        -30.39470672563482
                                    ],
                                    [
                                        -56.65667343183338,
                                        -30.395431518949408
                                    ],
                                    [
                                        -56.64161300623522,
                                        -30.31474876424403
                                    ],
                                    [
                                        -56.61774826007411,
                                        -30.297622680442316
                                    ],
                                    [
                                        -56.6072273252808,
                                        -30.26715278617212
                                    ],
                                    [
                                        -56.63636779763573,
                                        -30.26306152377026
                                    ],
                                    [
                                        -56.62702178932409,
                                        -30.23999786401015
                                    ],
                                    [
                                        -56.66174697874004,
                                        -30.219617843288802
                                    ],
                                    [
                                        -56.643627166560464,
                                        -30.202171325646134
                                    ],
                                    [
                                        -56.69649505590206,
                                        -30.20267677341434
                                    ],
                                    [
                                        -56.70510864284955,
                                        -30.174560547031604
                                    ],
                                    [
                                        -56.77487564059828,
                                        -30.163682937517535
                                    ],
                                    [
                                        -56.78038024874945,
                                        -30.12800979611518
                                    ],
                                    [
                                        -56.802124023005206,
                                        -30.119579315632848
                                    ],
                                    [
                                        -56.80290222166013,
                                        -30.10393142679385
                                    ],
                                    [
                                        -56.87690353427064,
                                        -30.085393905604235
                                    ],
                                    [
                                        -56.901260375965535,
                                        -30.106927871623952
                                    ],
                                    [
                                        -56.91654586769761,
                                        -30.09138870272642
                                    ],
                                    [
                                        -56.978954314789746,
                                        -30.093467712265067
                                    ],
                                    [
                                        -56.99183273329396,
                                        -30.079689025628
                                    ],
                                    [
                                        -57.04071426435178,
                                        -30.0986270904678
                                    ],
                                    [
                                        -57.06833648683937,
                                        -30.08774375946689
                                    ],
                                    [
                                        -57.08846282949594,
                                        -30.119001388802985
                                    ],
                                    [
                                        -57.10939407347769,
                                        -30.111831665199134
                                    ],
                                    [
                                        -57.109123230053,
                                        -30.139402389808424
                                    ],
                                    [
                                        -57.127094269185136,
                                        -30.143037795757607
                                    ],
                                    [
                                        -57.165214538719965,
                                        -30.1998348240179
                                    ],
                                    [
                                        -57.157833099417985,
                                        -30.23190689109009
                                    ],
                                    [
                                        -57.202816009151434,
                                        -30.277204513177708
                                    ],
                                    [
                                        -57.098823547368795,
                                        -30.27325248741232
                                    ],
                                    [
                                        -57.07741165172632,
                                        -30.32739829989157
                                    ],
                                    [
                                        -56.995590209620445,
                                        -30.32661056482567
                                    ],
                                    [
                                        -56.97458267255223,
                                        -30.350532532150567
                                    ]
                                ]
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "1",
                            "name": "n.a3",
                            "Country": "Uruguay",
                            "State": "Artigas"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                        -57.41722488362143,
                                        -30.29360008217799
                                    ],
                                    [
                                        -57.424922942739556,
                                        -30.272167206251538
                                    ],
                                    [
                                        -57.46327209513106,
                                        -30.26243782054894
                                    ],
                                    [
                                        -57.4992294312932,
                                        -30.279132843106197
                                    ],
                                    [
                                        -57.537673950492376,
                                        -30.27181625391694
                                    ],
                                    [
                                        -57.55657196042762,
                                        -30.254777907974017
                                    ],
                                    [
                                        -57.56108093273883,
                                        -30.20615386990511
                                    ],
                                    [
                                        -57.63419342019017,
                                        -30.1765785213816
                                    ],
                                    [
                                        -57.64294815033685,
                                        -30.202402115065524
                                    ],
                                    [
                                        -57.60689926139173,
                                        -30.24848175073214
                                    ],
                                    [
                                        -57.63539123531723,
                                        -30.338024139702213
                                    ],
                                    [
                                        -57.78306579594971,
                                        -30.43265151945201
                                    ],
                                    [
                                        -57.77141189614207,
                                        -30.429557800352143
                                    ],
                                    [
                                        -57.76450347865256,
                                        -30.45383262657441
                                    ],
                                    [
                                        -57.67060089131803,
                                        -30.450849533079463
                                    ],
                                    [
                                        -57.63094711311874,
                                        -30.501667023014647
                                    ],
                                    [
                                        -57.562702179262146,
                                        -30.5161724086297
                                    ],
                                    [
                                        -57.558231353494136,
                                        -30.455635071201527
                                    ],
                                    [
                                        -57.51711273166717,
                                        -30.374963760369212
                                    ],
                                    [
                                        -57.41722488362143,
                                        -30.29360008217799
                                    ]
                                ]
                            ]
                        }
                    }
                ]
            }
        )

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(create_operation)

    @staticmethod
    def _create_test_periodic_subscription(user, aoi_id):
        create_operation = Operations() \
            .periodic_subsc \
            .for_user(user) \
            .with_variable("D1_2M_MAX_TEMP") \
            .with_source("ECMWF") \
            .with_operation("MEAN") \
            .with_aoi(aoi_id)

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(create_operation)

    @staticmethod
    def _delete_test_aoi(user, aoi_id):
        delete_operation = Operations() \
            .delete_aoi \
            .from_user(user) \
            .with_aoi(aoi_id)

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(delete_operation)

    @staticmethod
    def _delete_test_subscription(user, subsc_id):
        delete_operation = Operations() \
            .unsubscribe \
            .from_user(user) \
            .with_subsc(subsc_id)

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(delete_operation)

    def fail_if_error(self, response):
        self.failIf(isinstance(response, Error), response.__str__())


class QueryIntegrationTest(unittest.TestCase):

    @staticmethod
    def test_areas_of_interest():
        print('Testing Areas of Interest ========================')

        # given
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
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
        session = _get_sandbox_session()
        query = Query().subsc.by_user(user).filter_by(subscription).period(from_, to)

        # when
        entity = Context(session).get(query)

        # then
        assert isinstance(entity, BinaryData)
        assert subscription in entity.name
        assert '{0}_TO_{1}'.format(from_, to) in entity.name
        assert len(entity.content) > 0


class HelperTest(unittest.TestCase):

    @staticmethod
    def test_check_aoi():
        # given
        session = _get_sandbox_session()
        helper = Helpers\
            .check_aoi({
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "5b8c9e286e63b329cf764c61",
                            "name": "Jerovia - D9"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                        -60.675417,
                                        -21.854207
                                    ],
                                    [
                                        -60.675394,
                                        -21.855348
                                    ],
                                    [
                                        -60.669532,
                                        -21.858799
                                    ],
                                    [
                                        -60.656133,
                                        -21.85887
                                    ],
                                    [
                                        -60.656118,
                                        -21.854208
                                    ],
                                    [
                                        -60.675417,
                                        -21.854207
                                    ]
                                ]
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "5b8c9d296e63b329cf764c5f",
                            "name": "Jerovia - D7"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                        -60.663761,
                                        -21.859673
                                    ],
                                    [
                                        -60.663722,
                                        -21.864248
                                    ],
                                    [
                                        -60.65605,
                                        -21.864169
                                    ],
                                    [
                                        -60.656126,
                                        -21.859664
                                    ],
                                    [
                                        -60.663761,
                                        -21.859673
                                    ]
                                ]
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "5b8c9c106e63b329cf764c5b",
                            "name": "Jerovia - A12"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                        -60.749415,
                                        -21.903979
                                    ],
                                    [
                                        -60.749403,
                                        -21.90626
                                    ],
                                    [
                                        -60.749406,
                                        -21.908444
                                    ],
                                    [
                                        -60.730063,
                                        -21.908529
                                    ],
                                    [
                                        -60.730055,
                                        -21.90626
                                    ],
                                    [
                                        -60.730035,
                                        -21.903993
                                    ],
                                    [
                                        -60.749415,
                                        -21.903979
                                    ]
                                ]
                            ]
                        }
                    },
                    {
                        "type": "Feature",
                        "properties": {
                            "id": "5b8c9c7f6e63b329cf764c5d",
                            "name": "Jerovia - C9"
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [
                                        -60.749333,
                                        -21.87043
                                    ],
                                    [
                                        -60.729954,
                                        -21.87053
                                    ],
                                    [
                                        -60.73004,
                                        -21.875076
                                    ],
                                    [
                                        -60.746133,
                                        -21.87494
                                    ],
                                    [
                                        -60.749343,
                                        -21.872319
                                    ],
                                    [
                                        -60.749333,
                                        -21.87043
                                    ]
                                ]
                            ]
                        }
                    }
                ]
            })

        # when
        check_aoi = Context(session).get(helper)

        assert not isinstance(check_aoi, Error)


if __name__ == '__main__':
    unittest.main()
