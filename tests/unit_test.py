import unittest
from kladama.info import *
from kladama.operations import *
from kladama.queries import *


class UnitTest(unittest.TestCase):

    @staticmethod
    def test_aoi_urls():
        assert Query().aoi.url_path == '/aoi'
        assert Query().aoi.by_key('aoi-name').url_path == '/aoi/aoi-name'
        assert Query().aoi.by_user('user-name').url_path == '/aoi/user/user-name'
        assert Query().aoi.by_user('user-name').by_key('aoi-name').url_path == '/aoi/user/user-name/aoi-name'

    @staticmethod
    def test_aoi_validation_urls():
        assert SystemInfo.check_aoi({}).url_path == '/do/aoivalidation'
        assert SystemInfo.check_aoi({}).method == 'post'

    @staticmethod
    def test_phenom_urls():
        assert Query().phenom.url_path == '/phenom'
        assert Query().phenom.forecast.url_path == '/phenom/forecast'
        assert Query().phenom.observed.url_path == '/phenom/observed'
        assert Query().phenom.by_key('phenomena-name').url_path == '/phenom/phenomena-name'
        assert Query().phenom.by_sources('source-1').url_path == '/phenom/src/source-1'
        assert Query().phenom.by_sources('source-1', 'source-2').url_path == '/phenom/src/source-1,source-2'
        assert Query().phenom.by_sources('source-1').observed.url_path == '/phenom/src/source-1/observed'
        assert Query().phenom.by_sources('source-1').forecast.url_path == '/phenom/src/source-1/forecast'

    @staticmethod
    def test_organization_urls():
        assert Query().org.url_path == '/org'
        assert Query().org.by_key('organization-name').url_path == '/org/organization-name'

    @staticmethod
    def test_source_urls():
        assert Query().src.url_path == '/src'
        assert Query().src.forecast.url_path == '/src/forecast'
        assert Query().src.observed.url_path == '/src/observed'
        assert Query().src.by_key('source-name').url_path == '/src/source-name'
        assert Query().src.by_phenomena('phenomena-name').url_path == '/src/phenom/phenomena-name'
        assert Query().src.by_phenomena('phenomena-name').observed.url_path == '/src/phenom/phenomena-name/observed'
        assert Query().src.by_phenomena('phenomena-name').forecast.url_path == '/src/phenom/phenomena-name/forecast'

    @staticmethod
    def test_schedule_urls():
        assert Query().schedule.url_path == '/schedule'
        assert Query().schedule.by_user('u1').url_path == '/schedule/user/u1'
        assert Query().schedule.by_user('u1').by_subsc('s1').url_path == '/schedule/user/u1/subsc/s1'
        assert Query().schedule.by_user('u1').by_subsc('s1', 's2').url_path == '/schedule/user/u1/subsc/s1,s2'

    @staticmethod
    def test_subscription_url():
        assert Query().subsc.url_path == '/subsc'

    @staticmethod
    def test_subscription_by_users_url():
        assert Query().subsc.by_user('user-name').url_path == '/subsc/user/user-name'

    @staticmethod
    def test_subscription_by_key_urls():
        assert Query().subsc.by_key('subscription-key').url_path == '/subsc/subscription-key'
        assert Query().subsc.by_user('user-name').by_key('subscription-key').url_path == '/subsc/user/user-name/subscription-key'

    @staticmethod
    def test_subscription_by_key_dates_urls():
        assert Query().subsc.by_key('subscription-key').dates.url_path == '/subsc/subscription-key/dates'
        assert Query().subsc.by_key('subscription-key').dates_since('20200115').url_path == '/subsc/subscription-key/dates/20200115TONOW'
        assert Query().subsc.by_key('subscription-key').dates_in('20200115', '20200120').url_path == '/subsc/subscription-key/dates/20200115TO20200120'

    @staticmethod
    def test_subscription_by_status_urls():
        assert Query().subsc.by_status(1).url_path == '/subsc/status/1'
        assert Query().subsc.by_user('user-name').by_status(1).url_path == '/subsc/user/user-name/status/1'

    @staticmethod
    def test_subscription_results_urls():
        assert Query().subsc.by_user('user-name').by_key('subscription').results.last.url_path == '/subsc/user/user-name/subscription/results/last'
        assert Query().subsc.by_user('user-name').by_key('subscription').results.last_n(5).url_path == '/subsc/user/user-name/subscription/results/last5'
        assert Query().subsc.by_user('user-name').by_key('subscription').results.last_n_years(5, '20200101', '20200215').url_path == '/subsc/user/user-name/subscription/results/5years/20200101,20200215'
        assert Query().subsc.by_user('user-name').by_key('subscription').results.around(5, '20200101', '20200215').url_path == '/subsc/user/user-name/subscription/results/5around/20200101,20200215'
        assert Query().subsc.by_user('user-name').by_key('subscription').results.dates('20200101', '20200215').url_path == '/subsc/user/user-name/subscription/results/dates/20200101,20200215'
        assert Query().subsc.by_user('user-name').by_key('subscription').results.period('20200101', '20200215').url_path == '/subsc/user/user-name/subscription/results/period/20200101TO20200215'

    @staticmethod
    def test_variables_urls():
        assert Query().var.url_path == '/var'
        assert Query().var.forecast.url_path == '/var/forecast'
        assert Query().var.observed.url_path == '/var/observed'
        assert Query().var.by_key('var-name').url_path == '/var/var-name'
        assert Query().var.by_phenomena('phenomena-name').url_path == '/var/phenom/phenomena-name'
        assert Query().var.by_phenomena('phenomena-name').observed.url_path == '/var/phenom/phenomena-name/observed'
        assert Query().var.by_phenomena('phenomena-name').forecast.url_path == '/var/phenom/phenomena-name/forecast'
        assert Query().var.by_sources('source-1').url_path == '/var/src/source-1'
        assert Query().var.by_sources('source-1', 'source-2').url_path == '/var/src/source-1,source-2'
        assert Query().var.by_sources('source-1').observed.url_path == '/var/src/source-1/observed'
        assert Query().var.by_sources('source-1').forecast.url_path == '/var/src/source-1/forecast'

    @staticmethod
    def test_create_aoi_url_path():
        operation = Operations()\
            .add_aoi\
            .for_user("fake-user-name")\
            .with_name("fake-aoi-id")\
            .with_description("fake-aoi-name")\
            .with_category("fake-category-name")

        assert operation.url_path == '/aoi/user/fake-user-name/fake-aoi-id'

    @staticmethod
    def test_delete_aoi_url_path():
        operation = Operations()\
            .delete_aoi\
            .from_user("fake-user-name")\
            .with_aoi("fake-aoi-id")

        assert operation.url_path == '/aoi/user/fake-user-name/fake-aoi-id'

    @staticmethod
    def test_create_subscription_url_path():
        operation = Operations()\
            .periodic_subsc\
            .for_user("fake-user-name")\
            .with_variable("fake-var-name")\
            .with_operation("fake-oper-name")\
            .with_aoi("fake-aoi-name")

        assert operation.url_path == '/subsc/user/fake-user-name'

    @staticmethod
    def test_delete_subscription_url_path():
        operation = Operations()\
            .unsubscribe\
            .from_user("fake-user-name")\
            .with_subsc("fake-subsc-id")

        assert operation.url_path == '/subsc/user/fake-user-name/fake-subsc-id'


if __name__ == '__main__':
    unittest.main()
