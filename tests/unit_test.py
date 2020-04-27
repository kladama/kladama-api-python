import unittest
from kladama.queries import Query


class UnitTest(unittest.TestCase):

    @staticmethod
    def test_url_paths():

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


if __name__ == '__main__':
    unittest.main()
