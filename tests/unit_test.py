import unittest
from kladama import *


class UnitTest(unittest.TestCase):

    @staticmethod
    def test_query_url_paths():
        assert Query().aoi.url_path == '/aoi'
        assert Query().aoi.by_name('aoi-name').url_path == '/aoi/aoi-name'
        assert Query().aoi.by_user('user-name').url_path == '/aoi/user/user-name'
        assert Query().aoi.by_user('user-name').filter_by('aoi-name').url_path == '/aoi/user/user-name/aoi-name'

        assert Query().phenom.url_path == '/phenom'
        assert Query().phenom.forecast.url_path == '/phenom/forecast'
        assert Query().phenom.observed.url_path == '/phenom/observed'
        assert Query().phenom.by_name('phenomena-name').url_path == '/phenom/phenomena-name'
        assert Query().phenom.by_sources('source-1').url_path == '/phenom/src/source-1'
        assert Query().phenom.by_sources('source-1', 'source-2').url_path == '/phenom/src/source-1,source-2'
        assert Query().phenom.by_sources('source-1').observed.url_path == '/phenom/src/source-1/observed'
        assert Query().phenom.by_sources('source-1').forecast.url_path == '/phenom/src/source-1/forecast'

        assert Query().org.url_path == '/org'
        assert Query().org.by_name('organization-name').url_path == '/org/organization-name'

        assert Query().src.url_path == '/src'
        assert Query().src.forecast.url_path == '/src/forecast'
        assert Query().src.observed.url_path == '/src/observed'
        assert Query().src.by_name('source-name').url_path == '/src/source-name'
        assert Query().src.by_phenomena('phenomena-name').url_path == '/src/phenom/phenomena-name'
        assert Query().src.by_phenomena('phenomena-name').observed.url_path == '/src/phenom/phenomena-name/observed'
        assert Query().src.by_phenomena('phenomena-name').forecast.url_path == '/src/phenom/phenomena-name/forecast'

        assert Query().subsc.url_path == '/subsc'
        assert Query().subsc.by_name('subscription-name').url_path == '/subsc/subscription-name'
        assert Query().subsc.by_user('user-name').url_path == '/subsc/user/user-name'
        assert Query().subsc.by_user('user-name').filter_by('subscription-name') \
                   .url_path == '/subsc/user/user-name/subscription-name'

        assert Query().var.url_path == '/var'
        assert Query().var.forecast.url_path == '/var/forecast'
        assert Query().var.observed.url_path == '/var/observed'
        assert Query().var.by_name('var-name').url_path == '/var/var-name'
        assert Query().var.by_phenomena('phenomena-name').url_path == '/var/phenom/phenomena-name'
        assert Query().var.by_phenomena('phenomena-name').observed.url_path == '/var/phenom/phenomena-name/observed'
        assert Query().var.by_phenomena('phenomena-name').forecast.url_path == '/var/phenom/phenomena-name/forecast'
        assert Query().var.by_sources('source-1').url_path == '/var/src/source-1'
        assert Query().var.by_sources('source-1', 'source-2').url_path == '/var/src/source-1,source-2'
        assert Query().var.by_sources('source-1').observed.url_path == '/var/src/source-1/observed'
        assert Query().var.by_sources('source-1').forecast.url_path == '/var/src/source-1/forecast'

        assert Query().subsc.by_user('user-name').filter_by('subscription').last\
                   .url_path == '/subsc/user/user-name/subscription/last'
        assert Query().subsc.by_user('user-name').filter_by('subscription').last_n(5)\
                   .url_path == '/subsc/user/user-name/subscription/last5'
        assert Query().subsc.by_user('user-name').filter_by('subscription').last_years(5, '20200101', '20200215')\
                   .url_path == '/subsc/user/user-name/subscription/5years/20200101,20200215'
        assert Query().subsc.by_user('user-name').filter_by('subscription').around(5, '20200101', '20200215')\
                   .url_path == '/subsc/user/user-name/subscription/5around/20200101,20200215'
        assert Query().subsc.by_user('user-name').filter_by('subscription').dates('20200101', '20200215')\
                   .url_path == '/subsc/user/user-name/subscription/dates/20200101,20200215'
        assert Query().subsc.by_user('user-name').filter_by('subscription').period('20200101', '20200215')\
                   .url_path == '/subsc/user/user-name/subscription/period/20200101TO20200215'

    @staticmethod
    def test_create_aoi_url_path():
        operation = Operations()\
            .create_aoi\
            .set_user("fake-user-name")\
            .set_aoi_id("fake-aoi-id")\
            .set_name("fake-aoi-name")\
            .set_category("fake-category-name")

        assert operation.url_path == '/aoi/user/fake-user-name/fake-aoi-id'

    @staticmethod
    def test_delete_aoi_url_path():
        operation = Operations()\
            .delete_aoi\
            .set_user("fake-user-name")\
            .set_area_of_interest_id("fake-aoi-id")

        assert operation.url_path == '/aoi/user/fake-user-name/fake-aoi-id'

    @staticmethod
    def test_create_subscription_url_path():
        operation = Operations()\
            .create_periodic_subsc\
            .set_user("fake-user-name")\
            .set_variable_name("fake-var-name")\
            .set_variable_source_name("fake-var-src-name")\
            .set_spatial_operation_name("fake-oper-name")\
            .set_aoi_name("fake-aoi-name")

        assert operation.url_path == '/subsc/user/fake-user-name'

    @staticmethod
    def test_delete_subscription_url_path():
        operation = Operations()\
            .delete_subsc\
            .set_user("fake-user-name")\
            .set_subscription_id("fake-subsc-id")

        assert operation.url_path == '/subsc/user/fake-user-name/fake-subsc-id'


if __name__ == '__main__':
    unittest.main()
