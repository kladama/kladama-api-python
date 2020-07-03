import datetime
import unittest
from kladama import authenticate
from kladama import Environments
from kladama.context import *
from kladama.entities import *


def _get_dev_session():
    env = Environments().dev
    api_token = 'ANYTHING_WORKS_NOW'
    return authenticate(env, api_token)


class OperationIntegrationTest(unittest.TestCase):
    user = 'dev'

    @classmethod
    def setUpClass(cls) -> None:
        now_timestamp = datetime.datetime.now().timestamp()
        cls.aoi_name = 'test_aoi_{0}'.format(now_timestamp)

    def test_create_delete_aoi(self):
        # when
        creation_response = self._create_test_aoi(self.user, self.aoi_name)

        # then
        self.fail_if_error(creation_response)

        # and when
        deletion_response = self._delete_test_aoi(self.user, self.aoi_name)

        # then
        self.fail_if_error(deletion_response)

    def test_create_delete_subscription(self):
        # given
        self._create_test_aoi(self.user, self.aoi_name)

        # when
        creation_response = self._create_test_periodic_subscription(self.user, self.aoi_name)

        # then
        self.fail_if_error(creation_response)

        code = creation_response.result['code']
        assert isinstance(code, str)

        # and when
        deletion_response = self._delete_test_subscription(self.user, code)

        # then
        self.fail_if_error(deletion_response)

        # cleanup
        self._delete_test_aoi(self.user, self.aoi_name)

    def test_check_reschedule_clear_schedule_by_user(self):
        # when
        response = self._check_schedule('dev')

        # then
        self.fail_if_error(response)

        # and when
        reschedule_response = self._clear_schedule('dev')

        # then
        self.fail_if_error(reschedule_response)

        # and when
        clear_response = self._clear_schedule('dev')

        # then
        self.fail_if_error(clear_response)

    # private members

    @staticmethod
    def _get_context():
        session = _get_dev_session()
        return Context(session)

    @staticmethod
    def _create_test_aoi(user, aoi_name):
        create_operation = Operations() \
            .add_aoi \
            .for_user(user) \
            .with_name(aoi_name) \
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

    def _create_test_periodic_subscription(self, user, aoi_id):
        ctx = OperationIntegrationTest._get_context()
        var_query = Query().var
        variables = ctx.get(var_query)
        self.failIf(len(variables.result) == 0, "Cannot find variables to be used in subscriptions")

        first_var: Variable = variables.result[0]

        create_operation = Operations() \
            .periodic_subsc \
            .for_user(user) \
            .with_variable(first_var.name) \
            .with_operation("MEAN") \
            .with_aoi(aoi_id)

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

    @staticmethod
    def _check_schedule(user, *subscriptions):
        operation = Operations()\
            .check_schedule\
            .for_user(user)\
            .for_subsc(*subscriptions)

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(operation)

    @staticmethod
    def _clear_schedule(user, *subscriptions):
        operation = Operations()\
            .clear_schedule\
            .for_user(user)\
            .for_subsc(*subscriptions)

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(operation)

    @staticmethod
    def _re_schedule(user, *subscriptions):
        operation = Operations()\
            .re_schedule\
            .for_user(user)\
            .for_subsc(*subscriptions)

        ctx = OperationIntegrationTest._get_context()
        return ctx.execute(operation)

    def fail_if_error(self, response):
        self.failIf(isinstance(response, Error), response.__str__())


class QueryIntegrationTest(unittest.TestCase):

    _user = 'dev_it'
    _empty_subscription = 'FA66FH1EUG2KSKUZPFIHNLY7F536SM'
    _subscription = '35XY51E5M2Z1QI6VRDB766LHPO038K'

    def test_areas_of_interest(self):
        print('Testing Areas of Interest ========================')

        # given
        session = _get_dev_session()
        query = Query().aoi

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for aoi in res.result:
            self.assertIsInstance(aoi, AreaOfInterest)
            print(aoi.name, '-', aoi.description, 'in', aoi.link)

        print('\n')

    def test_get_areas_of_interest_by_user_dev(self):
        print('Testing Areas of Interest for user dev ========================')

        # given
        session = _get_dev_session()
        query = Query().aoi.by_user(self._user)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for aoi in res.result:
            self.assertIsInstance(aoi, AreaOfInterest)
            print(aoi.name, '-', aoi.description, 'in', aoi.link)

        print('\n')

    def test_variables(self):
        print('Testing Variables ========================')

        # given
        session = _get_dev_session()
        query = Query().var

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for var in res.result:
            self.assertIsInstance(var, Variable)
            print(var.name, 'from', var.source.name, 'in', var.link)

        print('\n')

    def test_sources(self):
        print('Testing Sources ========================')

        # given
        session = _get_dev_session()
        query = Query().src

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for source in res.result:
            self.assertIsInstance(source, Source)
            print(source.name, ':', source.description, 'in', source.link)

        print('\n')

    def test_get_source_by_name(self):

        # given
        source_names = [
            'ECMWF',
            'NOAA-NWS',
            'NOAA-CPC',
            'NOAA-STAR',
            'ESA',
        ]
        session = _get_dev_session()
        ctx = Context(session)

        for source_name in source_names:
            print('Testing Source by name: ', source_name, ' ========================')

            # given
            query = Query().src.by_key(source_name)

            # when
            res = ctx.get(query)

            # then
            self.assertIsInstance(res, Success, res.__str__())
            self.assertIsInstance(res.result, Source)
            self.assertEqual(res.result.name, source_name)
            print(source_name, ':', res.result.description, 'in', res.result.link)
            print('\n')

    def test_phenomenas(self):
        print('Testing Phenoms ========================')

        # given
        session = _get_dev_session()
        query = Query().phenom

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for phenom in res.result:
            self.assertIsInstance(phenom, Phenomena)
            print(phenom.name, ':', phenom.description, 'in', phenom.link)

        print('\n')

    def test_phenoms_by_not_existing_name(self):
        print('Testing Phenom by not existing name ========================')

        # given
        session = _get_dev_session()
        query = Query().phenom.by_key('FAKE NAME')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Error, res.__str__())
        self.assertEqual(404, res.code)
        print('Expected error message: {0}'.format(res.message))

    def test_get_phenomena_by_name(self):

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
        session = _get_dev_session()
        ctx = Context(session)

        for phenom_name in phenom_names:
            print('Testing Phenom by name: ', phenom_name, ' ========================')

            # given
            query = Query().phenom.by_key(phenom_name)

            # when
            res = ctx.get(query)

            # then
            self.assertIsInstance(res, Success, res.__str__())
            self.assertIsInstance(res.result, Phenomena)
            self.assertEqual(res.result.name, phenom_name)
            print(phenom_name, ':', res.result.description, 'in', res.result.link)
            print('\n')

    def test_get_phenomena_from_esa_and_cpc(self):
        print('Testing Phenom from ESA and NOAA-CPC ========================')

        # given
        session = _get_dev_session()
        query = Query().phenom.by_sources('ESA', 'NOAA-CPC')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for phenomena in res.result:
            self.assertIsInstance(phenomena, Phenomena)
            print(phenomena.name, ':', phenomena.description, 'in', phenomena.link)
            print('\n')

    def test_organizations(self):
        print('Testing Organizations ========================')

        # given
        session = _get_dev_session()
        query = Query().org

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for organization in res.result:
            self.assertIsInstance(organization, Organization)
            print(organization.name, ':', organization.acronym, 'in', organization.link)

        print('\n')

    def test_users(self):
        print('Testing Users ========================')

        # given
        session = _get_dev_session()
        query = Query().user

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for user in res.result:
            self.assertIsInstance(user, User)
            print(user.username, 'from', user.organization.name, 'in', user.link)

        print('\n')

    def test_schedules(self):
        print('Testing Schedules ========================')

        # given
        session = _get_dev_session()
        query = Query().schedule

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        for schedule in res.result:
            self.assertIsInstance(schedule, Schedule)
            print(schedule.user, 'has job:', schedule.job_id, 'that is executed', schedule.cron_exp)

        print('\n')

    def test_schedules_by_users(self):
        print('Testing Schedules ========================')

        # given
        session = _get_dev_session()
        query = Query().schedule.by_user(self._user)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        for schedule in res.result:
            self.assertIsInstance(schedule, Schedule)
            print(schedule.user, 'has job:', schedule.job_id, 'that is executed', schedule.cron_exp)

        print('\n')

    def test_subscriptions(self):
        print('Testing Subscriptions ========================')

        # given
        session = _get_dev_session()
        query = Query().subsc

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for subscription in res.result:
            self.assertIsInstance(subscription, Subscription)
            print(subscription.code, 'from', subscription.owner, 'in', subscription.link)

        print('\n')

    def test_subscriptions_by_active_status(self):
        print('Testing Subscriptions ========================')

        # given
        session = _get_dev_session()
        query = Query().subsc.by_status(1)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(len(res.result) > 0)
        for subscription in res.result:
            self.assertIsInstance(subscription, Subscription)
            self.assertEqual(1, subscription.status)
            print(subscription.code, 'from', subscription.owner, 'in', subscription.link)

        print('\n')

    def test_subscriptions_by_user_with_active_status(self):
        print('Testing Subscriptions ========================')

        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_status(1)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        for subscription in res.result:
            self.assertIsInstance(subscription, Subscription)
            self.assertEqual(1, subscription.status)
            print(subscription.code, 'from', subscription.owner, 'in', subscription.link)

        print('\n')

    def test_subscriptions_by_user_get_dates(self):
        print('Testing Subscriptions ========================')

        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).dates

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        print(res.__str__())
        print('\n')

    def test_subscriptions_by_user_with_dates(self):
        print('Testing Subscriptions ========================')

        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).dates_in('20200519', '20200622')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        print(res.__str__())
        print('\n')

    def test_around(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).results.around(5, '20200519', '20200622')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsInstance(res.result, BinaryResult)
        self.assertIn(self._subscription, res.result.name)
        self.assertTrue(len(res.result.content) > 0)

    def test_around_empty(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._empty_subscription).results.around(5, '20200105', '20200115')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsNone(res.result)

    def test_last(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).results.last

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsInstance(res.result, BinaryResult)
        self.assertIn(self._subscription, res.result.name)
        self.assertTrue(len(res.result.content) > 0)

    def test_last_empty(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._empty_subscription).results.last

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsNone(res.result)

    def test_last_n(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).results.last_n(5)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsInstance(res.result, BinaryResult)
        self.assertIn(self._subscription, res.result.name)
        self.assertTrue(len(res.result.content) > 0)

    def test_last_n_empty(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._empty_subscription).results.last_n(5)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsNone(res.result)

    def test_last_years(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).results.last_n_years(5, '20200519', '20200622')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsInstance(res.result, BinaryResult)
        self.assertIn(self._subscription, res.result.name)
        self.assertTrue(len(res.result.content) > 0)

    def test_last_years_empty(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._empty_subscription).results.last_n_years(5, '20200105', '20200115')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsNone(res.result)

    def test_subscriptions_result_dates(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).results.dates('20200519', '20200622')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsInstance(res.result, BinaryResult)
        self.assertIn(self._subscription, res.result.name)
        self.assertTrue(len(res.result.content) > 0)

    def test_subscriptions_result_dates_empty(self):
        # given
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._empty_subscription).results.last_n_years(5, '20200105', '20200115')

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsNone(res.result)

    def test_period(self):
        # given
        from_ = '20200101'
        to = '20200701'
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._subscription).results.period(from_, to)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsInstance(res.result, BinaryResult)
        self.assertIn(self._subscription, res.result.name)
        self.assertIn('{0}_TO_{1}'.format(from_, to), res.result.name)
        self.assertTrue(len(res.result.content) > 0)

    def test_period_empty(self):
        # given
        from_ = '20200101'
        to = '20200301'
        session = _get_dev_session()
        query = Query().subsc.by_user(self._user).by_key(self._empty_subscription).results.period(from_, to)

        # when
        res = Context(session).get(query)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertIsNone(res.result)


class SystemInfoTest(unittest.TestCase):

    def test_check_aoi(self):
        # given
        session = _get_dev_session()
        helper = SystemInfo\
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
        res = Context(session).get(helper)

        # then
        self.assertIsInstance(res, Success, res.__str__())
        self.assertTrue(res.result['valid'])


if __name__ == '__main__':
    unittest.main()
